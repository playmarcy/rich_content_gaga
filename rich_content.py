import json
from content import content_3, content_2, content_1
from create_widget import create_widget


another_games = '''{
    "widgetName": "raTextBlock",
    "title": {
        "content": [],
        "size": "size1",
        "color": "color1"
    },
    "theme": "default",
    "padding": "type1",
    "gapSize": "s",
    "text": {
        "size": "size6",
        "align": "center",
        "color": "color2",
        "content": [
            "Другие игры серии"
        ]
    }
},'''
another_games_examples = {
    1: content_1,
    2: content_2,
    3: content_3,
}

count_blocks = int(input('Из скольки блоков будет состоять контент? (1, 2, 3):  '))
print(another_games)
print(create_widget(count_blocks))
