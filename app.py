from dotenv import load_dotenv
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 環境変数の読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LangChainのLLMインスタンスを作成
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# LLMにプロンプトを渡して回答を取得する関数
def get_llm_response(input_text, expert_type):
    """
    LLMにプロンプトを渡し、回答を取得する関数。

    Parameters:
        input_text (str): ユーザーが入力したテキスト。
        expert_type (str): 専門家の種類（例: "旅行", "映画"）。

    Returns:
        str: LLMからの回答。
    """
    # 専門家の種類に応じたシステムメッセージを設定
    if expert_type == "旅行":
        system_message = "You are a travel expert. Provide detailed and helpful travel advice."
    elif expert_type == "映画":
        system_message = "You are a movie expert. Provide detailed and insightful movie recommendations and analysis."
    else:
        system_message = "You are a helpful assistant."

    # メッセージの構築
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]

    # LLMにメッセージを渡して回答を取得
    result = llm(messages)
    return result.content

# StreamlitアプリのUI構築
st.title("専門家として振る舞うLLMアプリ")
st.write("""
このアプリでは、LLM（大規模言語モデル）に旅行または映画の専門家として振る舞わせることができます。
以下の手順で操作してください:
1. ラジオボタンで専門家の種類を選択してください。
2. 入力フォームに質問や知りたい内容を入力してください。
3. 「実行」ボタンを押すと、LLMからの回答が表示されます。
""")

# 専門家の種類を選択
selected_expert = st.radio(
    "専門家の種類を選択してください。",
    ["旅行", "映画"]
)

# 入力フォーム
user_input = st.text_input("質問や知りたい内容を入力してください:")

# 実行ボタン
if st.button("実行"):
    if user_input.strip() == "":
        st.warning("入力フォームにテキストを入力してください。")
    else:
        # LLMからの回答を取得
        response = get_llm_response(user_input, selected_expert)
        # 回答を表示
        st.divider()
        st.write("### LLMからの回答:")
        st.write(response)