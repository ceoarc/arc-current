---
title: SOH 추정 방식의 종류와 현장 적용 한계
date: 2026-08-28 14:50:00+09:00
categories:
- tech
tags:
- second-life
draft: false
cover:
  image: /images/covers/soh-estimation-methods-field-limits.png
  alt: SOH 추정 방식의 종류와 현장 적용 한계
  relative: false
---

[재제조 배터리의 인증 경로](https://current.arc.ai.kr/ko/posts/remanufactured-battery-certification-path/)에서 다룬 탈거 전 성능평가 제도는 사용후 배터리를 성능·안전성·이력 세 축으로 평가해 재제조·재사용·재활용 세 등급으로 나눈다. 이 중 성능 축의 실체는 잔존용량, 즉 SOH(State of Health, 건강 상태)다. 어느 등급으로 판정되느냐에 따라 배터리가 다시 전기차로 돌아갈지, ESS 같은 다른 용도로 재사용될지, 원료로 돌아갈지가 갈리므로, SOH를 어떻게 재느냐는 제도의 구체적 기준이 아직 하위법령에 남아 있는 지금도 미리 짚어둘 필요가 있는 기술적 토대다. 이 글은 SOH가 정확히 무엇을 뜻하는 값인지, 이를 추정하는 방식에 어떤 계열이 있는지, 그리고 신품 셀 연구실에서 나온 정확도가 사용후 배터리 현장에서는 왜 그대로 재현되지 않는지를 정리한다.

## SOH는 왜 하나의 정의로 통일돼 있지 않은가

SOH는 가장 널리 쓰이는 정의로 보면 배터리의 현재 최대 충전 가능 용량을 신품 시점의 정격 용량(또는 초기 용량)으로 나눈 비율이다. ISO 12405-4와 SAE J1798 같은 전기차 배터리 성능시험 표준은 이 비율 자체를 규정하기보다, 셀·모듈·팩 단위에서 정전류 또는 정전력 방식으로 용량을 측정하는 시험 절차를 표준화한다. SOH는 그 측정값을 신품 대비 비율로 계산하는 후속 절차로, 표준마다 시험 조건(전류율, 온도, 휴지 시간)이 다르면 같은 배터리라도 산출되는 용량 값이 달라질 수 있다.

문제는 용량만이 SOH를 정의하는 유일한 축이 아니라는 점이다. 배터리의 내부저항이 신품 대비 얼마나 늘었는지를 기준으로 삼는 저항 기반 정의(SOH_R)도 함께 쓰인다. 용량과 저항은 배터리 열화의 서로 다른 측면을 반영하기 때문에 둘이 항상 같은 방향, 같은 속도로 움직이지 않는다. 여기에 더해 셀 단위에서 통용되는 정의를 여러 셀이 직병렬로 묶인 모듈·팩 단위로 그대로 확장할 수 있는지도 별도로 정리돼야 하는 문제로 남아 있다는 지적이 학계 리뷰에서 반복적으로 나온다. 즉 SOH는 하나의 표준 수치가 아니라, 무엇을 기준으로 잴 것인지부터 합의가 필요한 값이다.

## 추정 방식의 계열

SOH 추정 방식은 크게 네 계열로 나뉜다.

**직접 측정 계열**은 배터리를 실제로 충방전시켜 물리량을 직접 읽는다. 완전방전 용량시험(RPT, Reference Performance Test)이 가장 기본으로, 정해진 전류율(C/3, C/10 등)로 완전 충전과 완전 방전을 반복해 실측 용량을 얻는다. 쿨롱 카운팅은 충방전 중 전류를 시간에 대해 적분해 용량을 누적 계산하는 방식이고, 개방회로전압(OCV) 방식은 배터리를 충분히 쉬게 한 뒤 안정된 전압과 충전상태(SOC)의 관계식에서 잔존용량을 역산한다.

**전기화학적 방식**은 배터리 내부의 반응 과정을 신호로 들여다본다. 전기화학 임피던스 분광법(EIS)은 여러 주파수(대략 수 mHz에서 수십~100kHz 대역)의 미세 교류 신호를 흘려 임피던스 스펙트럼을 얻고, 그 형태 변화에서 열화 정도를 읽는다. 증분용량분석(ICA)과 미분전압분석(DVA)은 충방전 중 전압 곡선을 미분해 나타나는 피크의 위치와 높이 변화를 통해 용량 저하와 열화 기전을 추정한다.

**모델 기반 방식**은 배터리를 등가회로모델이나 전기화학모델로 표현하고, 칼만필터 같은 추정기로 모델 파라미터를 실시간 갱신하면서 SOH를 함께 추정한다. 전류·전압 센서만으로 SOC와 SOH를 동시에 추정할 수 있다는 점에서 온라인(주행 중) 적용에 적합하다.

**데이터 기반(기계학습) 방식**은 물리 모델 대신 충방전 이력 데이터에서 패턴을 학습한다. 서포트벡터회귀, 랜덤포레스트, 합성곱신경망, LSTM 등이 쓰이며, 위 세 계열이 뽑아낸 신호(부분 충전 구간 전압, 임피던스, 저항 등)를 입력 특징으로 함께 활용하는 경우가 많다.

## 정확도·소요시간·필요 장비의 상충 관계

방식을 고르는 실질적 기준은 이 셋의 조합이다.

완전방전 용량시험은 가장 신뢰도 높은 기준 값을 준다는 점에서 다른 방식의 정확도를 검증하는 기준(ground truth)으로 쓰이지만, 완전 충방전 사이클 하나에 여러 시간이 걸리고 배터리를 정상 운용에서 빼내 전용 충방전 장비에 물려야 한다는 제약이 있다.

쿨롱 카운팅은 배터리관리시스템(BMS)에 이미 있는 전류 센서만으로 계산할 수 있어 별도 장비가 거의 필요 없지만, 전류 센서 오차와 초기값 오차가 시간이 지날수록 누적돼 정확도가 점차 떨어진다. OCV 방식도 추가 장비는 필요 없으나, 전압이 안정될 때까지 상당한 휴지 시간을 필요로 하고 SOC-OCV 관계 자체가 온도와 열화 정도에 따라 달라져 실시간 적용에는 한계가 있다.

EIS는 정보량이 많아 열화 기전까지 구분해낼 수 있다는 장점이 있지만, 전통적으로는 넓은 주파수 대역을 정밀하게 스윕할 수 있는 전용 임피던스 분석 장비가 필요해 비용과 측정 시간 부담이 있었다. 다만 최근에는 BMS의 기존 전류·전압 파형을 활용해 별도 장비 없이 임피던스에 준하는 정보를 얻으려는 연구도 진행 중이다. ICA·DVA는 완전 충방전이 아니라 10~20분 수준의 부분 충전 구간 데이터만으로도 추정이 가능하다는 점에서 상대적으로 빠르며, 실험실 조건에서는 평균절대오차가 1% 안팎으로 보고된다.

모델 기반 방식은 온라인 추정에 적합해 소요 시간 부담이 적지만, 등가회로모델과 칼만필터를 결합한 연구에서 보고되는 오차는 DST(Dynamic Stress Test)와 FUDS(Federal Urban Driving Schedule) 같은 표준화된 동적 부하 프로파일로 실험실에서 신품 또는 초기 열화 셀을 시험한 조건에서 1~2% 수준이다. 데이터 기반 방식의 정확도 역시 대체로 실험실에서 순환 열화시킨 셀의 사이클 데이터를 학습·검증한 결과다.

## 사용후 배터리 현장에서 부딪히는 한계

여기서 짚어야 할 지점은, 위에서 인용한 정확도 수치 대부분이 단일 화학종·단일 이력의 신품 셀을 실험실에서 통제된 조건으로 순환 열화시킨 뒤 측정한 값이라는 사실이다. 사용후 배터리 현장은 이 조건과 거리가 있다.

첫째, 이력이 균일하지 않다. 실험실 셀은 열화 경로가 알려진 상태에서 출발하지만, 탈거된 사용후 배터리는 차량마다 주행 패턴과 정비·사고 이력이 달라 같은 모델이라도 열화 상태가 제각각이다. 모델 기반 방식이 전제하는 파라미터도, 데이터 기반 방식이 학습한 패턴도 애초에 이런 이질적인 이력을 대표하도록 만들어지지 않았다. 최근 연구들은 이 문제를 화학종과 SOC, SOH에 대한 사전 정보가 전혀 없는 "미지의(unknown)" 배터리를 얼마나 빠르게 선별할 수 있는지의 문제로 재정의하며 접근하고 있는데, 이는 거꾸로 기존 방식들이 이력을 안다는 전제 위에서 설계됐다는 뜻이기도 하다.

둘째, 팩 단위와 셀 단위의 측정은 다른 문제다. 학계 리뷰에 따르면 셀 단위 추정에서 보고되는 오차가 대체로 낮은 편인 데 비해, 팩 단위로 넘어가면 오차 폭이 더 벌어지는 경향이 나타난다. 원인은 두 가지로 정리된다. 하나는 직병렬로 묶인 셀들 사이의 편차(전류·전압·온도 불균형)가 팩 전체의 SOH 산출에 불확실성을 더한다는 점이고, 다른 하나는 팩의 회로 구성이 복잡해질수록 전기화학모델 기반 접근이 더는 유효하게 적용되기 어려워, 결국 데이터 기반 방식에 의존할 수밖에 없다는 점이다. 그런데 사용후 배터리는 대부분 팩이나 모듈 단위로 탈거되어 들어오고, 그 팩을 셀 단위로 다시 분해해 개별 시험하는 데는 추가 공정과 시간이 든다.

셋째, 시간과 비용 제약이 정확도와 정면으로 충돌한다. 가장 신뢰도 높은 완전방전 용량시험은 사용후 배터리 한 팩을 처리하는 데도 여러 시간이 걸린다. 사용후 배터리가 대량으로 발생해 짧은 시간 안에 등급을 매겨 분류해야 하는 현장에서는 이 방식을 모든 개체에 적용하기 어렵다. 그래서 부분 충전 구간이나 임피던스처럼 짧은 시간에 얻을 수 있는 신호로 추정하는 방식에 관심이 쏠리지만, 이런 방식의 정확도가 신품 셀 실험실 조건에서 보고된 수준을 이력이 제각각인 사용후 팩에서도 그대로 유지하는지는 별개의 검증이 필요한 문제로 남는다.

## ARC의 관찰

지금까지 나온 SOH 추정 연구 대부분은 통제된 실험실 조건에서 신품 셀을 대상으로 정확도를 입증해왔고, 이력이 알려지지 않은 사용후 팩을 짧은 시간 안에 선별해야 하는 문제는 비교적 최근에야 별도 연구 주제로 다뤄지기 시작했다. 탈거 전 성능평가 제도가 재제조·재사용·재활용 등급을 성능평가 결과로 가르는 구조를 택한 이상, 그 등급 판정에 어떤 SOH 추정 방식을 어떤 조건에서 요구할지가 실무 진입 가능성을 좌우하는 지점이 될 것으로 보인다. 특히 오차 폭이 넓어지는 팩 단위 판정을 그대로 신뢰할지, 아니면 셀 단위 재시험을 요구할지는 정확도와 처리 시간·비용 사이에서 어느 쪽에 무게를 둘 것인지의 정책적 선택이기도 하다.

참고: [ISO] "ISO 12405-4:2018, Electrically propelled road vehicles — Test specification for lithium-ion traction battery packs and systems — Part 4" (https://www.iso.org/standard/71407.html)

참고: [SAE International] "J1798_201911, Recommended Practice for Performance Rating of Electric Vehicle Battery Modules" (https://saemobilus.sae.org/standards/j1798_201911-recommended-practice-performance-rating-electric-vehicle-battery-modules)

참고: [Battery Design] "State of Health (SOH)" (https://www.batterydesign.net/battery-management-system/state-of-health/)

참고: [ScienceDirect, Applied Energy] "Enhanced Coulomb counting method for estimating state-of-charge and state-of-health of lithium-ion batteries" (https://www.sciencedirect.com/science/article/pii/S0306261908003061)

참고: [ScienceDirect] "A comparative study of curve determination methods for incremental capacity analysis and state of health estimation of lithium-ion battery" (https://www.sciencedirect.com/science/article/abs/pii/S2352152X19317219)

참고: [MDPI, Energies] "Joint State-of-Charge and State-of-Health Estimation Method Based on Equivalent Circuit Model and Data-Driven Model Fusion" (https://doi.org/10.3390/en19061567)

참고: [IET, Energy Conversion and Economics] "State‐of‐health estimation of lithium‐ion batteries: A comprehensive literature review from cell to pack levels" (https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/enc2.12125)

참고: [ScienceDirect] "Fast state of health estimation of unknown lithium-ion batteries for second-life and recycling assessment" (https://www.sciencedirect.com/science/article/abs/pii/S0378775326009146)

참고: [arXiv] "Experimental Methods, Health Indicators, and Diagnostic Strategies for Retired Lithium-ion Batteries: A Comprehensive Review" (https://arxiv.org/abs/2512.01294)
