// Iterate over a list of NGOs, fill the Darpan search form (state, NPO name),
// read the captcha with Claude's help (file handshake), click Search, open
// the matching NPO's detail page, parse it, and write a clean JSON file
// straight into /ngos.
//
// Run: node scripts/fill_form.js
// Run one or more NGOs only: NGO_SLUG=slug1,slug2 node scripts/fill_form.js
//
// Captcha handshake:
//   1. This script screenshots the captcha canvas to scripts/captcha-current.png
//      and prints "CAPTCHA_READY: scripts/captcha-current.png" to stdout.
//   2. Claude reads that image and writes the characters (plain text, no
//      newline needed) into scripts/captcha-answer.txt.
//   3. This script polls for that file, reads it, types it in, clicks Search.

const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const URL = "https://ngodarpan.gov.in/#/search-ngo";
const SCRIPTS_DIR = __dirname;
const NGOS_DIR = path.join(SCRIPTS_DIR, "..", "ngos");
const CAPTCHA_IMG = path.join(SCRIPTS_DIR, "captcha-current.png");
const CAPTCHA_ANSWER = path.join(SCRIPTS_DIR, "captcha-answer.txt");
const SOURCE_URL = URL;
const COHORT = "core-cohort-2026";

// Each NGO lists every name variant worth trying (short/acronym and full
// legal name) — the portal's search sometimes only matches one or the other.
// Variants are tried in order; the first one that returns a result wins.
const NGOS = [
  {
    slug: "the-ant",
    names: ["The ANT", "The ANT (Action Northeast Trust)"],
    state: "Assam",
    district: "CHIRANG",
  },
  {
    slug: "diya-foundation",
    names: ["Diya Foundation"],
    state: "Assam",
    district: "KAMRUP",
  },
  { slug: "kabil", names: ["KABIL"], state: "Assam", district: "UDALGURI" },
  {
    slug: "satra",
    names: [
      "SATRA",
      "SATRA (Social Action for Appropriate Transformation & Advancement in Rural Areas)",
    ],
    state: "Assam",
    district: "DARRANG",
  },
  {
    slug: "projonmo",
    names: ["Projonmo"],
    state: "Assam",
    district: "KAMRUP METRO",
  },
  {
    slug: "mosonie-socio-economic-foundation",
    names: ["Mosonie Socio Economic Foundation", "Mosonie"],
    state: "Meghalaya",
    district: "Ri Bhoi",
  },
  {
    slug: "better-life-foundation",
    names: ["Better Life Foundation"],
    state: "Nagaland",
    district: "Tuensang",
  },
  {
    slug: "maneda",
    names: [
      "MANEDA",
      "MANEDA (Manipur North Economic Development Association)",
    ],
    state: "Manipur",
    district: "Senapati",
  },
  {
    slug: "pesch",
    names: ["Peoples Endeavour for Social Changes PESCH"],
    state: "Manipur",
    district: "Jiribam",
  },
  {
    slug: "prda",
    names: ["Peoples Resource Development Association"],
    state: "Manipur",
    district: "Bishnupur",
    filterByDistrict: true,
  },
  {
    slug: "snehpad",
    names: ["SOCIETY FOR NORTH EAST HANDMADE PAPER DEVELOPMENT"],
    state: "Assam",
    district: "JORHAT",
    filterByDistrict: true,
  },
  {
    slug: "ajagar-social-circle",
    names: ["Ajagar Social Circle"],
    state: "Assam",
    district: "GOALPARA",
  },
];

function escapeRegex(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

async function waitForCaptchaAnswer(timeoutMs = 600000) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    if (fs.existsSync(CAPTCHA_ANSWER)) {
      const text = fs.readFileSync(CAPTCHA_ANSWER, "utf-8").trim();
      if (text) {
        fs.unlinkSync(CAPTCHA_ANSWER);
        return text;
      }
    }
    await new Promise((r) => setTimeout(r, 1000));
  }
  throw new Error("Timed out waiting for scripts/captcha-answer.txt");
}

async function selectDropdown(page, formControlName, optionLabel) {
  await page
    .locator(`p-dropdown[formcontrolname="${formControlName}"]`)
    .click();
  await page.waitForTimeout(700);
  // Case-insensitive exact-text match: only Assam's on-portal district
  // casing has been verified so far, not Meghalaya/Nagaland/Manipur's.
  const option = page.locator(".p-dropdown-panel li[role='option']").filter({
    hasText: new RegExp(`^\\s*${escapeRegex(optionLabel)}\\s*$`, "i"),
  });
  await option.first().click();
  await page.waitForTimeout(700);
}

// A fixed sleep after clicking Search is a race: if the portal is slow to
// respond, the results table hasn't populated yet when we check it, and a
// genuinely-matching NGO gets misreported as NO_RESULTS. Poll instead —
// stop as soon as rows appear (fast path stays fast), but give it up to
// 15s before concluding there really are none.
async function waitForSearchToSettle(page, maxWaitMs = 30000) {
  const start = Date.now();
  while (Date.now() - start < maxWaitMs) {
    const rowCount = await page.locator("table tbody tr").count();
    if (rowCount > 0) return;
    await page.waitForTimeout(500);
  }
}

async function waitForDetailPageToLoad(detailPage, maxWaitMs = 20000) {
  const start = Date.now();
  while (Date.now() - start < maxWaitMs) {
    const darpanIdText = await detailPage
      .locator(".label-head", { hasText: "DARPAN ID" })
      .first()
      .locator("xpath=..")
      .innerText()
      .catch(() => "");
    if (darpanIdText && !darpanIdText.includes("--")) return;
    await detailPage.waitForTimeout(500);
  }
}

async function pickResultRow(page, nameVariant, district) {
  const rows = page.locator("table tbody tr");
  const rowCount = await rows.count();
  if (rowCount === 0) return null;

  const target = nameVariant.trim().toLowerCase();
  const targetDistrict = district ? district.trim().toLowerCase() : null;

  let bestLink = null;
  let bestScore = 0;
  for (let i = 0; i < rowCount; i++) {
    const link = rows.nth(i).locator("a").first();
    if ((await link.count()) === 0) continue;
    const nameText = (await link.innerText()).trim().toLowerCase();

    let score = 0;
    if (nameText === target) score += 10;
    if (targetDistrict) {
      const rowText = (await rows.nth(i).innerText()).toLowerCase();
      if (rowText.includes(targetDistrict)) score += 5;
    }

    if (score > bestScore) {
      bestScore = score;
      bestLink = link;
    }
  }

  if (!bestLink) {
    console.log(
      `NOTE: no exact name/district match among ${rowCount} result row(s) for "${nameVariant}" — using first row`
    );
    return rows.first().locator("a").first();
  }
  return bestLink;
}

// The captcha <canvas> redraws/clears on its own cycle, so checking "does
// it have content?" and then screenshotting a moment later can straddle
// that cycle and capture a blank frame — which the portal then rejects,
// silently mislabeling known-good NGO names as NOT_FOUND. Read the pixels
// via toDataURL() inside the SAME evaluate() call that checks contrast, so
// there's no gap. If still blank after a few tries, click the portal's
// captcha-refresh button to force a fresh draw.
async function screenshotCaptcha(page, imgPath, maxAttempts = 9) {
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    const dataUrl = await page.evaluate(() => {
      const canvas = document.querySelector("canvas.captcha-canvas");
      if (!canvas) return null;
      const ctx = canvas.getContext("2d");
      const { data } = ctx.getImageData(0, 0, canvas.width, canvas.height);
      let min = 255;
      let max = 0;
      for (let i = 0; i < data.length; i += 4) {
        const v = data[i];
        if (v < min) min = v;
        if (v > max) max = v;
      }
      if (max - min <= 20) return null;
      return canvas.toDataURL("image/png");
    });
    if (dataUrl) {
      const base64 = dataUrl.replace(/^data:image\/png;base64,/, "");
      fs.writeFileSync(imgPath, Buffer.from(base64, "base64"));
      return;
    }
    if (attempt % 3 === 0) {
      const refreshBtn = page.locator("button.captcha-refresh");
      if ((await refreshBtn.count()) > 0) await refreshBtn.first().click();
    }
    if (attempt < maxAttempts) await page.waitForTimeout(500);
  }
  console.log("WARNING: captcha canvas still looks blank after retries");
  await page.locator("canvas.captcha-canvas").screenshot({ path: imgPath });
}

// The Darpan detail page renders each section as a <p-card header="...">
// and repeats the full set of cards a second time (an off-screen
// <app-pdf-template> used for its own PDF generation) after the "View NPO
// Email" reveal click, with the real email instead of the masked one.
// Rather than hardcoding section names, discover every <p-card header="...">
// generically, keyed by a slugified header — so a section Darpan adds
// tomorrow (e.g. "Funding Details") shows up automatically under
// sections.funding_details. Where a header appears twice, the second
// occurrence wins, since it carries the revealed email.

function toKey(label) {
  return label
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "_")
    .replace(/^_+|_+$/g, "");
}

async function extractCardSections(detailPage) {
  const cards = detailPage.locator("p-card[header]");
  const count = await cards.count();
  const sections = {};

  for (let i = 0; i < count; i++) {
    const card = cards.nth(i);
    const header = (await card.getAttribute("header")).trim();
    const key = toKey(header);

    const hasTable = (await card.locator("table").count()) > 0;
    if (hasTable) {
      const columnKeys = (
        await card.locator("table tr").first().locator("th").allInnerTexts()
      ).map(toKey);
      const rowLocator = card.locator("table tr");
      const rowCount = await rowLocator.count();
      const rows = [];
      for (let r = 1; r < rowCount; r++) {
        const cells = await rowLocator.nth(r).locator("td").allInnerTexts();
        if (cells.length === 0) continue;
        const row = {};
        columnKeys.forEach((ck, idx) => {
          row[ck || `col_${idx}`] = (cells[idx] || "").trim();
        });
        rows.push(row);
      }
      sections[key] = rows;
      continue;
    }

    const labelLocator = card.locator(".label-head");
    const labelCount = await labelLocator.count();
    const pairs = [];
    for (let j = 0; j < labelCount; j++) {
      const labelEl = labelLocator.nth(j);
      const label = (await labelEl.innerText()).trim();
      const parentText = (await labelEl.locator("xpath=..").innerText()).trim();
      const value = parentText.startsWith(label)
        ? parentText.slice(label.length).trim()
        : parentText.replace(label, "").trim();
      pairs.push([toKey(label), value.replace(/\s+/g, " ")]);
    }

    // Group into repeating blocks: whenever a key repeats, start a new
    // group (this is what turns "Details of Achievements" — repeating
    // Year/Working Sector/Achievement/Best Practices — into an array,
    // generically, for any section that happens to repeat labels).
    const groups = [];
    let current = {};
    let seenInCurrent = new Set();
    for (const [k, v] of pairs) {
      if (seenInCurrent.has(k)) {
        groups.push(current);
        current = {};
        seenInCurrent = new Set();
      }
      current[k] = v;
      seenInCurrent.add(k);
    }
    if (Object.keys(current).length > 0) groups.push(current);

    sections[key] = groups.length > 1 ? groups : groups[0] || {};
  }

  return sections;
}

function findFieldAcrossSections(sections, fieldKey) {
  for (const value of Object.values(sections)) {
    if (!Array.isArray(value) && value && value[fieldKey] != null) {
      return value[fieldKey];
    }
  }
  return null;
}

async function parseDetailPage(detailPage, nameVariantHint) {
  const sections = await extractCardSections(detailPage);

  let entityName = null;
  const titleCount = await detailPage.locator(".title").count();
  if (titleCount > 0) {
    entityName = (await detailPage.locator(".title").first().innerText())
      .replace(/\s+/g, " ")
      .trim();
  }

  return {
    entity_type: "ngo",
    entity_name: entityName || nameVariantHint,
    darpan_id: findFieldAcrossSections(sections, "darpan_id"),
    cohort: COHORT,
    source: "darpan-portal",
    source_url: SOURCE_URL,
    status: "clean",
    sections,
  };
}

(async () => {
  if (fs.existsSync(CAPTCHA_ANSWER)) fs.unlinkSync(CAPTCHA_ANSWER);
  if (!fs.existsSync(NGOS_DIR)) fs.mkdirSync(NGOS_DIR, { recursive: true });

  const filterSlugs = process.env.NGO_SLUG
    ? process.env.NGO_SLUG.split(",").map((s) => s.trim())
    : null;
  const targets = filterSlugs
    ? NGOS.filter((n) => filterSlugs.includes(n.slug))
    : NGOS;

  const browser = await chromium.launch({ headless: false });

  for (const ngo of targets) {
    const outPath = path.join(NGOS_DIR, `ngo-darpan-${ngo.slug}.json`);
    if (fs.existsSync(outPath) && fs.statSync(outPath).size > 0) {
      console.log(`\n=== Skipping ${ngo.slug}: already saved ===`);
      continue;
    }

    console.log(`\n=== Processing: ${ngo.slug} (${ngo.names.join(" | ")}) ===`);
    const page = await browser.newPage();
    await page.goto(URL, { waitUntil: "domcontentloaded" });
    await page.waitForTimeout(4000);

    await selectDropdown(page, "selectedState", ngo.state);
    // District isn't filtered by default since it's the operational
    // district, which can differ from the portal's registered district
    // (e.g. Better Life Foundation: registered DIMAPUR, not Tuensang).
    // Opt in via `filterByDistrict: true` when they're known to match.
    if (ngo.district && ngo.filterByDistrict) {
      await selectDropdown(page, "selectedDistrict", ngo.district);
    }

    let found = false;

    for (const nameVariant of ngo.names) {
      console.log(`--- trying name: "${nameVariant}" ---`);
      await page.locator("#username").fill("");
      await page.locator("#username").fill(nameVariant);
      await page.waitForTimeout(500);

      await screenshotCaptcha(page, CAPTCHA_IMG);
      console.log(
        `CAPTCHA_READY: ${path.relative(process.cwd(), CAPTCHA_IMG)}`
      );

      const captchaText = await waitForCaptchaAnswer();
      console.log(`Got captcha answer: ${captchaText}`);
      if (fs.existsSync(CAPTCHA_IMG)) fs.unlinkSync(CAPTCHA_IMG);

      await page.locator("#captchaInput").fill(captchaText);
      await page.waitForTimeout(300);
      await page.getByRole("button", { name: "Search", exact: true }).click();
      await waitForSearchToSettle(page);

      const nameLink = await pickResultRow(page, nameVariant, ngo.district);
      if (!nameLink) {
        console.log(`NO_RESULTS for variant "${nameVariant}"`);
        continue;
      }

      const popupPromise = page
        .waitForEvent("popup", { timeout: 5000 })
        .catch(() => null);
      await nameLink.click();
      const popup = await popupPromise;
      const detailPage = popup || page;
      if (popup) await popup.waitForLoadState("domcontentloaded");
      await waitForDetailPageToLoad(detailPage);

      const viewEmailLink = detailPage.getByText("View NPO Email", {
        exact: false,
      });
      if ((await viewEmailLink.count()) > 0) {
        await viewEmailLink.first().click();
        await detailPage.waitForTimeout(1500);
      }

      const record = await parseDetailPage(detailPage, nameVariant);
      fs.writeFileSync(outPath, JSON.stringify(record, null, 2) + "\n");
      console.log(
        `SAVED: ngos/ngo-darpan-${ngo.slug}.json (matched on "${nameVariant}")`
      );

      if (popup) await popup.close();
      found = true;
      break;
    }

    if (!found) {
      fs.writeFileSync(outPath, "");
      console.log(
        `NOT_FOUND: ${ngo.slug} — wrote empty placeholder ngos/ngo-darpan-${ngo.slug}.json`
      );
    }

    await page.close();
  }

  console.log("\nAll NGOs processed. Closing browser in 5s...");
  await new Promise((r) => setTimeout(r, 5000));
  await browser.close();
})();
