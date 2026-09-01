import requests

with open("data.txt", "r",encoding="utf-8") as data:
    data=data.read()
    print(data)

class ChatBot:
    def __init__(self):
        # 初始化：可以在这里放模型配置、历史记录等
        self.history = []  # 用列表保存聊天历史

    def send_message(self, user_input):
        # 发消息的方法：接收用户输入，返回回复
        self.history.append({"role": "user", "content": user_input})
        # 这里先写一个模拟回复，后面换成真实大模型调用
        reply = f"收到你的消息：{user_input}"
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def show_history(self):
        return self.history

# 测试运行
bot = ChatBot()
response = bot.send_message("你好")
print(response)
print(bot.show_history())