import json
from content import content_3, content_2, content_1, another_games
from create_widget import create_widget

count_blocks = int(input('Из скольки блоков будет состоять контент? (1, 2, 3):  '))
another_games_examples = json.dumps(create_widget(count_blocks), ensure_ascii=False, indent=4)
print(another_games)
print(another_games_examples, ',', sep='')
input("Нажми Enter, чтобы выйти")