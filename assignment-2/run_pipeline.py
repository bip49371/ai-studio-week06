import pandas as pd
from classify import classify_review

df = pd.read_csv("reviews_sample.csv") #csv파일의 리뷰 읽기
reviews = df["review_text"].tolist()

stats = {}
failed_count = 0
for r in reviews:
    result = classify_review(r)
    if result is None:          # 실패 건은 건너뛰되 기록
        failed_count+=1
        continue
    cat = result["category"]
    stats[cat] = stats.get(cat, 0) + 1
print("카테고리 별 집계:", stats)
print(f"처리 {len(reviews)}건 / 실패 {failed_count}건")