import tkinter as tk
from tkinter import ttk
import json

# Предустановленные JSON-данные
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

# Глобальная переменная для хранения текстовых полей
text_entries = []

def create_text_entries(num):
    for widget in frame_text_entries.winfo_children():
        widget.destroy()

    global text_entries
    text_entries = []
    labels = ["Название игры", "Ссылка на картинку", "Ссылка на озон"]
    for i in range(num):
        label_text = labels[i % 3]
        label = tk.Label(frame_text_entries, text=f"{label_text} {i//3 + 1}:")
        label.pack()
        entry = tk.Entry(frame_text_entries, width=40)
        entry.pack(pady=2)
        text_entries.append(entry)

def on_option_change(event):
    selection = option_var.get()
    if selection == "1":
        create_text_entries(3)
    elif selection == "2":
        create_text_entries(6)
    elif selection == "3":
        create_text_entries(9)

def call_function():
    input_values = [entry.get() for entry in text_entries]
    result = process_data(input_values, int(option_var.get()))
    output_field.config(state='normal')
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, result)
    output_field.config(state='disabled')

def process_data(input_values, content_number):
    content = eval(f'content_{content_number}')
    for i in range(len(content['blocks'])):
        content['blocks'][i]['title']['content'][0] = input_values[i*3]
        content['blocks'][i]['img']['src'] = input_values[i*3+1]
        content['blocks'][i]['img']['srcMobile'] = input_values[i*3+1]
        content['blocks'][i]['imgLink'] = input_values[i*3+2]
    return another_games + '\n' + json.dumps(content, ensure_ascii=False, indent=4)

# Создание основного окна
root = tk.Tk()
root.title("Input Collector")

# Фрейм для выбора параметра
frame_option = ttk.Frame(root)
frame_option.pack(pady=10)

option_var = tk.StringVar(value="1")
option_label = ttk.Label(frame_option, text="Выберите параметр:")
option_label.pack(side="left")

option_menu = ttk.Combobox(frame_option, textvariable=option_var, values=["1", "2", "3"], state="readonly")
option_menu.pack(side="left")
option_menu.bind("<<ComboboxSelected>>", on_option_change)

# Фрейм для текстовых полей
frame_text_entries = ttk.Frame(root)
frame_text_entries.pack(pady=10)

# Фрейм для кнопки
frame_button = ttk.Frame(root)
frame_button.pack(pady=10)

submit_button = ttk.Button(frame_button, text="Выполнить", command=call_function)
submit_button.pack()

# Фрейм для вывода результата
frame_output = ttk.Frame(root)
frame_output.pack(pady=10)

output_label = ttk.Label(frame_output, text="Результат:")
output_label.pack()

output_field = tk.Text(frame_output, height=20, width=100, state='disabled')
output_field.pack()

# Инициализация текстовых полей для начального значения
on_option_change(None)

# Запуск главного цикла
root.mainloop()
