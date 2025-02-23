
## 2번 탭 ##


## 프로필 생성 ( 1번탭 함수 사용 ) ##


import first_tab

def create_profile(select):
    
    if select == "쇼펜하우어":
        return first_tab.create_profile("./Images/first_model.png","./Images/first_model_bg.jpg","쇼펜하우어","인간의 삶은 왜 고통인가?")
    else:
        return first_tab.create_profile(None,None)




### 챗봇 부분 ###

from transformers import AutoTokenizer, AutoModelForCausalLM

# 모델 1 파트
model1 = AutoModelForCausalLM.from_pretrained("PocaChip/my_schopenhauer_model")
tokenizer1 = AutoTokenizer.from_pretrained("PocaChip/my_schopenhauer_model")
terminators1 = [
    tokenizer1.eos_token_id,  # EOS 토큰 사용
    tokenizer1.convert_tokens_to_ids("<end_of_turn>")  # <end_of_turn> 토큰을 종료 조건으로 설정
]

# 모델 2.... 



# 대화 부분
def respond(message, chat_history, select):
    if select == "쇼펜하우어":
        return model1_respond(message, chat_history)
    else :
        return else_respond(message, chat_history)
        


# 모델 1 대답
def model1_respond(message, chat_history):

    chat = [{ "role": "user", "content": message }]

    bot_message = tokenizer1.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)

    inputs = tokenizer1.encode(bot_message, add_special_tokens=False, return_tensors="pt").to(model1.device)

    outputs = model1.generate(input_ids=inputs.to(model1.device), max_new_tokens=100, eos_token_id=terminators1)

    generated_text = tokenizer1.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)
    print(generated_text)
    
    generated_text = tokenizer1.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)
    chat_history.append((message, generated_text))
    return "", chat_history

def else_respond(message, chat_history):
        
        generated_text = "튜닝된 모델을 선택해주세요."
        chat_history.append((message, generated_text))
        return "", chat_history
    
