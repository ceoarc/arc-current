---
title: Europe's SOH Disclosure Mandates Are Building a Battery Diagnostics Market
date: 2026-09-01 15:52:00+09:00
categories:
- policy
tags:
- second-life
- players
draft: false
cover:
  image: /images/covers/eu-soh-disclosure-diagnostic-market.png
  alt: Europe's SOH Disclosure Mandates Are Building a Battery Diagnostics Market
  relative: false
---

Two European rules are about to make a car's battery State of Health (SOH) something manufacturers and sellers can no longer keep to themselves. The Battery Passport becomes mandatory from 18 February 2027 for electric-vehicle batteries, batteries for light means of transport such as e-bikes, and industrial batteries above 2 kWh placed on the EU market. A European Commission guidance document, published 28 July 2026 and updated 15 August, lays out 71 data points across battery categories, each marked mandatory, optional, or conditional. Around the same time, Euro 7 (Regulation (EU) 2024/1257) sets minimum battery durability thresholds for new vehicle types and requires that the underlying SOH be made available to the owner through an in-vehicle monitor. New-type approvals must comply from 29 November 2026; registration of previously approved types that don't meet the requirement is barred from 29 November 2027.

## The rules asked first

What the two frameworks share is that neither had put a number on SOH before. The Battery Passport spells out *what* must be disclosed, data point by data point. Euro 7 goes further, expressing that SOH as two named metrics — State of Certified Energy (SOCE) and State of Certified Range (SOCR). Technical literature analyzing these metrics (including a paper in the journal *Vehicles*, MDPI) describes SOCE and SOCR as defined under UN GTR No. 22, which Euro 7 references, and calculated from a shortened WLTP procedure built on the WLTC drive cycle. That method, though, is scoped to new-type approval testing — it doesn't reach into how a battery already on the road gets diagnosed after the fact.

## The rules built a market

In Germany, diagnostics are already turning into a retail product ahead of that deadline. TÜV SÜD said in an 27 August press release that its battery-check service — which reads out remaining capacity as a percentage via the OBD interface and issues an inspection report — is now available at more than 100 of its service centers, with a phased nationwide rollout planned.

AVILOO, an Austrian battery-diagnostics firm, took the next step and turned the diagnosis into a warranty product. According to AVILOO's own announcement (reported by electrive.net), a battery bought used and tested below a vehicle-specific SOH threshold within one year or 20,000 km is covered for up to €3,000 under a warranty built on its FLASH Test — launched in France and Sweden in June, then extended to eight countries including Germany in July. The diagnosis is no longer just an inspection report; it now backs a financial product. The €3,000 cap and the eight-country count are AVILOO's own figures, not independently verified.

## A number alone isn't enough

As [SOH Estimation Methods and Their Field Limits](https://current.arc.ai.kr/en/posts/soh-estimation-methods-field-limits/) laid out, the same battery can yield different SOH values depending on which method and test conditions produced them. That problem doesn't go away just because a regulation now demands the number. Euro 7 pins down the SOCE/SOCR method — a WLTC-based test — but only for new-type approval. TÜV SÜD's OBD-based quick check and AVILOO's FLASH Test, both aimed at cars already in the field, run their own separate methodologies. Nor do the Battery Passport's data-point rules, or the interoperability standard published alongside it (Commission Implementing Decision (EU) 2026/1736), settle the measurement question — they govern how the data is formatted and exchanged, not how it was measured or under what conditions. That leaves room for the same car to carry different SOH numbers depending on who tested it and how.

## ARC's observation

South Korea's own version of this is arriving through an amendment to the Motor Vehicle Management Act, which routes a pre-removal performance assessment into three grades — remanufacturing, second-life reuse, or recycling. But the specific SOH measurement standard that will decide which grade a battery gets is still delegated to a Ministry of Land, Infrastructure and Transport ordinance yet to be written — see [The Certification Path for Remanufactured Batteries](https://current.arc.ai.kr/en/posts/remanufactured-battery-certification-path/) for how that framework is structured. Europe set the disclosure obligation first and is now working through the measurement-consistency question after the fact. That sequencing is worth watching as Korea's own subordinate legislation gets filled in.

Reference: [European Commission] "Digital Product Passport for Batteries (Battery Passport)" (https://single-market-economy.ec.europa.eu/single-market/digital-product-passport/batteries_en)

Reference: [European Commission] "Guidance Document: Digital Batteries Passport – data points by category" (https://single-market-economy.ec.europa.eu/document/download/cd1e5e6c-4a4a-4b99-995a-49eb6916187e_en?filename=Digital+Batteries+Passport+-+data+point+by+category.pdf)

Reference: [EUR-Lex] "Regulation (EU) 2024/1257 on type-approval of motor vehicles ... with respect to their emissions and battery durability (Euro 7)" (https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024R1257)

Reference: [European Parliament] "Euro 7: Deal on new EU rules to reduce road transport emissions" (https://www.europarl.europa.eu/news/en/press-room/20231207IPR15740/euro-7-deal-on-new-eu-rules-to-reduce-road-transport-emissions)

Reference: [MDPI, Vehicles] "Experimental Application of the Global Technical Regulation on In-Vehicle Battery Durability" (https://www.mdpi.com/2313-0105/9/9/454)

Reference: [TÜV SÜD, lifePR] "TÜV SÜD bietet neue Tests für Traktionsbatterien an" (https://www.lifepr.de/pressemitteilung/tv-sd/TV-SD-bietet-neue-Tests-fr-Traktionsbatterien-an/boxid/1071026)

Reference: [electrive.net] "3.000 Euro bei Akku-Defekt: Aviloo überführt Batteriediagnose in eigene Kaufgarantie" (https://www.electrive.net/2026/06/16/3-000-euro-bei-akku-defekt-aviloo-ueberfuehrt-batteriediagnose-in-eigene-kaufgarantie/)
