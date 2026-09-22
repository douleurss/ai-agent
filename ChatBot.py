import os
import requests
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

class ChatBot:
    def __init__(self):
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        self.api_url = os.getenv("DASHSCOPE_CHAT_URL")
        self.history = []  # 用列表保存聊天历史

    def chat_fn(self, message, history):
        messages = []
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": message})

        data = {
            "model": "qwen-turbo",
            "messages": messages,
            "stream": False
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(self.api_url, json=data, headers=headers)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        return reply

    def show_history(self):
        return self.history

    def clear_history(self):
        """清空聊天历史"""
        self.history.clear()
        print("聊天历史已清空")

bot = ChatBot()

demo = gr.ChatInterface(
    fn=bot.chat_fn,
    title="千问",
    description="ChatBot",
)

# 测试运行
if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft(),server_name="0.0.0.0",share=True)
    # print(bot.show_history())