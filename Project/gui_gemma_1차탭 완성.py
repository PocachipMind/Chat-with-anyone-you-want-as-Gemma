import gradio as gr

################################### 커스텀 대화 탭 ( 1번 탭 ) 함수 ###################################

import base64

### 프로필 부분 ###

def sync_bot_name(bot_name):
    return bot_name  # Just return the same name for profile_name

# Base64로 이미지를 인코딩하는 함수
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# 프로필 레이아웃을 KakaoTalk 스타일로 맞춤
def create_profile(image, img_back , name, status):
    # 업로드된 이미지가 없으면 기본 이미지를 사용하도록 변경
    if image:
        img_base64 = encode_image_to_base64(image)
    else:
        # 기본 이미지 경로를 설정
        default_image_path = "default_image.png"  # 로컬에 저장된 기본 이미지 경로
        img_base64 = encode_image_to_base64(default_image_path)
    
    img_tag = f"<img src='data:image/png;base64,{img_base64}' style='border-radius:25%; width:100px; height:100px; display: block; margin: 0 auto;'>"

    # 업로드된 백그라운드 이미지가 없으면 기본 이미지를 사용하도록 변경
    if img_back:
        img_back_tag = encode_image_to_base64(img_back)
    else:
        # 기본 색상인 회색으로 리턴
        return f"""
<div style="background-color:#848b91; padding:20px; border-radius:20px; width:280px; height:500px; font-family: Arial, sans-serif; color: white; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; margin-bottom: 60px;">
        <div style="display: flex; gap: 10px;">
            <div style="width: 30px; height: 30px; background-color: #9a9a9a; border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                </svg>
            </div>
            <div style="width: 30px; height: 30px; background-color: #9a9a9a; border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                </svg>
            </div>
            <div style="width: 30px; height: 30px; background-color: #9a9a9a; border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
            </div>
            <div style="width: 30px; height: 30px; background-color: #9a9a9a; border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="1"></circle>
                    <circle cx="19" cy="12" r="1"></circle>
                    <circle cx="5" cy="12" r="1"></circle>
                </svg>
            </div>
        </div>
        <div style="font-size: 24px; cursor: pointer;">×</div>
    </div>
    <div style="text-align:center; flex-grow: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; padding-bottom: 80px;">
        {img_tag}
        <h2 style="font-size:18px; margin: 10px 0 5px 0;">{name}</h2>
        <p style="color:#e0e0e0; font-size:14px; margin: 0;">
            {status}
            <span style="display: inline-block; width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 5px solid #e0e0e0; margin-left: 5px; vertical-align: middle;"></span>
        </p>
    </div>
    <div style="display: flex; justify-content: space-around;">
        <button style="background:none; border:none; color: white; font-size:14px; display: flex; flex-direction: column; align-items: center;">
            <span style="font-size: 24px; margin-bottom: 5px;">💬</span>
            1:1 채팅
        </button>
        <button style="background:none; border:none; color: white; font-size:14px; display: flex; flex-direction: column; align-items: center;">
            <span style="font-size: 24px; margin-bottom: 5px;">📞</span>
            보이스톡
        </button>
        <button style="background:none; border:none; color: white; font-size:14px; display: flex; flex-direction: column; align-items: center;">
            <span style="font-size: 24px; margin-bottom: 5px;">📹</span>
            페이스톡
        </button>
    </div>
</div>
    """

    # KakaoTalk 프로필 스타일로 HTML 작성        
    return f"""
<div style="background-image: url('data:image/png;base64,{img_back_tag}'); background-size: cover; background-position: center; padding:20px; border-radius:20px; width:280px; height:500px; font-family: Arial, sans-serif; color: white; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; margin-bottom: 60px;">
        <div style="display: flex; gap: 10px;">
            <div style="width: 30px; height: 30px; background-color: rgba(154, 154, 154, 0.7); border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                </svg>
            </div>
            <div style="width: 30px; height: 30px; background-color: rgba(154, 154, 154, 0.7); border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                </svg>
            </div>
            <div style="width: 30px; height: 30px; background-color: rgba(154, 154, 154, 0.7); border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="12" y1="16" x2="12" y2="12"></line>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                </svg>
            </div>
            <div style="width: 30px; height: 30px; background-color: rgba(154, 154, 154, 0.7); border-radius: 50%; display: flex; justify-content: center; align-items: center;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="1"></circle>
                    <circle cx="19" cy="12" r="1"></circle>
                    <circle cx="5" cy="12" r="1"></circle>
                </svg>
            </div>
        </div>
        <div style="font-size: 24px; cursor: pointer;">×</div>
    </div>
    <div style="text-align:center; flex-grow: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; padding-bottom: 80px;">
        {img_tag}
        <h2 style="font-size:18px; margin: 10px 0 5px 0; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">{name}</h2>
        <p style="color:#e0e0e0; font-size:14px; margin: 0; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">
            {status}
            <span style="display: inline-block; width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 5px solid #e0e0e0; margin-left: 5px; vertical-align: middle;"></span>
        </p>
    </div>
    <div style="display: flex; justify-content: space-around;">
        <button style="background:none; border:none; color: white; font-size:14px; display: flex; flex-direction: column; align-items: center; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">
            <span style="font-size: 24px; margin-bottom: 5px;">💬</span>
            1:1 채팅
        </button>
        <button style="background:none; border:none; color: white; font-size:14px; display: flex; flex-direction: column; align-items: center; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">
            <span style="font-size: 24px; margin-bottom: 5px;">📞</span>
            보이스톡
        </button>
        <button style="background:none; border:none; color: white; font-size:14px; display: flex; flex-direction: column; align-items: center; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">
            <span style="font-size: 24px; margin-bottom: 5px;">📹</span>
            페이스톡
        </button>
    </div>
</div>
    """

### 챗봇 부분 ###

from transformers import AutoTokenizer, AutoModelForCausalLM

# 토크나이저와 모델 불러오기
tokenizer = AutoTokenizer.from_pretrained("carrotter/ko-gemma-2b-it-sft")
model = AutoModelForCausalLM.from_pretrained("carrotter/ko-gemma-2b-it-sft")

# 모델 설정 부분

# 모델 상태 선언
def set_model(bot_name, bot_gender, bot_profession, bot_personality, state_var):
    prompt = (
        "<bos>"
        "<start_of_turn>system\n"
        f"당신은 {bot_gender} {bot_profession}입니다. 당신의 이름은 '{bot_name}'입니다. 당신은 {bot_personality} 태도로 대화를 합니다. "
        "\n<end_of_turn>"
    )
    state_var = prompt  # 값을 상태 변수에 저장
    return state_var  # 상태 변수를 반환하여 업데이트

# 대화 부분

def respond(message, chat_history, model_state):
        bot_message = model_state + "<start_of_turn>user\n" + message + "\n<end_of_turn>" + "<start_of_turn>model\n"
        # print(bot_message) # 확인용
        # 텍스트 토큰화 및 디바이스로 이동
        inputs = tokenizer.encode(bot_message, add_special_tokens=False, return_tensors="pt").to(model.device)

        # 종료 조건 설정
        terminators = [
            tokenizer.eos_token_id,  # EOS 토큰 사용
            tokenizer.convert_tokens_to_ids("<end_of_turn>")  # <end_of_turn> 토큰을 종료 조건으로 설정
        ]

        # 텍스트 생성
        outputs = model.generate(
            input_ids=inputs,
            max_new_tokens=100,  # 생성할 최대 토큰 수를 줄여서 한 번의 응답만 생성
            eos_token_id=terminators,  # 종료 조건으로 EOS 토큰 사용
            do_sample=True,  # 샘플링 사용
            temperature=0.5,  # 다양성을 위한 온도 조절
            top_p=0.9  # Top-p 샘플링
        )

        # 생성된 텍스트 출력 (입력된 프롬프트 이후의 생성 텍스트만 출력)
        generated_text = tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)
        chat_history.append((message, generated_text))
        return "", chat_history

###################################  GUI 웹 부분  ###################################

# 스타팅 꾸미기
js = """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';

    var text = 'Chat with anyone you want as Gemma!';
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 250);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}
"""

with gr.Blocks(js=js) as demo:

    # 커스텀 대화 탭
    with gr.Tab("Custom Chat mod"):
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    with gr.Column():
                        bot_name = gr.Textbox(label="Bot Name",placeholder="Enter a name for your bot.")
                        bot_gender = gr.Dropdown(["남자", "여자"], label="Bot Gender", info="Enter the gender of your bot.")
                        bot_profession = gr.Textbox(label="Bot Profession",placeholder="Enter the bot's profession.")
                        bot_personality = gr.Textbox(label="Bot Personality",placeholder="Enter the personality of your bot.")
                        with gr.Accordion("Make Bot Progile", open= False):
                            profile_image = gr.Image(label="Upload Profile Image", placeholder="Upload a profile image to create bot profile.", type="filepath")
                            profile_image_back = gr.Image(label="Upload Background Image",placeholder="Upload a background image for bot profile.", type="filepath")
                            profile_name = gr.Textbox(label="Name",interactive=False)
                            profile_status = gr.Textbox(label="Status Message", placeholder="Enter a status message to create bot profile.", value="Hello. What a great day!")
                        bot_submit_btn = gr.Button("Make_Custom_Bot")
                    with gr.Column():
                        profile_display = gr.HTML()
                    
                    # 동기화 함수
                    bot_name.change(sync_bot_name, inputs=bot_name, outputs=profile_name)
                    
                    # 모델 설정 버튼
                    bot_submit_btn.click(create_profile, inputs=[profile_image, profile_image_back, profile_name, profile_status], outputs=profile_display)
                    
                    # 상태 변수 생성
                    model_state = gr.State(value="")  # 초기값 설정
                    bot_submit_btn.click(set_model, inputs=[bot_name, bot_gender, bot_profession, bot_personality], outputs=model_state)  # 상태 변수 업데이트
                    
                    
            
            with gr.Column():
                chatbot = gr.Chatbot()
                msg = gr.Textbox(placeholder="Enter your message.")
                clear = gr.Button("Clear")

                msg.submit(respond, [msg, chatbot, model_state], [msg, chatbot])
                clear.click(lambda: None, None, chatbot, queue=False)
        
        examples = gr.Examples(
            examples=[
                ["차은우", "남자", "연예인", "친절한", "./ex1.png", "./ex1_back.jpg", "저도 질투란걸 해요.저 메뉴 맛있겠다."],
                ["골드로저", "남자", "해적", "호탕한", "./ex2.png", "./ex2_back.png", "원피스는 실존한다."],
            ],
            inputs=[bot_name, bot_gender, bot_profession, bot_personality, profile_image, profile_image_back, profile_status],
            )
    
    with gr.Tab("Fine Tuned Chat mod"):
        with gr.Row():
            with gr.Column():
                select = gr.Dropdown(["1번튜닝", "2번튜닝"], label="Bot select", info="select fine tuned model.")
                profile_display = gr.HTML()
                bot_submit_btn.click(create_profile, inputs=[profile_image, profile_image_back, profile_name, profile_status], outputs=profile_display)
                
            with gr.Column():
                chatbot = gr.Chatbot()
                msg = gr.Textbox(placeholder="Enter your message.")
                clear = gr.Button("Clear")
        
    

        

demo.launch(share=True)