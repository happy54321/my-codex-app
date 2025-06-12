import random

COMMON_TAGS = [
    "#Daily", "#InstaGood", "#分享", "#打卡", "#必看",
    "#生活", "#美照", "#travel", "#love", "#photo"
]


def sanitize_topic(topic: str):
    """Simple function to create hashtag-friendly topic keywords"""
    return ''.join(c for c in topic if c.isalnum() or c in ('_', '-'))


def generate_hashtags(topic: str):
    """Generate 10 mixed Chinese and English hashtags based on topic."""
    keywords = [sanitize_topic(part) for part in topic.split() if part]
    hashtags = [f"#{kw}" for kw in keywords]
    remaining = 10 - len(hashtags)
    if remaining > 0:
        hashtags.extend(random.sample(COMMON_TAGS, k=min(remaining, len(COMMON_TAGS))))
    return hashtags[:10]


if __name__ == "__main__":
    import sys
    t = sys.argv[1] if len(sys.argv) > 1 else "測試主題"
    print(generate_hashtags(t))
