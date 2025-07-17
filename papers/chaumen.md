# Automated FC in dialogue: Are specialized models needed? 

**핵심 기여**
  - 기존의 standalone 팩트체킹 모델은 대화 속 발언(claim)에 취약함을 확인.
  - 대화 데이터로 fine‑tuning 시 standalone 모델 성능 저하(catatrophic forgetting) 문제 발견.
  - retrieval adaptation 및 conversational input transformation 기술을 제안하여, 하나의 모델로 standalone + dialogue 환경을 동시에 대응. "이게 저자들이 주장하는 핵심.'
  - 제안된 방법을 적용한 모델이 dialogue 벤치마크(DialFact)에서 SOTA 수준 성능 달성하면서, standalone 벤치마크(FEVER) 성능도 유지됨.

- **제안된 데이터셋**
  - 논문 자체에서는 새로운 데이터셋을 만들지 않고,
  -  **DialFact** (대화 context 포함된 검증용 claim 22,245개)와 **FEVER** (독립된 claim 검증 데이터셋)를 사용 

- **제안된 모델 / 작동 원리**
  - 기존 fact‑checking 모델 (예: FEVER 학습된 모델 + VitC 강화) 유지하며, 아래 추가 처리:
    1. **Claim detection**: 대화에서 실제 검증이 필요한 문장만 추출.
    2. **Document retrieval**: claim 중심의 검색 점수 + 대화 context 점수를 조합하여 관련 문서 재탐색.
    3. **Sentence retrieval**: 문서 유사도 뿐만 아니라 문서-문장 relevance 고려.
    4. 이후 해당 evidence와 함께 기존 모델 입력 → support/refute 결정.
  - 이렇게 입력 전처리 및 retrieval 세부 조정을 통해 dialogue 특히 coreference 환경에서도 standalone 모델이 높은 성능 유지.

- **결과 요약**
  - standalone 모델에 제안된 기술 추가 시:
    - DialFact 정확도: SOTA dialogue‑specialized 모델과 유사 (±3% 이내 격차)
    - FEVER 정확도: dialogue fine‑tuned 모델 대비 12%p 이상 높은 성능 유지
  - dialogue fine‑tuned 모델은 FEVER에서 성능 급락(catatrophic forgetting)함을 실험적으로 증명.