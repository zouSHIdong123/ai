#!/usr/bin/env python3
"""
AI Chatbot using Moonshot API (Kimi)
"""

import os
from openai import OpenAI


class MoonshotChatbot:
    def __init__(self, api_key=None):
        """
        Initialize the Moonshot AI chatbot
        
        Args:
            api_key (str): Moonshot API key. If None, it will try to get from environment variable
        """
        if api_key is None:
            api_key = os.getenv("MOONSHOT_API_KEY")
        
        if not api_key:
            raise ValueError("API key is required. Set MOONSHOT_API_KEY environment variable or pass as argument.")
        
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.moonshot.cn/v1",
        )
        
        self.history = [
            {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
        ]
    
    def chat(self, query):
        """
        Send a query to the AI and get a response
        
        Args:
            query (str): User's input
            
        Returns:
            str: AI's response
        """
        self.history.append({
            "role": "user", 
            "content": query
        })
        
        try:
            completion = self.client.chat.completions.create(
                model="kimi-k2-turbo-preview",
                messages=self.history,
                temperature=0.6,
            )
            
            result = completion.choices[0].message.content
            self.history.append({
                "role": "assistant",
                "content": result
            })
            
            return result
        except Exception as e:
            print(f"Error occurred: {e}")
            return "抱歉，出现了错误，请稍后再试。"
    
    def reset_conversation(self):
        """Reset the conversation history"""
        self.history = [
            {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
        ]
    
    def get_history(self):
        """Get the current conversation history"""
        return self.history


def main():
    """Main function to run the chatbot in console mode"""
    print("欢迎使用 Moonshot AI 聊天机器人！")
    print("输入 'quit', 'exit', 或 '退出' 来结束对话")
    print("输入 'reset' 来重置对话历史")
    print("-" * 50)
    
    # Initialize the chatbot
    try:
        bot = MoonshotChatbot()
    except ValueError as e:
        print(f"初始化失败: {e}")
        return
    
    while True:
        user_input = input("\n你: ")
        
        if user_input.lower() in ['quit', 'exit', '退出']:
            print("再见！")
            break
        elif user_input.lower() == 'reset':
            bot.reset_conversation()
            print("对话已重置。")
            continue
        
        if user_input.strip():
            print("Kimi: ", end="")
            response = bot.chat(user_input)
            print(response)


if __name__ == "__main__":
    main()