"모든 문맥 정보가 주장 검증에 항상 도움이 될까?"라는 질문에는 James Thorne 도 그렇고 많은 연구자들이 "해로운 문맥의 일부를 찾아 제거하면 주장검증에 더 도움이 된다."
고 밝혀왔다. 하지만, 법적 도메인에서 "모든 사실정보가 판결에 도움이 될까?"라는 질문에 대해 진행된 연구는 아직 없다. 
이에, ECtHR Task A dataset 데이터를 이용해 선별된 사실정보가 판결에 더 도움이 된다는 것을 증명하고자 한다.
이 데이터는 '주어진 판결문 요약'(test)를 통해서 '특정 조항 위반 여부'를 판단하는 태스크이다.
우리는 이 데이터를 '대화 속 주장 검증'의 실험을 위해 2-turn base conversation으로 변환한다. 이 때, 원래의 label로부터 두 개의 claim과 label 쌍이 나온다.
예를 들어, label이 [3,8]이면 3번 조항과 8번 조항을 위반했다는 의미인데, 이를 통해 우리는 "the applicant violated the article 3 and 8."라는 claim과 label은 "supported"를 생성했다.
그리고 추가적으로 "the applicant violated the article 1,8." 라는 주장을 만들어 "refuted"라는 label을 갖는 샘플도 추가 생성했다.
즉, 하나의 샘플로 label이 supported인 추가 샘플 하나와 refuted인 또 다른 샘플, 총 2개의 샘플을 생성한다.
레이블이 비어있는 약 10%(학습데이터 9k 중에서 941개)의 데이터는 label이 비어있다. 이는 applicant가 어떤 조항도 위반하지 않음을 의미하는데, 
이 샘플로부터는 "the applicant violated the law."라는 주장과 "NEI(Not Enough Information)"이란 레이블을 갖는 샘플이 생성된다.

우리는 위의 방식으로 변환된 데이터를 기반으로 legalbert, llama3, colloquialbert 를 테스트해 비교한다.
	