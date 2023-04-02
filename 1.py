
def data_recording(file):
    '''функция записывает данные в файл'''
    text = input('Введите данные для записи в файл:\n'
                 'Для окончания нажмите Enter:\n>>> ')
    while text:
        file.write(text + '\n')
        text = input('Введите данные для записи в файл:\n'
                     'Для окончания нажмите Enter:\n>>> ')


with open('file/output_file.txt', 'w') as f:
    data_recording(f)