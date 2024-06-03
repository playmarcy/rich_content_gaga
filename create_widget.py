from content import content_1, content_2, content_3

def create_widget(content_number: int) -> str:
    content = eval(f'content_{content_number + 1}')
    return content
