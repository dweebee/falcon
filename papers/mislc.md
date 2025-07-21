Misinformation with Legal Consequences (MisLC): A New Task Towards Harnessing Societal Harm of Misinformation

- NLLP 2024 채택 논문.
- factchecking verfication 보다는 detection.
- 전문가들과 데이터 생성
- 팩트체크 뿐만 아니라, 법적 문제되는지 여부까지 분류하는 모델 제안.
- https://github.com/chufeiluo/mislc

### Misinformation with Legal Consequences: 법적 결과를 초래할 수 있는 허위정보
-   단순히 틀린 주장이 아니라, 법적 처벌이나 분쟁으로 이어질 수 있는 허위 주장
-   "이 약은 암을 치료할 수 있어요!" → 단순 거짓이 아니라 소비자 보호법 위반 가능성

### MisLC: 그런 '법적 위험성이 있는 misinformation'을 따로 탐지하는 새로운 태스크

### 기존연구: 현재의 misinformation detection benchmark들은 해악의 정도를 구분하지 않는다
-   지금까지의 fact-checking 시스템은 이게 참이냐 거짓이냐만 판단하지, 그 거짓말이 얼마나 해로운지, 특히 법적으로 심각한 영향을 미칠 수 있는지는 전혀 고려하지 않음!!!
-   “지구는 평평하다” → 거짓이지만 실제 사회적 해악은 작음
-   “백신은 불임을 유발한다” → 거짓이고, 사회적/법적 해악 큼!!!

### MisLC detection
- 입력: 어떤 주장 (예: 뉴스 속 발언, 인용, 트윗 등)
- 출력: 이 주장이 법적으로 문제될 소지가 있는 misinformation인지 여부
- 기존 모델들은 “이 말이 진짜야?”만 잘 판단해요. 그런데 “이 말이 법적으로 문제될 거짓말이야?”는 판단을 잘 못함!!!
- 그냥 문장만 보는 대신, 모델한테 추가 정보를 같이 줘보자.

그 추가 정보란 게 바로:

✅ 1. Sociolegal 정보:

예: "이 말은 인종차별적인가?", "이건 명예훼손일 수 있나?", "공공안전에 해를 주나?"

사회적/법적 맥락.

✅ 2. Precedent (판례):

예: “과거에 이런 주장을 했다가 고소당한 경우가 있었는가?”

실제 법원에서 판결된 유사한 사례를 참고하게 함.

### 새로운 데이터셋 제공
- 실제 인도 팩트체크 웹사이트에서 1,500개의 주장 수집
- 법률 전문가가 각 주장에 대해 MisLC 여부를 주석 → Ground truth 생성
- 기존 모델과 다르게, 다음을 추가로 사용함
-   sociolegal features: 사회적/법적 배경 정보
-   precedent retrieval: 과거 유사한 사례(판례) 검색하여 입력에 추가

### 모델 구조
- MisLC 모델 구조: "법을 아는 팩트체커"
- 기본 입력: 주장 문장

예: “이 약을 먹으면 암이 완치됩니다”

모델은 이 문장이 진짜인지, 그리고 법적으로 문제가 될 수 있는지 판단

{claim + sociolegal + precedent } ===== > RoBERTa =======> 결합된 표현 =======> 분류기 ========> 이 주장이 법적으로 위험한 misinformation 인지 분류! 

### 실험 과정
- 실험1: 기본 roberta는 문장만 보고 판단
- 실험2: sociolegal 추가하니 성능 소폭 개선
- 실험3: precedent까지 모두 추가하니 성능 상당히 개선! 


### 실험결과
- 
