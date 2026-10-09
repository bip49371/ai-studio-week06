# main.py — 호출하는 쪽 (13주차에도 이 코드는 그대로 유지된다)
from mock_llm import mock_llm_call

SYSTEM = "당신은 고객 리뷰 분류기입니다."
# review = "배송이 정말 빨라서 만족합니다"
review = "제품이 파손되었습니다. 환불해주세요"
# review = "제품 품질이 좋아 만족합니다"
result = mock_llm_call(SYSTEM, f"다음 리뷰를 분류하세요: {review}")
print(result["text"])                    # 모델 답변 (JSON 문자열)
print(result["usage"]["output_tokens"])  # 토큰 사용량 확인 습관
