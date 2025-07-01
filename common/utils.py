from langchain_core.messages import AIMessageChunk

def stream_response(response, return_output=False):
    """
    AI 모델로부터의 응답을 스트리밍하여 각 청크를 처리하면서 출력

    매개변수:
    - response (iterable): `AIMessageChunk` 객체 또는 문자열일 수 있는 응답 청크의 이터러블
    - return_output (bool, optional): True인 경우, 함수는 연결된 응답 문자열을 문자열로 반환. 기본값은 False

    반환값:
    - str: `return_output`이 True인 경우, 연결된 응답 문자열.
    """
    answer = ""
    for token in response:
        if isinstance(token, AIMessageChunk):
            answer += token.content
            print(token.content, end="", flush=True)
        elif isinstance(token, str):
            answer += token
            print(token, end="", flush=True)
    if return_output:
        return answer