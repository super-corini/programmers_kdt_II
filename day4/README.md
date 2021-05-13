# Day 4 - EDA

2. Kaggle에서 Dataset을 찾고, 이 Dataset에서 유의미한 Feature를 3개 이상 찾고 이를 시각화해봅시다.
데이터를 뽑아봅시다.
데이터에 대한 가설을 세워봅시다.
가설을 검증하기 위한 증거를 찾아봅시다.


## 내가 선택한 데이터셋


[Kaggle hotle booking demand dataset] https://www.kaggle.com/jessemostipak/hotel-booking-demand

- 관광지의 호텔 중 하나인 호텔 H1과 도심의 호텔 중 하나인 호텔 H2의  2015년 7월 ~ 2017년 8월의 예약 정보 약 119000건을 총 31개의 변수 구조로 데이터화 한 것.

- 호텔을 예약 후 취소한 것을 boolean으로 나타낸 'is_canceled' feature를 y feature로 두고, 취소율과 관련있을 것 같은 feature들을 살펴보았습니다.

1. hotel
본 dataset에 포함된 hotel은 city hotel과 resort hotel 두 곳으로 이름 그대로 호텔이 위치한 지역을 의미합니다. 지역에 따른 취소율 차이가 있는지 궁금합니다.

2. time of year
여행업계는 시기에 매우 민감하여, '비수기', '성수기'라는 말이 있습니다. 호텔 예약 건수와, 취소율에도 이와 같은 시기의 차이가 있는지 궁금합니다.

3. lead time
리드 타임이란 예약일와 숙박일 사이의 기간을 의마하는 여행업계 용어 입니다.
미리 예약을 한 사람과 임박해서 예약을 한 사람 사이에 취소율 차이가 있을까요?

 