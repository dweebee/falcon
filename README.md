# falcon
falcon project for 2025 NLLP

# Timeline
W1. ACL 논문구조 뼈대잡기, 관련 연구정리, 연구 질문 확정, 모델과 데이터 선정, 실험 디자인 초안 설계 ~7.19

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

# Reference
  ### “Automated Fact-Checking in Dialogue: Are Specialized Models Needed?” Chamoun et al., EMNLP 2023 워크숍 논문
  Chamoun은 retrieval 방식만 수정
  <인용이유> 이 논문의 저자들도 지시대명사 참조문제 해결이 팩트체킹 성능향상에 영향을 미친다고 주장. 그리고, dialogue와 corpus 사이를 변환하며 실험. 즉, 대화라도 fever기반 모델로 성능체크 가능하다고 주장. 이 내용으로 인해 내가 ecthr데이터의 text를 대화의 context이자 evidence로 써도 무방할까? 아니면, text자체를 긴 evidence로 보고 context는 이전 대화인데, 이전 대화는 없다고 보고 실험해야할까?

  #### FactGraph: Evaluating Factuality in Summarization with Semantic Graph Representations
  
