# falcon
falcon project for 2025 NLLP

---
# checklist
### SOTA 케이스 조사
[] LexGLUE ECtHR Task A로 사실검증한 논문이 최근 5년(2020~2025) 내  있는지? </br>
[] 최근 연구 중, 

### LexGLUE ECtHR Task A 데이터 이해
[] 레이블 정보 부록에 추가: (1) 가능한 레이블(위반 조항번호) 범위 10개의 정의; (2) 판사의 판결을 위한 요건사실 정리
[] 각 샘플의 경우의 수: (1) 레이블 1개(위반한 조항이 딱 하나!); (2) 레이블 2개; (3) 레이블 빈 리스트(: 이는 

### 관련 모델 이해: LegalBERT, Llama3

### 전처리
[] LexGLUE 데이터를 대화 내 주장검증용 NLI용으로 데이터 변환: {text, label} to {context, claim, label}
[] Supported에 해당하는 claim 후보 다섯 문장 선정 (전처리할 때, 랜덤함수로 5개중 하나로 변환) 
[] Refuted, NEI 생성 방법 정의필요
- Refuted는 증거 텍스트가 해당 주장을 명시적으로 반박하는 경우입니다. 즉, 주장과 상충되는 내용이 직접적으로 존재해야 합니다.
- NEI는 텍스트 내에 그 주장을 입증할 수도, 반박할 수도 있는 정보가 전혀 없는 경우입니다. 즉, 텍스트가 침묵하거나 정보가 불충분한 상태인 경우입니다.
- NotEnoughInfo는 위키피디아에서 해당 주장을 뒷받침하거나 반박할 수 있는 정보가 전혀 없는 경우로 사용된다.(FEVER,2018)
[] 


---
# Timeline
W1. ACL 논문구조 뼈대잡기, 관련 연구정리, 연구 질문 확정, 모델과 데이터 선정, 실험 디자인 초안 설계 ~7.19
	- RQ1: 법률적 추론 구조에 기반하여 판결문의 문단들을 클러스터링하고, 이 중 주장과 밀접한 핵심 문단만을 선별하여 입력할 경우, 문서 전체를 사용할 때보다 팩트체크(주장 검증) 성능이 향상되는가?
W2. 실험3개 진행, 실험 로그 및 시각화, introduction & related work 초안 ~7.25

W3. Ablation & 추가실험, Results & Analysis, Method(성능비교, 그래프 등) ~8.1

W4. Abstract, Conclusion, Reference정리 ~8.8

# data transformation
- dataset: lexglue-icthr task a
- property: text, label
- 	how to make text into dialogue?
	- conversion method: text to {context/evidence, claim}, label to {claim and label}
		- example:
 			(json sample) into then converted data sample***
			- text 값을 단순히 대화로 바꾸는 게 '대화 속 주장의 팩트체크 검증 성능향상' 입증을 위한 증명으로는 미약하지않을까....?
	- turn level conversation 형태

### LexGLUE icthr task a 데이터 후속연구 조사
1. 긴 법률문서 처리 한계 -> text가 너무 김.
2. 텍스트 내 핵심정보 식별 어려움 -> claim verification에 핵심적인 문맥 식별 필요함.
3. 특수 도메인 언어 및 지식 격차
4. 벤치마크의 언어적 제약 (국가별 법규 차이 존재, 다양한 법에 시도해 알고리즘의 기능 검증필요)

문맥 전처리/요약 기법은 1,2번 해결 기대. 이 요약기법이 실제 팩트체킹 성능을 향상시키는지 검증 필요하고, 요약의 최적 방식을 탐색하는 연구 진행필요. 

# 실험 계획
- 일단 총 다섯 단계: 문단 임베딩 → 클러스터링 → claim 유사도 기반 클러스터 선택 → 클러스터 내 상위 문단 3개 선택 → NLI 입력 구성

1. **전체 문맥 사용 Baseline**: 케이스의 모든 문단을 한 번에 입력하는 모델 (llama or BERT-based model)
2. **문단 선별 기법**: 문단 임베딩 클러스터링 → 주장 관련 문단만 선택하여 NLI 판별
3. **모델 선택**: LegalBERT 등 도메인 특화 모델 vs. LLM (예: Llama2) 비교
4. **입력 구성 비교**: {대화 문맥+증거+주장} vs {문맥+주장} vs {증거+주장} (DialFact 설정)
5. **평가지표**: (정확도, 매크로/마이크로 F1 등 )NLI 분류 성능 전반 평가
6. **최종 목표**: 장문 맥락에서 핵심 근거 추출이 주장 검증 향상 (법률 도메인에서의 새로운 시도에 포커싱.)

# Structure 
- 목표: 대화 문맥 중 주장 검증(즉, 법적 판단)에 핵심이 되는 정보(문맥)만 선별하여 주장검증 성능 분석
- 문맥 필터링 방식: 법률적 추론 과정에 기반한 클러스터링
- 적용 도메인: 법률 대화 도메인(법적 사실 문단들로 구성)
- 문맥 구조:대화형 문맥
- 주장 검증 방식: 판결에 필요한 선별된 문맥을 구성해 claim 검증
- 연구 초점:"법률적 추론기반 문맥 선별을 통해 더 효과적인 주장검증 가능여부"확인

# 연구 기여점
1. 도메인 차별성: 일반 도메인이 아닌 법률 도메인, 특히 법률 대화체 기반의 주장검증  실험
2. 문맥 구조 차별성: 판사처럼 절차적 추론 흐름의 구조를 반영해 판결에 도움이 되는 문맥 선별
3. 문맥 선별 방식 차별성: Throne의 모델 기반 증거선택이 아닌, **법적 추론 과정에 기반한 정보 선별방식**

### 데이터 특징(이 데이터로 판사의 판단흐름에 따라 분류가능한 이유)
이 데이터는 사실관계-주장-판단이 시간순/논리순으로 서술된 구조.

### 판사의 추론 구조란?
실제 유럽인권재판소나 한국법원의 판결문은 보통 다음과 같은 절차적 구조를 따른다.
1. 사건의 배경 설명(사실관계)
2. 당사자의 주장 정리
3. 법적 쟁점 제시
4. 사실판단
5. 법적 평가(적용 규정 언급)
6. 판단

따라서, 데이터 내 전체 문맥을 {사건개요, 주장요지(쟁점정리), 법적평가및판단}으로 나눔.




# Reference
  ### “Automated Fact-Checking in Dialogue: Are Specialized Models Needed?” Chamoun et al., EMNLP 2023 워크숍 논문
  Chamoun은 retrieval 방식만 수정
  <인용이유> 이 논문의 저자들도 지시대명사 참조문제 해결이 팩트체킹 성능향상에 영향을 미친다고 주장. 그리고, dialogue와 corpus 사이를 변환하며 실험. 즉, 대화라도 fever기반 모델로 성능체크 가능하다고 주장. 이 내용으로 인해 내가 ecthr데이터의 text를 대화의 context이자 evidence로 써도 무방할까? 아니면, text자체를 긴 evidence로 보고 context는 이전 대화인데, 이전 대화는 없다고 보고 실험해야할까?

  #### FactGraph: Evaluating Factuality in Summarization with Semantic Graph Representations
  
