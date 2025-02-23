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
def create_profile(image, img_back , name="", status=""):
    
    # 업로드된 이미지가 없으면 기본 이미지를 사용하도록 변경
    if image:
        img_base64 = encode_image_to_base64(image)
    else:
        # 기본 이미지 경로를 설정
        default_image_path = "./Images/default_image.png"  # 로컬에 저장된 기본 이미지 경로
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
        print(bot_message)
        

        # 생성된 텍스트 출력 (입력된 프롬프트 이후의 생성 텍스트만 출력)
        generated_text = "모델이 없는 시연용 페이지입니다."
        chat_history.append((message, generated_text))
        return "", chat_history
