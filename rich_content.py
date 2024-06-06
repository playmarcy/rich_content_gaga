from tkinter import *
from tkinter.ttk import Combobox, Checkbutton

import json
from content import content_3, content_2, content_1, another_games
from create_widget import create_widget

window = Tk()
window.title("Формирование rich контента")
window.geometry("600x350")


# Приветствие
lbl = Label(window, text="Привет", font=("Helvetica", 12))
lbl.grid(column=0, row=0)


# Поле ввода
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

# Кнопка
def clicked():
    res = f"Привет {txt.get()}"
    lbl.configure(text=res)

btn = Button(window, text="Не жмай", bg="black", fg="white", command=clicked)
btn.grid(column=2, row=0)

# Поле выбора блока
combo = Combobox(window)
combo["values"] = (1, 2, 3)
combo.current(0)
combo.grid(column=1, row=1)


window.mainloop()



# count_blocks = int(input('Из скольки блоков будет состоять контент? (1, 2, 3):  '))
# another_games_examples = json.dumps(create_widget(count_blocks), ensure_ascii=False, indent=4)
# print(another_games)
# print(another_games_examples, ',', sep='')
# input("Нажми Enter, чтобы выйти")

