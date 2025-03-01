# 모델 Train 관련

## 실행 환경 : Google Colab

코랩환경을 통해 T4 GPU로 학습을 진행했습니다.

pip install 버전은 pip freeze > requirements.txt 명령어를 통해 requirements.txt에 담겨있습니다.

## 학습

양자화 : BitsAndBytesConfig를 사용하여 4bit 양자화(NF4) 적용

LoRA : peft.LoraConfig, get_peft_model()을 사용하여 LoRA 설정을 적용

prepare_model_for_kbit_training(model)을 사용하여 양자화된 모델에서 미세 조정 가능하도록 설정

bnb_4bit_use_double_quant=True, bnb_4bit_quant_type="nf4" 설정

즉, QLoRA 적용 및 학습

## 학습 데이터 수집 : GPT, 쇼펜하우어 저서 사용

Project Gutenberg 사이트를 통해 해외의 저작권 만료된 작품을 무료로 이용할 수 있습니다.

여기서 쇼펜하우어의 저서를 통해 데이터를 생성했습니다.

ex ) 

- ( 쇼펜하우어 pdf를 주며 ) 해당 저서를 인용해서 학습 데이터를 만들어줘
- ( 쇼펜하우어 저서를 복사한 후 ) 해당 저서를 활용해서 학습 데이터를 만들어줘.

사용 저서 : https://www.gutenberg.org/ebooks/10731

![image](https://github.com/user-attachments/assets/6919c10d-9dae-4e44-8d12-89e538d07536)

## 학습

양자화를 하고 LoRA의 기법을 사용하여 학습을 진행.

![image](https://github.com/user-attachments/assets/570f75ab-f05e-4a74-a65a-403c517471ef)

데이터의 양이 워낙 작아서인지 학습 에포크를 많이 늘리더라도 눈에 띄는 큰 변화가 보이지 않는다고 판단되었음.

![image](https://github.com/user-attachments/assets/435dc954-a78f-48f4-aeb2-6c89f3426388)

그리고 학습을 더 늘릴 경우 좀 더 길게 응답하는 느낌을 받았는데, 짧게 대답하는 모델이 채팅성향과 좀 더 부합하다고 판단했기에 110회 정도의 학습 모델을 채택.

