import gradio as gr

import first_tab
import second_tab

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
                    bot_name.change(first_tab.sync_bot_name, inputs=bot_name, outputs=profile_name)
                    
                    # 모델 설정 버튼
                    bot_submit_btn.click(first_tab.create_profile, inputs=[profile_image, profile_image_back, profile_name, profile_status], outputs=profile_display)
                    
                    # 상태 변수 생성
                    model_state = gr.State(value="")  # 초기값 설정
                    bot_submit_btn.click(first_tab.set_model, inputs=[bot_name, bot_gender, bot_profession, bot_personality], outputs=model_state)  # 상태 변수 업데이트
                    
                    
            
            with gr.Column():
                chatbot = gr.Chatbot()
                msg = gr.Textbox(placeholder="Enter your message.")
                clear = gr.Button("Clear")

                msg.submit(first_tab.respond, [msg, chatbot, model_state], [msg, chatbot])
                clear.click(lambda: None, None, chatbot, queue=False)
                bot_submit_btn.click(lambda: None, None, chatbot, queue=False)
        
        examples = gr.Examples(
            examples=[
                ["차은우", "남자", "연예인", "친절한", "./Images/ex1.png", "./Images/ex1_back.jpg", "저도 질투란걸 해요.저 메뉴 맛있겠다."],
                ["골드로저", "남자", "해적", "호탕한", "./Images/ex2.png", "./Images/ex2_back.png", "원피스는 실존한다."],
            ],
            inputs=[bot_name, bot_gender, bot_profession, bot_personality, profile_image, profile_image_back, profile_status],
            )
    
    with gr.Tab("Fine Tuned Chat mod"):
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    with gr.Column():
                        select = gr.Dropdown(["쇼펜하우어", "2번튜닝", "3번튜닝"], label="Bot select", info="select fine tuned model.")
                    with gr.Column():
                        profile_display = gr.HTML()
                    
                    select.change(second_tab.create_profile, inputs=select, outputs=profile_display)
                    
                    
                    
                    
            with gr.Column():
                chatbot = gr.Chatbot()
                msg = gr.Textbox(placeholder="Enter your message.")
                clear = gr.Button("Clear")

                msg.submit(second_tab.respond, [msg, chatbot, select], [msg, chatbot])
                clear.click(lambda: None, None, chatbot, queue=False)
                select.change(lambda: None, None, chatbot, queue=False)

        
    

        

demo.launch(share=True)