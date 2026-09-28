# 목표
- 랭체인 이해, 간단한 체인 구성, llm 호출
- 체인구성
    - 프럼프트 구성 -> llm 호출
    - 해당 구성은 향후 복잡한 agent 구성으로 확장

# 구조
```
/
L app
    L llm.py : llm 모듈
L step3
    L step4_langchain_basic.py  : 체인구성 (prompt | llm) 
```

# 실행
```
python -m steps.step4_langchain_basic
----

# LangChain Runnable 파이프라인

## 핵심 개념

LangChain의 `Runnable`은 LCEL(LangChain Expression Language)의 기반이 되는 표준 인터페이스입니다. `|` (파이프) 연산자를 사용해 여러 컴포넌트를 체이닝할 수 있습니다.

**핵심 메서드**: `invoke()`, `stream()`, `batch()`, `ainvoke()` (비동기)

## 예시: 프롬프트 → LLM → 출력 파서 체인

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# 1. 각 컴포넌트는 모두 Runnable
prompt = ChatPromptTemplate.from_template(
    "{topic}에 대해 한 문장으로 설명해줘"
)
model = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()

# 2. | 연산자로 파이프라인 구성 (LCEL)
chain = prompt | model | output_parser

# 3. 실행
result = chain.invoke({"topic": "LangChain"})
print(result)
```

## 동작 원리

```
입력 dict → [Prompt] → ChatMessage 객체 → [Model] → AIMessage → [Parser] → 문자열
```

각 단계의 **출력이 다음 단계의 입력**으로 자동 전달됩니다.

## 왜 유용한가?

| 기능 | 설명 |
|---|---|
| **일관된 인터페이스** | 모든 컴포넌트가 동일한 방식(`invoke`, `stream` 등)으로 동작 |
| **스트리밍 지원** | `chain.stream()`으로 토큰 단위 실시간 출력 가능 |
| **병렬/분기 처리** | `RunnableParallel`, `RunnableBranch`로 복잡한 흐름 구성 |
| **가독성** | 복잡한 로직을 선언적으로 표현 |

## 응용: 스트리밍 실행

```python
for chunk in chain.stream({"topic": "RAG"}):
    print(chunk, end="", flush=True)
```

이처럼 Runnable은 **레고 블록처럼 컴포넌트를 조립**하는 방식으로 LLM 애플리케이션을 구성하게 해줍니다.
```