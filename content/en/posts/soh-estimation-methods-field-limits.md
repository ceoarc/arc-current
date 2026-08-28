---
title: "Ways to Estimate SOH, and Where They Break Down in the Field"
date: 2026-08-28 14:50:00+09:00
categories:
- tech
tags:
- second-life
draft: false
cover:
  image: /images/covers/soh-estimation-methods-field-limits.png
  alt: "Ways to Estimate SOH, and Where They Break Down in the Field"
  relative: false
---

[The Certification Path for Remanufactured Batteries](https://current.arc.ai.kr/en/posts/remanufactured-battery-certification-path/) covered Korea's pre-removal performance evaluation system, which grades retired EV batteries on three axes — performance, safety, and history — and sorts them into remanufacturing, reuse, or recycling. The performance axis is, in substance, remaining capacity: State of Health (SOH). Which grade a battery lands in decides whether it goes back into a car, into a second-life application like ESS, or back to raw material recovery. Even while the detailed grading criteria remain unwritten in subordinate legislation, the technical foundation underneath that grading — how SOH is actually measured — is worth laying out now. This piece covers what SOH means, what families of estimation methods exist, and why accuracy figures from lab studies on new cells don't carry over cleanly to the field.

## Why SOH resists a single definition

The most common definition of SOH is the ratio of a battery's current maximum charge capacity to its rated (or initial) capacity when new. Standards such as ISO 12405-4 and SAE J1798 don't fix this ratio directly; instead they standardize the capacity test procedure itself — constant-current or constant-power discharge at the cell, module, or pack level. SOH is then computed from that measured capacity as a follow-on step, which means the test conditions a standard specifies (current rate, temperature, rest time) can shift the resulting capacity value even for the same battery.

Capacity is not the only axis on which SOH gets defined, either. A resistance-based definition (SOH_R), tracking how much a battery's internal resistance has grown relative to when it was new, is also in wide use. Capacity fade and resistance rise reflect different degradation mechanisms and don't always move together at the same rate. On top of that, academic reviews repeatedly flag that characterization parameters defined at the cell level don't automatically transfer to modules or packs built from many cells in series and parallel — that mapping still needs its own justification. SOH, in other words, isn't a single standardized number so much as a value that requires first agreeing on what you're measuring against.

## Families of estimation methods

SOH estimation methods fall into roughly four families.

**Direct measurement** charges and discharges the battery and reads a physical quantity off it. The Reference Performance Test (RPT) is the baseline: full charge and discharge cycles at a fixed current rate (C/3, C/10, and similar) yield a measured capacity. Coulomb counting integrates current over time during charge/discharge to accumulate a capacity estimate. Open-circuit voltage (OCV) methods let the battery rest until its voltage settles, then back out remaining capacity from the known relationship between stabilized voltage and state of charge (SOC).

**Electrochemical methods** read the battery's internal reaction processes as a signal. Electrochemical impedance spectroscopy (EIS) applies a small AC perturbation across a frequency sweep (roughly a few mHz up to tens of kHz or more) and reads degradation off the shape of the resulting impedance spectrum. Incremental capacity analysis (ICA) and differential voltage analysis (DVA) differentiate the voltage curve during charge/discharge and track how the position and height of the resulting peaks shift, which correlates with capacity fade and specific aging mechanisms.

**Model-based methods** represent the battery as an equivalent circuit model or electrochemical model and use an estimator — typically a Kalman filter — to update model parameters in real time, estimating SOH alongside SOC. Because this only needs current and voltage sensors already on hand, it suits online estimation while the battery is in use.

**Data-driven (machine learning) methods** skip the physical model and learn degradation patterns directly from cycling history. Support vector regression, random forests, CNNs, and LSTMs are common choices, often fed the same signals the other three families extract — partial-charge voltage segments, impedance, resistance — as input features.

## The trade-off: accuracy, time, and equipment

The practical basis for choosing among these is how they trade off on three axes.

Full discharge capacity testing gives the most trustworthy reference value — it's the ground truth other methods get validated against — but a single full charge/discharge cycle takes hours, and it requires pulling the battery out of normal operation and onto dedicated cycler hardware.

Coulomb counting needs essentially no extra equipment, since it runs off the current sensor already built into the battery management system (BMS), but sensor error and initial-value error accumulate over time, so accuracy degrades the longer it runs. OCV methods likewise need no added hardware, but require a substantial rest period for voltage to settle, and the SOC-OCV relationship itself shifts with temperature and aging — a real constraint for real-time use.

EIS carries a lot of information, enough to distinguish between different aging mechanisms, but has traditionally required dedicated impedance-analyzer hardware capable of precise sweeps across a wide frequency band, adding cost and measurement time. Recent work is exploring ways to extract impedance-equivalent information from a BMS's existing current/voltage waveforms without separate instrumentation. ICA and DVA can work off partial-charge data — on the order of 10 to 20 minutes — rather than a full cycle, making them comparatively fast; under lab conditions, studies report mean absolute error around 1%.

Model-based methods suit online estimation with little added time cost, but the error figures reported for Kalman-filter-plus-equivalent-circuit-model approaches — typically 1-2% — come from standardized dynamic load profiles like DST (Dynamic Stress Test) and FUDS (Federal Urban Driving Schedule) run on new or lightly aged cells under controlled lab conditions. Data-driven accuracy figures are likewise mostly drawn from cells cycled to failure in a lab and validated against that same cycling data.

## Where this runs into trouble with retired batteries

The point worth underscoring is that nearly all the accuracy figures cited above come from a single chemistry, a single known history, cycled under controlled lab conditions on new cells. The field for retired EV batteries looks nothing like that.

First, history is uneven. A lab cell starts from a known degradation path; a battery pulled from a retired vehicle carries whatever driving pattern, maintenance record, and accident history that specific car had, so degradation state varies even within the same model. Neither the parameters a model-based method assumes nor the patterns a data-driven method has learned were built to represent that kind of heterogeneous history. Recent work has started reframing the problem as how quickly an "unknown" battery — with no prior information on chemistry, SOC, or SOH — can be sorted, which implicitly concedes that the earlier methods were designed on the assumption that history is known.

Second, pack-level and cell-level measurement are not the same problem. Literature reviews find that error at the cell level tends to run lower, and that the error band widens noticeably once you move to the pack level. Two things drive this. One is that variation among cells wired in series and parallel — mismatches in current, voltage, and temperature — adds uncertainty to a pack-wide SOH figure. The other is that as pack circuit topology grows more complex, electrochemical-model-based approaches stop being reliably applicable, pushing estimation toward data-driven methods by default. Retired batteries, however, mostly arrive as intact packs or modules, and breaking a pack down to test cells individually adds its own process and time.

Third, time and cost constraints run head-on into accuracy. The most trustworthy method — full discharge capacity testing — still takes hours per pack. A field that has to sort a high volume of retired batteries into grades on a short timeline can't run every unit through that. That pulls interest toward methods that use short-duration signals like partial-charge segments or impedance — but whether those methods hold onto the accuracy reported under new-cell lab conditions when applied to retired packs with mixed, unknown histories is a separate question that still needs its own verification.

## ARC's take

Most SOH estimation research to date has proven its accuracy under controlled lab conditions on new cells, and the problem of sorting retired packs of unknown history within a short window has only recently become its own line of research. Since Korea's pre-removal performance evaluation system has chosen to split remanufacturing, reuse, and recycling grades based on performance-test results, which SOH estimation method gets required — and under what conditions — for that grading will likely be a decisive factor in how practical it is to enter this business. Whether to trust a pack-level grading with its wider error band, or require cell-level retesting, is ultimately a policy choice about how much weight to put on accuracy versus processing time and cost.

References: [ISO] "ISO 12405-4:2018, Electrically propelled road vehicles — Test specification for lithium-ion traction battery packs and systems — Part 4" (https://www.iso.org/standard/71407.html)

References: [SAE International] "J1798_201911, Recommended Practice for Performance Rating of Electric Vehicle Battery Modules" (https://saemobilus.sae.org/standards/j1798_201911-recommended-practice-performance-rating-electric-vehicle-battery-modules)

References: [Battery Design] "State of Health (SOH)" (https://www.batterydesign.net/battery-management-system/state-of-health/)

References: [ScienceDirect, Applied Energy] "Enhanced Coulomb counting method for estimating state-of-charge and state-of-health of lithium-ion batteries" (https://www.sciencedirect.com/science/article/pii/S0306261908003061)

References: [ScienceDirect] "A comparative study of curve determination methods for incremental capacity analysis and state of health estimation of lithium-ion battery" (https://www.sciencedirect.com/science/article/abs/pii/S2352152X19317219)

References: [MDPI, Energies] "Joint State-of-Charge and State-of-Health Estimation Method Based on Equivalent Circuit Model and Data-Driven Model Fusion" (https://doi.org/10.3390/en19061567)

References: [IET, Energy Conversion and Economics] "State‐of‐health estimation of lithium‐ion batteries: A comprehensive literature review from cell to pack levels" (https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/enc2.12125)

References: [ScienceDirect] "Fast state of health estimation of unknown lithium-ion batteries for second-life and recycling assessment" (https://www.sciencedirect.com/science/article/abs/pii/S0378775326009146)

References: [arXiv] "Experimental Methods, Health Indicators, and Diagnostic Strategies for Retired Lithium-ion Batteries: A Comprehensive Review" (https://arxiv.org/abs/2512.01294)
