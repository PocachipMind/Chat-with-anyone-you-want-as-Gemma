### 모델 Train 관련

## 실행 환경 : Google Colab

저는 ananconda 환경을 활용했습니다.

## 학습 데이터 수집 : GPT, 쇼펜하우어 저서 사용

Project Gutenberg 사이트를 통해 해외의 저작권 만료된 작품을 무료로 이용할 수 있습니다.

여기서 쇼펜하우어의 저서를 통해 데이터를 생성했습니다.

ex ) 

(쇼펜하우어 pdf를 주며) 해당 저서를 인용해서 데이터를 만들어줘, ( 쇼펜하우어 저서를 복사한 후 ) 해당 저서를 활용해서 학습 데이터를 만들어줘.

사용 저서 : https://www.gutenberg.org/ebooks/10731

![image](https://github.com/user-attachments/assets/6919c10d-9dae-4e44-8d12-89e538d07536)

## 학습

양자화를 하고 LoRA의 기법을 사용하여 학습을 진행.
