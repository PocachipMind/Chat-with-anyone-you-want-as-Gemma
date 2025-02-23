# Chat-with-anyone-you-want-as-Gemma
Google Machine Learning Bootcamp를 진행하며 제작한 Gemma 활용 프로젝트.

프롬포트를 통한 아바타 대화, 파인튜닝 모델과 대화 두가지 기능 구현

- Project 폴더 : 실행하기 위한 파일들 수록
- Train 폴더 : 파인튜닝하기 위한 코드, 자료 수록


## 시연 이미지

![image](https://github.com/user-attachments/assets/907f4c10-7f5c-4802-841a-9bfb0d3080fb)


![image](https://github.com/user-attachments/assets/8c4ac68a-f2ed-4ff3-bfa5-d9c7808b5757)


![image](https://github.com/user-attachments/assets/aa0b8200-7c34-42d0-8a7f-0b33088dea7c)


 ## 시연 영상

1. 직접 입력 대화

https://github.com/user-attachments/assets/38e8a3e5-ceed-47dc-b44e-5adeedaf180b

2. 파인 튜닝된 모델 대화

https://github.com/user-attachments/assets/858678eb-041e-4988-a088-3cad6e10c3fc


## 핵심 로직

### 1. 프롬포팅 아바타
![image](https://github.com/user-attachments/assets/c89cd838-774c-45a1-9545-3aa84986d9d7)
![image](https://github.com/user-attachments/assets/5e1b5aab-44fc-4d11-8fca-1dc1f3f0c2b4)

위 이미지와 같이 system을 통해 페르소나를 주고 대화에 임하도록 구현

### 2. 파인 튜닝 아바타

![image](https://github.com/user-attachments/assets/aa17103c-dfb0-4f41-b596-1a203ddb7cfa)

모델을 학습 후 허깅페이스에 올려서 사용.

학습 코드 및 데이터는 Train폴더 안에 기재되어있음.


## 제작 이슈

Gemma 2 의 경우 System role이 존재하지 않았는데, 이를 적용하기 위해 프롬포트 자체에 System role 을 적용. ( chat mod로는 되지 않음 )

![image](https://github.com/user-attachments/assets/d6f70f9f-ae9f-42b9-a77a-cec0de3916ef)

참고 : https://huggingface.co/google/gemma-2-9b-it/discussions/15
