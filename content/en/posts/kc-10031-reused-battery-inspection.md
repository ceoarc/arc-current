---
title: "KC 10031: How Korea Actually Inspects Repurposed Batteries"
date: 2026-08-13T09:50:00+09:00
categories: ["policy"]
tags: ["second-life", "safety"]
draft: false
cover:
  image: "/images/covers/kc-10031-reused-battery-inspection.png"
  alt: "KC 10031: How Korea Actually Inspects Repurposed Batteries"
  relative: false
---

The certification a business actually has to clear to repurpose a used battery for another application isn't KC 62619. As the previous piece in this series, [KC 62619 Explained: Scope, Procedure, and Where It Strains Against Used Batteries](https://current.arc.ai.kr/en/posts/kc-62619-used-battery-issues/), laid out, KC 62619 was built around new industrial lithium cells, and that new-cell assumption strains against what a used battery actually is. Korea's government filled that gap with a separate safety inspection regime, detailed under KC 10031. This piece covers what KC 10031 actually governs, how far its scope reaches, what an inspection under it involves, and where that creates friction for a business trying to repurpose used batteries.

## The regime and why it exists

KC 10031 is an electrical-product safety standard notified by Korea's National Institute of Standards and Technology (KATS), formally titled "Safety Requirements for Lithium Secondary Batteries for Repurposing Used Batteries." Its legal basis is the Electrical Appliances and Consumer Products Safety Control Act. The amendment covering repurposed batteries was promulgated on October 18, 2022 and took effect on October 19, 2023. KC 10031 itself was notified the same day, October 19, 2023, as KATS Notice No. 2023-445. That amendment added a new category — items subject to safety inspection — under Chapter 6-2 of the act, and routed used batteries repurposed for another application through this inspection regime instead of KC 62619's safety certification or safety confirmation tracks.

The gap driving all this is between new-cell assumptions and what a used battery actually is. Driving history and charge-discharge history differ from vehicle to vehicle, so no two used batteries arrive in quite the same condition — a form of variance that a type-testing and factory-audit regime built for new cells isn't equipped to handle. KATS worked out the details through an administrative pre-announcement in April 2023, then phased the regime in with a grace period before enforcement began.

## Scope: what's covered, what isn't

KC 10031 governs two units. A repurposed battery module is a pack, module, or cell/cell block assembled to repurpose a used battery; a repurposed battery system is one or more of those modules combined into a system. The standard's own term for reassembling a used battery into a different application is "reassembly" (재조립, jojo-rip).

Scope comes with clear exclusions attached. First, a used battery going back into its original role as an EV drive battery falls outside KC 10031 — the same line KC 62619 itself draws by excluding automotive-use batteries from its own scope, as the previous piece described. Second, a recalled battery whose recall issue hasn't been resolved is excluded outright. Third, if the final product housing a repurposed battery system falls under fire-safety regulations with their own use-specific requirements, those requirements can apply on top of KC 10031, not in place of it.

## Inspection items and procedure

The two units don't carry equal inspection weight. A repurposed battery module goes through three pre-inspection items (serial number assignment and logging, related information, visual inspection) and five electrical inspection items (open-circuit voltage, insulation resistance, capacity, internal resistance, self-discharge) — and every single unit gets inspected, not a sample. That structure follows directly from what makes a used battery a used battery: no two units share the same history.

A repurposed battery system, instead, goes through functional safety review: overcharge voltage control, overcharge current control, and overheat control, tested once per model rather than unit by unit. This item is built by directly citing the battery-system functional safety review framework in KC 62619, Clause 8, and only an institution accredited by KOLAS (the Korea Laboratory Accreditation Scheme) can carry it out. An application also requires a business registration certificate, test samples, module and system specifications, a parts list, and labeling documentation.

Inspections run through safety inspection bodies designated by KATS. The initial order of designation ran Jeju Technopark (1st), the Korea Testing Laboratory / KTL (2nd), the Korea Testing Certification / KTC (3rd), and PMGrow (4th), with Sispia designated fifth in March 2024. Designations have kept expanding since, so the current full list is best checked directly against KATS's own notices rather than fixed in place here.

## Where it creates friction for a repurposing business

The first thing a business runs into is the full-inspection structure itself. Pre-inspection and electrical inspection on repurposed battery modules aren't sampled — every unit in a business's inventory goes through them. That's a direct response to unit-to-unit variance in used-battery history, but it comes back as a burden proportional to volume: inspect more units, repeat the process that many more times.

Second is what functional safety review actually is underneath. KC 10031 routes used batteries down a track separate from KC 62619, but the framework it uses to judge a repurposed battery system's functional safety is lifted directly from KC 62619 Clause 8. The regime avoids applying the new-cell standard to used batteries directly, while still borrowing its underlying judgment logic. That the only institutions qualified to run this item are KOLAS-accredited also narrows which inspection body a business can actually choose.

Third is the burden of tracing recall history. Because a battery with an unresolved recall issue is excluded from inspection at the outset, the business sourcing the used battery has to verify recall history on its own. And if the final product falls under fire-safety regulation, additional requirements can attach on top of a KC 10031 pass — so clearing KC 10031 alone doesn't always mean the process is finished.

## ARC's take

KC 10031 solved the mismatch between the new-cell standard (KC 62619) and used batteries by carving out a separate track, but look inside that track and it hasn't fully left the new-cell risk-analysis framework behind. Requiring full inspection on every module reads as an acknowledgment of unit-to-unit variance in used batteries. Leaning on KC 62619 Clause 8 for functional safety review reads as evidence that a fully independent safety-evaluation framework for used batteries specifically hasn't taken shape yet. How much this compromise actually slows a repurposing business down should become clearer as more inspection bodies get designated and more cases accumulate.

Source: [WTO TBT Notification] "KATS Notice No. 2023-0114, Administrative Pre-Announcement for Electrical Product Safety Standard KC 10031" (Apr. 17, 2023) (https://members.wto.org/crnattachments/2023/TBT/KOR/23_8951_00_x.pdf)

Source: [Korea Testing Laboratory (KTL)] "Repurposed Battery Safety Inspection System, Electrical Product Safety Standard KC 10031 Guide" (Jan. 2024) (https://customer.ktl.re.kr/afile/fileDownload/qUWmn)

Source: [Korea Battery Industry Association, Used Battery Industrialization Support Center] "Notice on Electrical and Consumer Products Safety Management Operating Guidelines and Electrical Product Safety Standard (KC10031)" (https://kbia-naju.or.kr/board.es?mid=a10702000000&bid=0002&act=view&list_no=4)

Source: [IndustryNews] "Reused Battery Safety Inspection Bodies Expand to Four — PMGrow First Manufacturer Designated" (https://www.industrynews.co.kr/news/articleView.html?idxno=51922)

Source: [Money Today] "Sispia Newly Designated as an 'Electrical Product Safety Inspection Body'" (Mar. 7, 2024) (https://news.mt.co.kr/mtview.php?no=2024030713011928450)
