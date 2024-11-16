import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# 제목 설정
st.title("6하원칙 기반 작문 도우미")

# API 키 입력 받기
api_key = st.text_input("Google API Key를 입력하세요", type="password")
ㅔ
if api_key:
    # Gemini 모델 설정
    genai.configure(api_key=api_key)
    
    # 6하원칙 입력 필드
    who = st.text_input("누가")
    when = st.text_input("언제")
    where = st.text_input("어디서")
    what = st.text_input("무엇을")
    how = st.text_input("어떻게")
    why = st.text_input("왜")

    # 프롬프트 템플릿 설정
    template = """
    다음 6하원칙을 바탕으로 자연스러운 글을 작성해주세요:
    
    누가: {who}
    언제: {when}
    어디서: {where}
    무엇을: {what}
    어떻게: {how}
    왜: {why}
    """

    prompt = PromptTemplate(
        input_variables=["who", "when", "where", "what", "how", "why"],
        template=template
    )

    # 생성 버튼
    if st.button("글 생성하기"):
        if who and when and where and what and how and why:
            try:
                # Gemini 모델 초기화
                llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", 
                                           temperature=0.7,
                                           google_api_key=api_key)
                
                # 프롬프트 생성
                final_prompt = prompt.format(
                    who=who,
                    when=when,
                    where=where,
                    what=what,
                    how=how,
                    why=why
                )
                
                # 결과 생성
                response = llm.invoke(final_prompt)
                
                # 결과 출력
                st.subheader("생성된 글:")
                st.write(response.content)
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {str(e)}")
        else:
            st.warning("모든 항목을 입력해주세요.")
else:
    st.warning("API 키를 입력해주세요.")
