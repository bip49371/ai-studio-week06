import json
from mock_llm import mock_llm_call
"""mock_llm이 제대로 되었나 확인하기 위한 검증용 함수"""
counts = {
    "정상": 0,
    "코드펜스": 0,
    "사족": 0,
    "잘림": 0
}

for i in range(100):
    result = mock_llm_call("고객 리뷰 분류기", "배송이 늦어요")
    raw = result["text"]

    if raw.startswith("```"):
        counts["코드펜스"] += 1

    elif raw.startswith("물론입니다"):
        counts["사족"] += 1

    else:
        try:
            json.loads(raw)
            counts["정상"] += 1

        except json.JSONDecodeError:
            counts["잘림"] += 1

print(counts)