import gradio as gr
from google import genai
from google.genai import types

client =  genai.Client()

with gr.Blocks() as demo:
    gr.Markdown("## Text to Summarization(總結)")
    style_radio = gr.Radio(choices=['小學','商業','專業','口語化','條列式'], label="風格")
    input_text = gr.Textbox(
        label="輸入文章",
        lines=10,
        submit_btn=True

    )
    output_md = gr.Markdown()

    @input_text.submit(inputs=[input_text, style_radio], outputs=[output_md])
    def summarize(text, style):
        if style == "口語化":
            style = "請使用口語化的風格\n"
        elif style == "小學":
            style = "請使用小生看得懂的語法\n"
        elif style == "學術":
            style = "請使用學術的風格\n"
        elif style == "商業":
            style = "請使用商業的風格\n"
        elif style == "專業":
            style = "請使用專業的風格\n"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config= types.GenerateContentConfig(
                system_instruction=f"""
                你是一個專業的總結助手，也是一個繁體中文的高手，請根據用戶提供的文章內容進行總結。
                你需要根據用戶選擇的風格來調整總結的語氣和格式，並且確保總結的內容清晰、簡潔且易於理解。
                目前使用者選擇的是風格: {style}。

                所有的回覆必須是markdown的語法
                """
            ),
            contents = [text]
        )
        summary = f"風格: {style}\n\n{response.text}"
        return summary

demo.launch()