# FACT-KG(2023)

핵심은 두 가지. 1)KG evidence, 2)FactKG dataset, Recon model

- 기존 텍스트 기반 팩트 검증(Fact Verification) 방식은 **claim과 evidence 문장 간의 의미적 일치 여부**를 평가함. 하지만 이 논문은 **evidence로 일반 텍스트가 아닌 지식 그래프(Knowledge Graph, KG)** 를 사용.
- 또한 주장을 검증하기 위한 **추론 경로(reasoning path)** 를 **명시적으로 제공**하고, **그래프 구조로 시각화**할 수 있어 **설명 가능한 추론(explainable reasoning)** 이 가능.
- 위 두 가지 핵심을 실현하기 위해 다음 두 가지를 제안함!
  - **FACT-KG 데이터셋**: Wikidata 기반으로 구축된 KG 기반 팩트 검증 벤치마크. 자연어 claim과 함께 정답 레이블 및 KG 기반 reasoning path 제공.
  - **ReCon 모델**: KG 상에서 claim에 부합하는 reasoning path를 탐색하고, 이를 기반으로 참/거짓을 예측하는 GNN 기반 모델.

### FACT-KG 데이터셋 구성

- **기반**: Wikidata Knowledge Graph
- **목적**: claim에 대한 정답 레이블(True / False)을 **텍스트 없이도 KG 정보만으로 판단** 가능하도록 구성
- **각 샘플(Claim)의 구성 요소**:
  - `claim`: 자연어 문장 (예: "Obama was born in Hawaii.")
  - `label`: 참(True) 또는 거짓(False)
  - `reasoning_paths`: claim을 지지하거나 반박하기 위한 KG 내의 triple 기반 추론 경로들 (triple들의 순서열)
  - `triples`: claim과 관련된 KG의 부분 그래프. reasoning path와는 별도로 주변 triple까지 포함
  - `entities`: claim 내 명사구 또는 고유명사를 **Wikidata entity linking**을 통해 추출한 주체/객체
  - `relations`: reasoning path에서 사용된 relation (predicate)들의 집합 "엣지"

- **데이터셋 split 비율**:
  - `train.json`: 약 70%
  - `valid.json`: 약 10%
  - `test.json`: 약 20%
  - 모든 split은 동일한 샘플 구조를 따름

### ReCon 모델? (Reasoning over Connections)

- **입력**:
  - 자연어 claim
  - claim과 관련된 KG 부분 그래프 (triples 및 해당 entities)

- **처리 단계**:
  1. **Claim 인코딩**:
     - Claim은 BERT 등 pre-trained LM을 통해 임베딩되고, KG의 노드 및 관계도 별도의 임베딩 공간에 매핑됨
     - 이후 claim 임베딩과 KG 엔티티 간의 의미적 유사도를 기반으로 KG 내 관련 노드를 매핑

  2. **Graph Reasoning**:
     - 선택된 KG 내 시드 노드들로부터 GNN을 통해 **의미 있는 추론 경로들**을 탐색
     - 단순 인접 노드가 아닌 **멀티홉 reasoning path** 단위로 탐색

  3. **경로 scoring 및 선택**:
     - 여러 후보 경로들 중에서 claim과 의미적으로 가장 일치하는 경로를 선택
     - attention 또는 path-level scoring 기법 사용

  4. **최종 예측**:
     - 선택된 경로를 기반으로 claim이 KG 내 사실과 일치하는지 여부(True / False)를 판별

- **모델 특징**:
  - 단순 노드 분류가 아닌, **경로 기반(path-based)** 추론 수행
  - 추론 과정 전체가 **설명 가능**하며 reasoning path를 그대로 추출/시각화 가능
  - KG의 **구조적 정보** + claim의 **언어적 정보**를 모두 반영한 통합적 추론 가능
