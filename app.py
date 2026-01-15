import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"
        }
    ]

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# Sidebar for API configuration
with st.sidebar:
    st.title("⚙️ 配置")
    
    # API Key input
    api_key_input = st.text_input(
        "API Key", 
        type="password", 
        value=st.session_state.api_key,
        help="输入你的 Moonshot AI API 密钥"
    )
    
    # Update session state with API key
    if api_key_input:
        st.session_state.api_key = api_key_input
    
    # Model selection
    model = st.selectbox(
        "选择模型", 
        ["kimi-k2-turbo-preview"],
        help="选择要使用的 AI 模型"
    )
    
    # Temperature slider
    temperature = st.slider(
        "Temperature", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.6, 
        step=0.1,
        help="控制回复的随机性，值越高回复越随机"
    )
    
    # Clear chat button
    if st.button("🗑️ 清空对话"):
        st.session_state.messages = [
            {
                "role": "system", 
                "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"
            }
        ]
        st.rerun()

# Main title
st.title("🤖 AI 聊天机器人")
st.caption("基于 Moonshot AI 的智能对话助手")

# Display chat messages
for message in st.session_state.messages[1:]:  # Skip system message
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("请输入你的问题..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Initialize OpenAI client
            client = OpenAI(
                api_key=st.session_state.api_key or os.getenv("MOONSHOT_API_KEY") or "$MOONSHOT_API_KEY",
                base_url="https://api.moonshot.cn/v1",
            )
            
            # Get response from API
            completion = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages,
                temperature=temperature,
            )
            
            response = completion.choices[0].message.content
            
            # Display response
            message_placeholder.markdown(response)
            
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            error_message = f"发生错误：{str(e)}"
            message_placeholder.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# Add some information at the bottom
with st.expander("ℹ️ 使用说明"):
    st.markdown("""
    - 在侧边栏输入你的 Moonshot AI API 密钥
    - 选择合适的模型和温度参数
    - 输入问题并按回车键开始对话
    - 点击“清空对话”按钮可以重置聊天历史
    """)