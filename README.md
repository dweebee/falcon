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
- conversion method: text to {context/evidence, claim}, label to {claim and label}
- example:
 (json sample) into then converted data sample***

# Reference
  ### “Automated Fact-Checking in Dialogue: Are Specialized Models Needed?” Chamoun et al., EMNLP 2023 워크숍 논문
  Chamoun은 retrieval 방식만 수정
  <인용이유> 이 논문의 저자들도 지시대명사 참조문제 해결이 팩트체킹 성능향상에 영향을 미친다고 주장. 그리고, dialogue와 corpus 사이를 변환하며 실험. 즉, 대화라도 fever기반 모델로 성능체크 가능하다고 주장. 이 내용으로 인해 내가 ecthr데이터의 text를 대화의 context이자 evidence로 써도 무방할까? 아니면, text자체를 긴 evidence로 보고 context는 이전 대화인데, 이전 대화는 없다고 보고 실험해야할까?

  #### FactGraph: Evaluating Factuality in Summarization with Semantic Graph Representations
  
