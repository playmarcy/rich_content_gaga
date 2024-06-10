import tkinter as tk
from tkinter.ttk import Combobox, Checkbutton

import json
from content import content_3, content_2, content_1, another_games
from create_widget import create_widget

window = tk.Tk()
window.title("Формирование rich контента")

lbl1 = tk.Label(window, text="Сюда название игры")
lbl1.grid(column=0, row=0)
txt1 = tk.Entry(width=40)
txt1.grid(column=0, row=1)

lbl2 = tk.Label(window, text="Сюда ссылка на картинку")
lbl2.grid(column=0, row=2)
txt2 = tk.Entry(width=40)
txt2.grid(column=0, row=3)

lbl3 = tk.Label(window, text="Сюда ссылка на озон")
lbl3.grid(column=0, row=4)
txt3 = tk.Entry(width=40)
txt3.grid(column=0, row=5)

window.mainloop()



# count_blocks = int(input('Из скольки блоков будет состоять контент? (1, 2, 3):  '))
# another_games_examples = json.dumps(create_widget(count_blocks), ensure_ascii=False, indent=4)
# print(another_games)
# print(another_games_examples, ',', sep='')
# input("Нажми Enter, чтобы выйти")

