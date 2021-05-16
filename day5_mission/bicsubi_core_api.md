# Mission 1
![image](https://user-images.githubusercontent.com/59414764/118406448-23279880-b6b7-11eb-96fc-7e7fc170b675.png). 

1. '/whoami' [GET] 을 통해 github id를 json형태로 반환받습니다.  
<img width="1235" alt="스크린샷 2021-05-17 오전 1 05 02" src="https://user-images.githubusercontent.com/59414764/118406065-c24b9080-b6b5-11eb-8049-a54a8d005ee5.png">  

2. '/echo/<하고싶은string>' [GET] 을 통해 주소로 입력받은 string을 반환받습니다.  
<img width="1235" alt="스크린샷 2021-05-17 오전 1 05 16" src="https://user-images.githubusercontent.com/59414764/118406108-f45cf280-b6b5-11eb-9dfe-7c871b995555.png">  

## Weapon. 

1. '/weapon' [POST] 을 통해 json을 입력으로 받아, 새로운 무기를 생성합니다. 기존에 있는 무기 이름일 경우, 해당 무기의 수량이 증가합니다.  
<img width="1235" alt="스크린샷 2021-05-17 오전 1 05 31" src="https://user-images.githubusercontent.com/59414764/118406270-49006d80-b6b6-11eb-9ac9-36733dc9effa.png">  

2. '/weapon' [GET] 을 통해 현재 가지고 있는 무기 이름, 수량을 반환받습니다.  
<img width="1235" alt="스크린샷 2021-05-17 오전 1 06 01" src="https://user-images.githubusercontent.com/59414764/118406294-68979600-b6b6-11eb-9e87-712bdf99357c.png">  

3. '/weapon/<int:index>' [PUT] 을 통해 json을 입력 받아, 해당 index의 무기의 이름, 수량을 바꿉니다.  
<img width="1235" alt="스크린샷 2021-05-17 오전 1 06 14" src="https://user-images.githubusercontent.com/59414764/118406391-dc39a300-b6b6-11eb-9ef4-c7c130a93759.png">  

4. '/weapon' [DELETE] 을 통해 json을 입력 받아, 해당 이름의 무기를 목록에서 지웁니다.  
<img width="1235" alt="스크린샷 2021-05-17 오전 1 06 23" src="https://user-images.githubusercontent.com/59414764/118406425-01c6ac80-b6b7-11eb-948c-9f67bab596b4.png">  
