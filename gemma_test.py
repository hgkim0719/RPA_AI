import time
from langchain_ollama import ChatOllama

start_time = time.time()
llm = ChatOllama(
    model="gemma:7b",  # 사용할 언어 모델을 지정합니다.
    format="json",  # 입출력 형식을 JSON으로 설정합니다.
    temperature=0,
)

# JSON 형식의 답변을 요구하는 프롬프트 작성
# prompt = "유럽 여행지 10곳을 알려주세요. key: `places`. resonse in JSON format."
prompt = "유럽 여행지 도시 10곳을 알려주세요. 자세한 설명 말고 장소만 알려주세요. key: `places`. resonse in JSON format."

# 체인 호출
response = llm.invoke(prompt)
print(response.content)  # 생성된 응답을 출력합니다.
# 시간 측정 종료
end_time = time.time()
elapsed_time = end_time - start_time
# 시간 출력
print(f"\n응답 처리 시간: {elapsed_time:.2f}초")