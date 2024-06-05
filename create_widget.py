from content import content_1, content_2, content_3


def create_widget(content_number: int) -> str:
    content = eval(f'content_{content_number}')
    for i in range(len(content['blocks'])):
        image_link = input(f'Вставьте ссылку на изображение из блока {i+1}:  ')
        content['blocks'][i]['img']['src'] = image_link
        content['blocks'][i]['img']['srcMobile'] = image_link
        content['blocks'][i]['imgLink'] = input(f'Вставьте ссылку на озон продукт:  ')
        content['blocks'][i]['title']['content'] = [input(f'Напишите название игры из блока {i+1}:  ')]
    return content
