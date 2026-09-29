'''
검색된 사내 문서를 근거로 LLM 답변을 생성하는 RAG 모듈
'''
from langchain_core.prompts import ChatPromptTemplate
from app.llm import get_chat_model
from app.retrieval import vector_search

def answer(query: str) -> str:
    # 랭체인을 이용하여 체인 구성 -> llm 추론 처리
    # 1. 질문에 가장 유사한 사내 규정 5개를 획득
    results = vector_search( query )

    # 2. 검색 결과를 LLM에 프럼프트에 적용할수 있게 구조 조정
    evidence = '\n\n'.join(f"[{code}] {content}" for code,_,_,_,content,_ in results)
    print( evidence )


    return ""