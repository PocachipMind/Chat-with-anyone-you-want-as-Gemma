# Chat-with-anyone-you-want-as-Gemma
Google Machine Learning Bootcamp를 진행하며 제작한 Gemma 활용 프로젝트.

## 시연 이미지

![image](https://github.com/user-attachments/assets/907f4c10-7f5c-4802-841a-9bfb0d3080fb)


![image](https://github.com/user-attachments/assets/b1073421-084f-418e-b7b4-88341f05009a)


![image](https://github.com/user-attachments/assets/2f2afdeb-2118-46ad-ba12-029244d3999c)

 ## 시연 영상

1. Example 사용

https://github.com/user-attachments/assets/38e8a3e5-ceed-47dc-b44e-5adeedaf180b

2. 직접 입력

https://github.com/user-attachments/assets/327206e2-bd84-477c-8564-b7d4b1b92dc1

## 사용법

![image](https://github.com/user-attachments/assets/f0574948-13aa-4dda-a500-6409e87165fc)

Bot Name : 대화 할 상대의 이름을 입력하세요.

Bot Gender : 대화 할 봇의 성별을 고르세요.

Bot Profession : 봇의 직업을 적으세요.

Bot Personality : 봇의 성격을 형용사 형식으로 적으세요.


![image](https://github.com/user-attachments/assets/e17e5874-5b85-41ca-a8ae-49a82b067780)

Make Bot Profile 탭을 누르면 위와 같이 봇 프로필을 제작할 수 있습니다. 

봇의 프로필 사진, 배경 사진, 상태 메세지를 설정할 수 있으며 이는 필수는 아닙니다.

만약 설정하지 않는다면 기본 이미지로 대체됩니다.

모든 설정을 한 이후 Make_Custom_Bot 버튼을 누르면 해당 봇과 대화가 가능합니다.

![image](https://github.com/user-attachments/assets/4c1ee3fb-8e20-45bd-b285-330655bae8a7)

## 제작 이슈

![image](https://github.com/user-attachments/assets/d6f70f9f-ae9f-42b9-a77a-cec0de3916ef)

Gemma 2 의 경우 System role이 존재하지 않았는데, 이를 적용하기 위해 프롬포트 자체에 System role 을 적용.

참고 : https://huggingface.co/google/gemma-2-9b-it/discussions/15
