import json
import pyperclip


with open("text.txt", "r", encoding="utf-8") as text:
    text = text.readlines()
    # Баннер для пати
    banner = {
        "widgetName": "raShowcase",
        "type": "billboard",
        "blocks": [
            {
                "imgLink": "",
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-0/6678436572.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-q/6675918146.jpg",
                    "alt": "",
                    "width": 1416,
                    "height": 300,
                    "widthMobile": 750,
                    "heightMobile": 272,
                },
                "title": {
                    "content": ["Весёлые игры для компании"],
                    "size": "size6",
                    "align": "center",
                    "color": "color2",
                },
                "text": {
                    "size": "size1",
                    "align": "center",
                    "color": "color2",
                    "content": [""],
                },
            }
        ],
    }
    # Позже удалить сверху
    content1 = content = {
        "widgetName": "raShowcase",
        "type": "tileL",
        "blocks": [
            {
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "alt": "",
                    "width": 900,
                    "height": 900,
                    "heightMobile": 900,
                    "widthMobile": 900,
                    "isParandja": False,
                    "isParandjaMobile": False,
                },
                "imgLink": "https://ozon.ru/t/b4dVyaW",
                "title": {
                    "content": [],
                    "size": "size4",
                    "align": "center",
                    "color": "color1",
                },
                "text": {
                    "size": "size2",
                    "align": "center",
                    "color": "color3",
                    "content": [],
                },
            },
            {
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "alt": "",
                    "width": 900,
                    "height": 900,
                    "heightMobile": 900,
                    "widthMobile": 900,
                    "isParandja": False,
                    "isParandjaMobile": False,
                },
                "imgLink": "https://ozon.ru/t/b4dVyaW",
                "title": {
                    "content": [],
                    "size": "size4",
                    "align": "center",
                    "color": "color1",
                },
                "text": {
                    "size": "size2",
                    "align": "center",
                    "color": "color3",
                    "content": [],
                },
            },
            {
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "alt": "",
                    "width": 900,
                    "height": 900,
                    "heightMobile": 900,
                    "widthMobile": 900,
                    "isParandja": False,
                    "isParandjaMobile": False,
                },
                "imgLink": "https://ozon.ru/t/b4dVyaW",
                "title": {
                    "content": [],
                    "size": "size4",
                    "align": "center",
                    "color": "color1",
                },
                "text": {
                    "size": "size2",
                    "align": "center",
                    "color": "color3",
                    "content": [],
                },
            },
        ],
    }
    content2 = content = {
        "widgetName": "raShowcase",
        "type": "tileL",
        "blocks": [
            {
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "alt": "",
                    "width": 900,
                    "height": 900,
                    "heightMobile": 900,
                    "widthMobile": 900,
                    "isParandja": False,
                    "isParandjaMobile": False,
                },
                "imgLink": "https://ozon.ru/t/b4dVyaW",
                "title": {
                    "content": [],
                    "size": "size4",
                    "align": "center",
                    "color": "color1",
                },
                "text": {
                    "size": "size2",
                    "align": "center",
                    "color": "color3",
                    "content": [],
                },
            },
            {
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "alt": "",
                    "width": 900,
                    "height": 900,
                    "heightMobile": 900,
                    "widthMobile": 900,
                    "isParandja": False,
                    "isParandjaMobile": False,
                },
                "imgLink": "https://ozon.ru/t/b4dVyaW",
                "title": {
                    "content": [],
                    "size": "size4",
                    "align": "center",
                    "color": "color1",
                },
                "text": {
                    "size": "size2",
                    "align": "center",
                    "color": "color3",
                    "content": [],
                },
            },
            {
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "alt": "",
                    "width": 900,
                    "height": 900,
                    "heightMobile": 900,
                    "widthMobile": 900,
                    "isParandja": False,
                    "isParandjaMobile": False,
                },
                "imgLink": "https://ozon.ru/t/b4dVyaW",
                "title": {
                    "content": [],
                    "size": "size4",
                    "align": "center",
                    "color": "color1",
                },
                "text": {
                    "size": "size2",
                    "align": "center",
                    "color": "color3",
                    "content": [],
                },
            },
        ],
    }
    content3 = content = {
        "widgetName": "raShowcase",
        "type": "tileL",
        "blocks": [
            {
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "alt": "",
                    "width": 900,
                    "height": 900,
                    "heightMobile": 900,
                    "widthMobile": 900,
                    "isParandja": False,
                    "isParandjaMobile": False,
                },
                "imgLink": "https://ozon.ru/t/b4dVyaW",
                "title": {
                    "content": [],
                    "size": "size4",
                    "align": "center",
                    "color": "color1",
                },
                "text": {
                    "size": "size2",
                    "align": "center",
                    "color": "color3",
                    "content": [],
                },
            },
            {
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "alt": "",
                    "width": 900,
                    "height": 900,
                    "heightMobile": 900,
                    "widthMobile": 900,
                    "isParandja": False,
                    "isParandjaMobile": False,
                },
                "imgLink": "https://ozon.ru/t/b4dVyaW",
                "title": {
                    "content": [],
                    "size": "size4",
                    "align": "center",
                    "color": "color1",
                },
                "text": {
                    "size": "size2",
                    "align": "center",
                    "color": "color3",
                    "content": [],
                },
            },
            {
                "img": {
                    "src": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-g/6654556780.jpg",
                    "alt": "",
                    "width": 900,
                    "height": 900,
                    "heightMobile": 900,
                    "widthMobile": 900,
                    "isParandja": False,
                    "isParandjaMobile": False,
                },
                "imgLink": "https://ozon.ru/t/b4dVyaW",
                "title": {
                    "content": [],
                    "size": "size4",
                    "align": "center",
                    "color": "color1",
                },
                "text": {
                    "size": "size2",
                    "align": "center",
                    "color": "color3",
                    "content": [],
                },
            },
        ],
    }
    contents = [content1, content2, content3]

    row_count = 0
    for content in contents:
        for block in content["blocks"]:
            row = text[row_count].strip().split("$")
            row_count += 1
            block["img"]["src"] = row[2]
            block["img"]["srcMobile"] = row[2]
            block["imgLink"] = row[1]
            block["title"]["content"] = [row[0]]
            block["text"]["content"] = [row[3]]

pyperclip.copy(
    json.dumps(banner, ensure_ascii=False, indent=4)
    + ","
    + json.dumps(contents, ensure_ascii=False, indent=4)[1:-1]
    + ","
)
print("Всё готово, результат в буфере обмена!")
