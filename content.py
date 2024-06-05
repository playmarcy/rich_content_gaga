import json

another_games = '''{
      "widgetName": "raTextBlock",
      "title": {
        "content": [
          "Другие игры серии"
        ],
        "size": "size6",
        "color": "color2",
        "align": "center"
      },
      "theme": "default",
      "padding": "type1",
      "gapSize": "s",
      "text": {
        "size": "size1",
        "align": "left",
        "color": "color1",
        "content": [
          ""
        ]
      }
    },'''

content3 = '''{
      "widgetName": "raShowcase",
      "type": "tileL",
      "blocks": [
        {
          "img": {
            "src": "https://cdn1.ozone.ru/s3/multimedia-c/6688718112.jpg",
            "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-c/6688718112.jpg",
            "alt": "",
            "position": "to_the_edge",
            "positionMobile": "to_the_edge",
            "isParandja": false,
            "isParandjaMobile": false
          },
          "imgLink": "https://ozon.ru/t/b4dVyaW",
          "title": {
            "content": [
              "Битва Легенд  (Том Первый)"
            ],
            "size": "size4",
            "align": "center",
            "color": "color1"
          },
          "text": {
            "size": "size1",
            "align": "left",
            "color": "color1",
            "content": [
              ""
            ]
          }
        },
        {
          "img": {
            "src": "https://cdn1.ozone.ru/s3/multimedia-b/6686502167.jpg",
            "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-b/6686502167.jpg",
            "alt": "",
            "position": "to_the_edge",
            "positionMobile": "to_the_edge",
            "isParandja": false,
            "isParandjaMobile": false
          },
          "imgLink": "https://ozon.ru/t/j4XjYJk",
          "title": {
            "content": [
              "Туман над Мостовой"
            ],
            "size": "size4",
            "align": "center",
            "color": "color1"
          },
          "text": {
            "size": "size1",
            "align": "left",
            "color": "color1",
            "content": [
              ""
            ]
          }
        },
        {
          "img": {
            "src": "https://cdn1.ozone.ru/s3/multimedia-7/6686502163.jpg",
            "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-7/6686502163.jpg",
            "alt": "",
            "position": "to_the_edge",
            "positionMobile": "to_the_edge",
            "isParandja": false,
            "isParandjaMobile": false
          },
          "imgLink": "https://ozon.ru/t/aeAZdbp",
          "title": {
            "content": [
              "Красная Шапочка vs Беовульф"
            ],
            "size": "size4",
            "align": "center",
            "color": "color1"
          },
          "text": {
            "size": "size1",
            "align": "left",
            "color": "color1",
            "content": [
              ""
            ]
          }
        }
      ]
    }'''

content2 = '''{
      "widgetName": "raShowcase",
      "type": "tileXL",
      "blocks": [
        {
          "img": {
            "src": "https://cdn1.ozone.ru/s3/multimedia-8/6668746640.jpg",
            "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-8/6668746640.jpg",
            "alt": "",
            "position": "to_the_edge",
            "positionMobile": "to_the_edge",
            "isParandja": false,
            "isParandjaMobile": false
          },
          "imgLink": "https://ozon.ru/t/3nnk2Kz",
          "title": {
            "content": [
              "Чпок 2"
            ],
            "size": "size4",
            "align": "center",
            "color": "color1"
          },
          "text": {
            "size": "size3",
            "align": "center",
            "color": "color3",
            "content": [
              ""
            ]
          }
        },
        {
          "img": {
            "src": "https://cdn1.ozone.ru/s3/multimedia-d/6668746645.jpg",
            "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-f/6668746647.jpg",
            "alt": "",
            "position": "to_the_edge",
            "positionMobile": "to_the_edge",
            "isParandja": false,
            "isParandjaMobile": false
          },
          "imgLink": "https://ozon.ru/t/yllAXzY",
          "title": {
            "content": [
              "Чпок Карманный"
            ],
            "size": "size4",
            "align": "center",
            "color": "color1"
          },
          "text": {
            "size": "size3",
            "align": "center",
            "color": "color3",
            "content": [
              ""
            ]
          }
        }
      ]
    }'''

content1 = '''{
      "widgetName": "raShowcase",
      "type": "billboard",
      "blocks": [
        {
          "imgLink": "https://ozon.ru/t/j4Ey3Rw",
          "img": {
            "src": "https://cdn1.ozone.ru/s3/multimedia-n/6675931679.jpg",
            "srcMobile": "https://cdn1.ozone.ru/s3/multimedia-h/6675931673.jpg",
            "alt": "",
            "position": "width_half",
            "positionMobile": "width_full"
          },
          "title": {
            "content": [
              "Мафия: Большой Город"
            ],
            "size": "size4",
            "align": "center",
            "color": "color1"
          },
          "text": {
            "size": "size1",
            "align": "left",
            "color": "color1",
            "content": [
              ""
            ]
          }
        }
      ]
    }'''

content_3 = json.loads(content3)
content_2 = json.loads(content2)
content_1 = json.loads(content1)