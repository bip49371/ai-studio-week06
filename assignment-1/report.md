제품 원래 색상이 이게 맞나요? 색상이 잘못 나온 거라면 교환이 가능한지도 궁금합니다. - 제품문의 / 2 (애매)

제품의 색상이 궁금합니다. - 제품문의 / 1

잘못된 곳에 배송이 간 것 같습니다. 배송이 완료되었다고 뜨는데 도착하지 않았습니다. - 배송 / 3

비밀번호 변경하고 싶어요. - 기타 / 1

배송이 안오는데 언제오나요? 3일 안에 안올 거 같으면 환불해주세요. - 배송 / 2 (애매)



1. Zero-shot
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)


2. Few-shot
![alt text](image-3.png)
![alt text](image-4.png)
![alt text](image-5.png)

3. CoT
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)

___
애매한 사례 1건을 버전별로 반복 실행하여 출력의 흔들림을 관찰하였다. 

1. Zero-shot
![alt text](image-13.png)
![alt text](image-15.png)
![alt text](image-16.png)

2. Few-shot
![alt text](image-20.png)
![alt text](image-21.png)
![alt text](image-22.png)


3. CoT
![alt text](image-17.png)
![alt text](image-18.png)
![alt text](image-19.png)

___

|    질문   |      1     |      2     |    3   |    4   |    5   |    5   |    5    |    5   |
|:---------:|:----------:|:----------:|:------:|:------:|:------:|:------:|:-------:|:------:|
|           | 제품문의 2 | 제품문의 1 | 배송 3 | 기타 1 | 배송 2 |        |         |        |
| zero shot | 제품문의 2 | 제품문의 1 | 배송 3 | 기타 1 | 배송 2 | 배송 2 |  배송 2 | 배송 2 |
|  few shot | 제품문의 2 | 제품문의 1 | 배송 3 | 기타 1 | 환불 3 | 배송 3 |  배송 3 | 배송 3 |
|    CoT    | 제품문의 3 | 제품문의 3 | 배송 1 | 기타 3 | 배송 2 | 배송 2 | 배송 2  | 배송 2 |


표의 결과를 분석한 결과, zero shot 버전이 가장 정답률이 높았다. few-shot 버전은 애매한 문의에 대해서 일관적이지 못한 응답을 출력한 점, CoT의 응답은 긴급도의 높은 정도가 반전되어 출력된 점이 눈에 띄었다.

현재 문의를 분석하는 모델의 경우 가장 높은 정답률을 보인 zero shot 버전을 사용하는 것이 가장 적절하다. 그러나 실제 캡스톤에 사용하는 것은 고객 문의가 아니며, 적은 데이터만을 사용했기 때문에 더 많고 다양한 데이터를 사용하면서 모델을 개선하는 것이 좋다. 