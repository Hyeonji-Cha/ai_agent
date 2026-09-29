'''
텍스트 -> 임베딩 하여 생성된 백터 데이터를 PostgreSQL pgvector에 저장하고, 유사도 검색 SQL 실행
'''

from pgvector import Vector
from app.embedding import get_embeddings