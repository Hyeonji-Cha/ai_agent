'''
- 기본 rag
    - 질문 고정 -> 청크 검색(백터 디비) -> 유사도순 랭킹(top_k개 획득) -> 프럼프트 + 검색내용 -> LLM 호출
'''
from app.retrieval import vector_search

q = '상품 자체 하자는 언제까지 환불할 수 있나요?' # 백터디비 검색 유사도로 cs 관련 정책을 가져오도로 구성(목표점)

for chunk in vector_search(q, 3):
    print( chunk )