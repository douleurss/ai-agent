import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ChatBot:
    def __init__(self):
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        self.api_url = os.getenv("DASHSCOPE_CHAT_URL")
        self.history = []  # 用列表保存聊天历史

    def send_message(self, user_input):
        # 发消息的方法：接收用户输入，返回回复
        self.history.append({"role": "user", "content": user_input})
        data = {
            "model": "qwen-turbo",
            "messages":self.history,
            "stream":False
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(self.api_url,json=data,headers=headers)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def show_history(self):
        return self.history

    def clear_history(self):
        """清空聊天历史"""
        self.history.clear()
        print("聊天历史已清空")

# 测试运行
if __name__ == "__main__":
    bot=ChatBot()
    print(bot.send_message("你好"))
    # print(bot.show_history())