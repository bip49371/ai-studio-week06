# mock_llm.py — 6~12주차용 모의 LLM 모듈
import random

def mock_llm_call(system, user_message, temperature=0.2, max_tokens=500):
    """실제 API와 동일한 인터페이스를 갖는 모의 함수.
    13주차에 이 함수의 내부만 실제 Anthropic 호출로 교체한다."""
    reviews_keywords = {
        "배송": '{"category": "배송", "sentiment": "긍정", "score": 4}',
        "환불": '{"category": "환불", "sentiment": "부정", "score": 2}',
        "품질": '{"category": "품질", "sentiment": "긍정", "score": 5}',
    }
    canned = '{"category" : "기타", "sentiment" : "중립", "score" : 3}'
    for keyword, response in reviews_keywords.items():
        if keyword in user_message:
            canned = response
            break #특정 키워드를 발견하면 return을 통해 함수가 바로 종료되는 문제 해결
    stop_reason = "end_turn"
    if random.random() < 0.2: #불량 응답 생성 코드 추가. error_type에 따라 세 가지 처리를 구현함
        error_type = random.choice(
            ["code_fence", "extra_text", "truncated"]
        )
        if error_type == "code_fence": 
            canned = f"```json\n{canned}\n```"
        elif error_type == "extra_text":
            canned = "물론입니다! 분석 결과는 다음과 같습니다.\n" + canned
        elif error_type == "truncated":
            canned = canned[:len(canned) // 2]
            stop_reason = "max_tokens"

    return {
        "text": canned,
        "stop_reason": stop_reason,
        "usage": {"input_tokens": 120, "output_tokens": 35}}
