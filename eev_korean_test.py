import time
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from common.utils import stream_response

start_time = time.time()
# Ollama 모델을 불러옵니다.
llm = ChatOllama(model="EEVE-Korean-10.8B:latest")

# 프롬프트
prompt = ChatPromptTemplate.from_template("{topic} 에 대하여 간략히 설명해 줘.")

# 체인 생성
chain = prompt | llm | StrOutputParser()

# 간결성을 위해 응답은 터미널에 출력됩니다.
answer = chain.stream({"topic": "deep learning"})

# 스트리밍 출력
stream_response(answer)

# 시간 측정 종료
end_time = time.time()
elapsed_time = end_time - start_time
# 시간 출력
print(f"\n응답 처리 시간: {elapsed_time:.2f}초")