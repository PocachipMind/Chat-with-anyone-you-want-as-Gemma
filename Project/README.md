### Project 실행을 위한 파일을 모아둔 폴더입니다.

## 실행 환경 : Anaconda Environment

저는 ananconda 환경을 활용했습니다.

### 1. 로컬 환경 (OS)에 맞는 Anaconda 실행 파일 다운

링크 : http://www.anaconda.com/

![image](https://github.com/user-attachments/assets/eef74a9d-5c5b-4746-9fc0-fe6839dc87ca)


### 2. Anaconda 설치 후 Terminal 실행 ( Windows OS 기준 Powershell Prompt )

![image](https://github.com/user-attachments/assets/e50acb0e-1f3c-43d4-8700-df1366890a45)

### 3. Terminal 실행 후 Python 가상환경 활성화

- 첨부된 GemmaSprint_env.yaml을 활용
  
- 하기와 같은 Command를 사용하여 가상환경 설치 진행
```
$ conda env create -f GemmaSprint_env.yaml
```
- 환경 설치가 완료되면 하기와 같은 Command를 사용하여 가상환경 활성화 진행
```
$ conda activate GemmaSprint
```
### > 혹여나 명령어가 어렵다면 

![image](https://github.com/user-attachments/assets/3beab979-abcb-4881-abbb-a98a6fe29dc8)

yaml 파일을 다운받고 Anaconda Navigator를 통해 환경을 설정해도 좋습니다.
## 실행 환경 : Visual Studio (VS) Code

### 1. 로컬 환경 (OS)에 맞는VS Code 실행 파일 다운

링크 : http://code.visualstudio.com/

![image](https://github.com/user-attachments/assets/e6e241c4-765a-4b4b-a886-549211a247c7)

### 2. VS Code 설치 후 Python Extension 설치
좌측이 Extension 아이콘 클릭 후 Python Extension Pack 검색 및 설치
![image](https://github.com/user-attachments/assets/76ebe31a-4b97-4db2-bd17-2eabf1a1c383)

### 3. Windows OS 기준 Control + P 후 Python: Select Interpreter 검색

### 4. 실습에서 사용할 환경 선택

예시 이미지의 경우 이름이 조금 다름. 우리의 경우 GemmaSprint 로 나와야함.

![image](https://github.com/user-attachments/assets/be946505-b5ab-4eb4-ae7f-0309a441d6a1)

### 5. 우측 하단에 3.10.14('GemmaSprint': conda)로 표기 되어있는지 확인

## 실행 방법

이 프로젝트의 최상위 레파지토리를 클론합니다. 
```
$ git clone https://github.com/PocachipMind/Chat-with-anyone-you-want-as-Gemma.git
```
그 이후 환경 설정한 VS Code에서 지금 이 폴더로 이동합니다. ( Chat-with-anyone-you-want-as-Gemma/Project )

![image](https://github.com/user-attachments/assets/7ef7ecc4-f00f-49d6-a222-66f7e56bc4e6)

해당 폴더 내의 ```gui_gemma_1차탭 완성.py```을 실행합니다. 

![image](https://github.com/user-attachments/assets/a5835566-5728-49bf-b337-c876b2355dc0)

