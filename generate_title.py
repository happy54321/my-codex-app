import random

STYLE_TEMPLATES = {
    "活潑": [
        "來點{topic}的樂趣吧！",
        "不容錯過的{topic}秘訣",
        "{topic}太棒了！",
        "準備好迎接{topic}的驚喜嗎？",
        "跟著我們一起玩{topic}！"
    ],
    "懷舊": [
        "重回{topic}的美好時光",
        "{topic}的經典回憶",
        "那些年的{topic}",
        "再次感受{topic}的溫度",
        "{topic}舊時風華"
    ],
    "勵志": [
        "{topic}讓你更強大",
        "向{topic}邁進",
        "{topic}的力量",
        "別放棄，{topic}在等你",
        "挑戰{topic}，成就更好的自己"
    ],
    "情緒化": [
        "無法抗拒的{topic}",
        "{topic}讓我感動",
        "關於{topic}的那些眼淚",
        "與{topic}共鳴的瞬間",
        "{topic}，直擊心靈"
    ]
}


def generate_titles(topic: str, style: str):
    """Generate 3-5 IG post titles based on topic and style."""
    templates = STYLE_TEMPLATES.get(style, ["{topic}"])
    num_titles = random.randint(3, 5)
    titles = []
    for _ in range(num_titles):
        template = random.choice(templates)
        titles.append(template.format(topic=topic))
    return titles


if __name__ == "__main__":
    import sys
    t = sys.argv[1] if len(sys.argv) > 1 else "測試主題"
    s = sys.argv[2] if len(sys.argv) > 2 else "活潑"
    print(generate_titles(t, s))
