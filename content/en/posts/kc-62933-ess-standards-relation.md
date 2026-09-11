---
title: "KC 62619, KC 10031, and KS C IEC 62933: Component Safety Standards and the ESS System Standard"
date: 2026-09-11 09:16:00+09:00
categories:
- policy
tags:
- second-life
- safety
draft: false
cover:
  image: /images/covers/kc-62933-ess-standards-relation.png
  alt: "KC 62619, KC 10031, and KS C IEC 62933: Component Safety Standards and the ESS System Standard"
  relative: false
---

A common shorthand among Korean ESS businesses goes like this: cells and modules are certified under KC 62619, and the complete ESS is certified under "KC 62933." If that were right, anyone building an ESS from used batteries would face an immediate question — after clearing KC 10031, does the repurposed system have to go through KC 62933 as well, or does KC 10031 stand in for it? This piece checks the premise before answering. The short version: in the editions of the safety act's standards list that we checked, there is no safety standard numbered KC 62933; the number 62933 is in use as a Korean Industrial Standard (KS). The next section spells out which editions were checked. From there, the piece sorts out where an ESS business actually runs into each standard, and how KC 10031 meets the installation rules when the batteries are second-life.

## What "62933" actually refers to: a KS, not a KC

The Korean Agency for Technology and Standards (KATS) keeps the full list of safety standards for products regulated under the Electrical Appliances and Consumer Products Safety Control Act in Annex 25 of its operating guidelines for that act. We compared the text of Annex 25 in two editions only: the edition posted on the National Law Information Center under KATS Notice No. 2024-66, and the full revised guidelines attached to the July 2026 administrative pre-announcement (KATS Public Notice No. 2026-201) — the latter a draft, not an issued notice. Neither lists a standard numbered 62933. We did not compare Annex 25 in any other edition. For the most recent issued amendment, Notice No. 2026-191, we checked only its announcement, which limits the changes to tablet PC classification and self-inspection items for single cells.

Where the number does appear is KS C IEC 62933-5-2, *Electrical energy storage (EES) systems — Part 5-2: Safety requirements for grid-integrated EES systems — Electrochemical-based systems*. It adopts IEC 62933-5-2 Ed.1.0 without modification (IDT), was established on May 31, 2019, was last reaffirmed on November 25, 2024, and sits under KATS. It covers grid-connected electrochemical storage systems and addresses safety across the whole system life, from design through operation and maintenance. In its June 2019 ESS safety measures, the government said it had established a KS covering the whole ESS system on May 31 of that year; the matching date suggests this is the standard it meant. What the industry calls "KC 62933," then, is not in itself a basis for any certification, confirmation, or inspection duty under the safety act.

## Where the two standards divide: the battery system versus the whole ESS

Both standards talk about a "system," but they don't mean the same thing. Annex 25 files KC 62619 under an item called "energy storage device components": lithium secondary single cells fall under safety certification, and lithium secondary battery systems fall under safety confirmation — but only up to a rated capacity of 300 kWh. Power conversion equipment (up to 2 MW rated) sits in the same item under its own standard, which shows how the act treats an ESS: not as one finished product, but as components managed separately. The "battery system" in KC 62619 is the battery side — cells, modules, and the BMS. How the cell and system procedures differ was covered in [KC 62619 Explained](https://current.arc.ai.kr/en/posts/kc-62619-used-battery-issues/).

The "system" in KS C IEC 62933-5-2 is the entire grid-connected storage installation. Korea's fire safety performance standard for energy storage facilities, NFPC 607, frames the device in a similar whole-installation way, defining an energy storage device as batteries, a battery management system, power conversion equipment, and an energy management system together. The "KC 62619 for cells and modules, KC 62933 for the system" shorthand appears to come from folding these two levels of "system" into one. Within the safety act, the two standards don't stack on each other.

## When an ESS business actually meets each one

For a business building an ESS from new batteries, KC 62619 shows up at procurement. Safety certification and confirmation are obtained by the manufacturer or importer that ships the product, so the ESS builder's job is to check that the cells and battery systems being delivered carry the right marks.

Installation runs on a different layer of rules. At this stage an ESS is typically handled as electrical equipment, under the Korea Electro-technical Code (KEC), which rests on the Electricity Business Act, and the pre-use inspection regime run by the Korea Electrical Safety Corporation (KESCO). KEC 511.2 requires, among other things, records of each secondary battery's replacement and manufacturing history, and it requires power conversion equipment outside the safety act to conform to a KS or perform at least as well. Fire protection follows NFPC 607. In checking these rules, we found no provision that makes conformity with KS C IEC 62933-5-2 mandatory. Whether a procurement spec or contract asks for it separately has to be checked project by project.

## Second-life ESS: how KC 10031 meets the installation rules

Repurposing used batteries into an ESS moves them onto a different track under the safety act. Annex 25 files KC 10031 under safety inspection and limits its scope to repurposed battery modules and repurposed battery systems rated at 300 kWh or less. The inspection itself was covered in [KC 10031: How Korea Actually Inspects Repurposed Batteries](https://current.arc.ai.kr/en/posts/kc-10031-reused-battery-inspection/), and the difference between safety certification, confirmation, and inspection in [A Used-Battery Glossary](https://current.arc.ai.kr/en/posts/used-battery-glossary/).

That answers the legal premise behind the central question. Because no KC 62933 appears in the editions of the safety act's standards list we checked, a repurposed system that has cleared KC 10031 neither becomes subject to KC 62933 nor has KC 10031 substitute for it — neither relationship exists. For KS C IEC 62933-5-2, we found no rule that treats a KC 10031 pass as meeting it, and none that requires it on top.

The question that actually matters sits at installation. KEC 511.2.5 applies the code's transport rules to every reused secondary battery, then asks three more things of reused secondary batteries the safety act does *not* cover: they must be marked as reused, their initial and remaining capacity must be marked, and they must meet the conformity requirements their manufacturer sets. The April 2023 amendment that introduced this clause (MOTIE Notice No. 2023-364) brought the part tied to the safety act's inspection category into force on October 19, 2023 — the day KC 10031 was established. Its supplementary provisions also set a transitional rule: until a relevant standard exists under the safety act or as a KS, a battery that meets its manufacturer's criteria counts as having passed an electrical-product safety confirmation test.

On its wording, the clause appears to leave KC 10031-inspected batteries, which the safety act covers, outside the extra requirements, and to aim those requirements at reused batteries outside the act's list. That is a reading of the text, not a confirmed practice. Public sources did not let us confirm whether repurposed systems above 300 kWh are in fact handled under those extra requirements, or what document a pre-use inspection accepts as proof of a KC 10031 result. The places to ask: KESCO for pre-use inspection documents; the Ministry of Climate, Energy and Environment, which now issues KEC amendments, for how 511.2.5 and its transitional rule apply; KATS — its operating guidelines name the Electrical and Telecommunication Products Safety Division as the responsible office — for the scope of the safety act; and the local fire authority for fire requirements. The KTL guidebook for KC 10031 itself notes that fire regulations for the end product may add use-specific requirements.

## What we see

The rules around ESS sit on different levels: the safety act works at the component level, the KEC and fire standards at the installation level, and the KS at the whole-system level. The name "KC 62933" looks like the product of collapsing those levels into one. For new-battery ESS, keeping the levels straight clears up most of the confusion. Second-life ESS is harder. The act's 300 kWh boundary overlaps with the two branches of KEC 511.2.5, and who verifies a large second-life system's conformity, and against what, is something we could not confirm from public materials. Because the transitional rule holds only until a safety-act or KS standard exists, this stretch remains one where the status of a future KS, any widening of the act's scope, and the KEC's interpretation each have to be checked on their own.

Source: [National Law Information Center] KATS Operating Guidelines, Annex 25: Status of Safety Standards for Regulated Electrical Products (KATS Notice No. 2024-66, effective Apr. 18, 2024) (https://www.law.go.kr/LSW/flDownload.do?flSeq=143407995&flNm=%5B%EB%B3%84%ED%91%9C+25%5D+%EC%95%88%EC%A0%84%EA%B4%80%EB%A6%AC%EB%8C%80%EC%83%81+%EC%A0%84%EA%B8%B0%EC%9A%A9%ED%92%88+%EC%95%88%EC%A0%84%EA%B8%B0%EC%A4%80+%ED%98%84%ED%99%A9(%EC%A0%9C63%EC%A1%B0+%EA%B4%80%EB%A0%A8)&bylClsCd=200201)

Source: [safetyguide.kr] KATS Public Notice No. 2026-201, Administrative Pre-announcement of Amendments to the Operating Guidelines (Jul. 1, 2026, full revised text attached) (http://www.safetyguide.kr/notiInstrucEstab/view?notificInstrucEstabId=18001&pageNum=1)

Source: [safetyguide.kr] KATS Notice No. 2026-191, Amendment to the Operating Guidelines (issued Jul. 31, 2026, effective Nov. 1, 2026) (http://www.safetyguide.kr/notiInstrucEstab/view?notificInstrucEstabId=18006&pageNum=1)

Source: [e-Nara Standards] KS C IEC 62933-5-2, Electrical energy storage (EES) systems — Part 5-2 (established May 31, 2019; reaffirmed Nov. 25, 2024) (https://standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?menuId=919&topMenuId=502&upperMenuId=503&ksNo=KSCIEC62933-5-2)

Source: [Korea.kr Policy Briefing] "ESS Accident Investigation Results and Safety Measures Announced" (Jun. 11, 2019) (https://www.korea.kr/news/policyNewsView.do?newsId=156335827)

Source: Korea Electro-technical Code 511.2.4–511.2.6 and supplementary provisions of MOTIE Notice No. 2023-364 (Apr. 17, 2023), Arts. 1 and 3 — per the full text as amended by MOTIE Notice No. 2023-875 (Dec. 14, 2023) (https://www.eom.co.kr/documents/1214%20%20%ED%95%9C%EA%B5%AD%EC%A0%84%EA%B8%B0%EC%84%A4%EB%B9%84%EA%B7%9C%EC%A0%95%20%EA%B0%9C%EC%A0%95%20%EC%A0%84%EB%AC%B8.pdf)

Source: [National Law Information Center] Korea Electro-technical Code (Ministry of Climate, Energy and Environment Notice No. 2025-227, effective Jan. 5, 2026) (https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000270772)

Source: [National Law Information Center] Fire Safety Performance Standard for Energy Storage Facilities (NFPC 607), Art. 3 (National Fire Agency Notice No. 2024-21, effective May 17, 2024) (https://www.law.go.kr/LSW/admRulInfoP.do?admRulSeq=2100000241004&lsId=80781&chrClsCd=010202)

Source: [KESCO] "Notice: ESS Pre-use Inspection Application Manual" (https://safety.kesco.or.kr/board/cyber/9/moveBbsNttDetail.do?nttSn=8872)

Source: [Korea Testing Laboratory (KTL)] "Reused Battery Safety Inspection System: Guide to Electrical Safety Standard KC 10031" (Jan. 2024) (https://customer.ktl.re.kr/afile/fileDownload/qUWmn)
