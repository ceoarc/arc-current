---
title: "KC 62619 Explained: Scope, Procedure, and Where It Strains Against Used Batteries"
date: 2026-08-13T09:15:00+09:00
categories: ["policy"]
tags: ["second-life", "safety"]
draft: false
cover:
  image: "/images/covers/kc-62619-used-battery-issues.png"
  alt: "KC 62619 Explained: Scope, Procedure, and Where It Strains Against Used Batteries"
  relative: false
---

Anyone putting lithium batteries into an ESS runs into KC 62619 first. Written for new industrial lithium cells, it also reads like the natural starting point for businesses trying to repurpose retired EV batteries. Apply it in practice, though, and clauses built around a new-cell assumption start to strain against what a used battery actually is. This piece lays out what KC 62619 covers, how certification under it actually runs, and where that strain shows up when the object in front of you is a used battery rather than a new one. The certification path for remanufacturing — putting a used battery back into its original role — belongs to the next piece in this series.

## Scope: what it covers, and how much

KC 62619 is one of the electrical-product safety standards notified by Korea's National Institute of Standards and Technology (KATS), formally titled "Safety of Industrial Lithium Secondary Batteries." It adapts the international standard IEC 62619 — safety requirements for secondary lithium cells and batteries used in industrial applications, within the broader IEC 62619 family for alkaline and other non-acid electrolyte secondary cells — to domestic conditions. First notified in October 2019, it was updated to its current edition (Ed 2.0) in March 2023 to align with IEC 62619 Ed.2.0.

Its scope has widened across revisions. The original notice (Ed 1.0, 2019) limited scope to lithium batteries for energy storage systems and set only an upper bound: 300kWh rated capacity. The 2023 revision (Ed 2.0) added mobile/stationary energy storage devices, large-capacity auxiliary batteries (camping power banks among them), and mobile EV chargers as examples of covered applications, and introduced a 500Wh lower bound that wasn't there before. It governs both the cell level and the assembled battery level. Its legal basis sits in the Electrical Appliances and Consumer Products Safety Control Act and the enforcement rule's lists of items subject to safety certification and safety confirmation.

There's an exclusion attached to that scope, though. Batteries already under separate safety regimes by virtue of their end use — automotive, aircraft, rail, marine — fall outside KC 62619 entirely. That exclusion resurfaces later, when this piece turns to used batteries specifically.

## Procedure: cells and systems split apart

KC 62619 doesn't put the same procedural weight on cells and battery systems. A cell falls under safety certification: it has to pass both product testing and a factory audit, and stays under periodic post-certification review — repeated factory audits and product testing — after that. A battery system, which bundles in the module, pack, and battery management system, falls under the lighter safety confirmation track instead: pass product testing at a designated test lab, report the result, and that's it. No factory audit, no periodic post-certification review at this stage. Cells go through the heavier process of having the production process itself verified; systems go through the lighter process of having a finished product's test results checked.

## Where it strains against used batteries

KC 62619's type testing is built around new cells and systems as the test sample. Its pass/fail thresholds — rated capacity, internal resistance, allowable self-discharge — are pinned to just-off-the-line specs. Applying those same thresholds to a used battery that has already lost capacity and developed cell-to-cell variance through repeated charge-discharge cycles is an awkward fit at best. The standard's baseline assumption — that each cell is new — simply doesn't hold for a used battery.

The factory audit runs into the same problem from a different angle. Safety certification assumes the manufacturer controls the entire process from design through production, and audits whether that process holds quality steady. But a business repurposing used batteries for another application usually isn't designing and producing its own cells — it's taking cells and modules an EV maker already built and reassembling them. Because the original cell designer and the repurposing business are different parties, the repurposer often lacks full visibility into the cell's design-stage information, which doesn't mesh cleanly with factory audit items built around the assumption of a from-scratch manufacturer.

The government appears to recognize this gap institutionally. The amendment to the Electrical Appliances and Consumer Products Safety Control Act that covers repurposed batteries was promulgated on October 18, 2022 and took effect on October 19, 2023, adding a new category — items subject to safety inspection — under Chapter 6-2. When a used battery is repurposed for something other than its original role, it isn't routed through KC 62619's safety certification or safety confirmation tracks at all; it goes through this safety inspection regime instead. The detailed standard is KC 10031, formally titled "Safety Requirements for Lithium Secondary Batteries for Repurposing Used Batteries." The standard's own term for reassembling a used battery into another application is "reassembly" (재조립), and it sets separate inspection items for repurposed battery modules and the systems assembled from them.

That separate track connects back to the exclusion noted earlier. KC 62619 already excludes batteries under separate safety regimes by end use, including automotive — so a used battery returning to its original role as an EV drive battery was never inside KC 62619's scope to begin with. Repurposing for another application, like ESS, isn't caught by that exclusion and could plausibly sit inside KC 62619 instead — but the new-cell assumptions built into its type testing and factory audit, described above, mean it doesn't in practice. That's why KC 10031, not KC 62619, governs it. The existence of a dedicated track at all, rather than folding used batteries into the new-cell standard, is itself evidence that KC 62619 doesn't map cleanly onto used batteries.

## ARC's take

KC 62619 reading like an obstacle to used-battery reuse businesses doesn't look like a flaw in the standard — it looks like a standard built for new industrial cells being asked to do a job it wasn't written for. That a separate safety inspection regime (KC 10031) exists for used batteries suggests the distinction is recognized institutionally, not just in practice. What isn't settled by this piece alone is how cleanly the two regimes' test items actually line up with each other, or how clear the line is, in practice, for a repurposing business trying to figure out which standard applies to it.

Source: [KATS] "Electrical Product Safety Standard KC 62619: Safety of Industrial Lithium Secondary Batteries" (https://www.kats.go.kr/cwsboard/board.do?mode=download&bid=155&cid=21073&filename=21073_201910251526580981.pdf)

Source: [Korea Law Information Center] Administrative Rule "Electrical Product Safety Standard (KC 62619)" (https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000220898)

Source: [Korea Testing Laboratory (KTL)] "Notice of Revision to Electrical Product Safety Standard (KC 62619 Ed 2.0)" (https://customer.ktl.re.kr/web/contents/K501000000.do?schM=view&id=45048)

Source: [Korea Testing Laboratory (KTL)] "Repurposed Battery Safety Inspection System, Electrical Product Safety Standard KC 10031 Guide" (Jan. 2024) (https://customer.ktl.re.kr/afile/fileDownload/qUWmn)

Source: [Korea Testing Laboratory (KTL)] Energy Storage System Testing overview (https://customer.ktl.re.kr/web/contents/K102130200.do)
