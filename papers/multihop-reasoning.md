- Test1. 'First hopping': they test if changing the prompt to indirectly mention the bridge entity instead of any other mention the bridge entity instead of any other entity increases the LLM's internal recall of the bridge entity.
	- 테스트 지표: entity recall score
		- (모델이 스스로 잠재적으로 연결 엔티티를 떠올리는 능력)
- Test2. '2nd hopping' : they test if increasing this recall causes the LLM to better utilize what it knows about the bridge entity.
	- 테스트 지표: consistency score btwn the distributions form completions of the two-hop prompt and an equivalent recall-based one-hop prompt
		- (두 단계 프롬프트(“Superstition의 가수의 어머니는?”)와 그에 대응하는 한 단계 프롬프트(“Stevie Wonder의 어머니는?”) 간에 모델이 생성한 답의 분포가 얼마나 서로 유사한지 나타내는 지표)
[인용할만한 내용]
- They find strong evidence of latent multi-hop reasoning for the prompts of certain relation types, with the reasoning pathway used in more than 80% of the prompts. However, the utilization is highly contextual, varying across different types of prompts.
- They find a clear scaling trend with increasin gmodel size for the first hop of reasoning but not for the second hop.

- (Vaswani et al., 2017) 트랜스포머모델은 프롬프트를 완수하기위해 파라미터내 저장된 factual information을 검색하고 저장한다.
- (Wei et al, 2022b) 필수정보가 입력(문맥)에 명시적으로 제공될 때, 뛰어난 맥락 내 추론 능력을 갖는다. 

- 모델이 다단계 추론능력(multi-hopping)을 갖추면, 지시대명사 참조문제도 자연스럽게 해결할 수 있다. (저자의 주장에 대한 나의 의견)

[주요 개념]
- activation patching: 활성화함수 출력값인 모델 내 은닉벡터의 '잘못된 값'을 '구멍'이라고 생각해, 개입해서 이 구멍을 메꾸는(값 수정) 것.
- 최종 예측이 잘못되면, 은닉벡터에 구멍(패칭)이 있다고 판단해 '개입'해서 활성화 출력값의 일부(구멍)를 수정하는 것.