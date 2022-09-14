# 2. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы,
# с которыми вызвалась и возвращаемое значение с параметром – путь к логам.
from pprint import pprint
from datetime import datetime

def log(path):

    def log_call_func(call_func):
        def loging(*args, **kwargs):
            with open(path, 'a', encoding='utf-8') as file_general:
                result = call_func(*args, **kwargs)
                file_general.write(f'Дата вызова: {datetime.now()}')
                file_general.write('\n')
                file_general.write(f'Имя вызываемой функции: {call_func.__name__}')
                file_general.write('\n')
                file_general.write(f'Аргументы функции:')
                if len(args)>0:
                    for i in args:
                        file_general.write(str(i))
                        file_general.write(' ')
                    file_general.write('\n')
                if len(kwargs)>0:
                    for i in kwargs:
                        file_general.write(str(kwargs[i]))
                        file_general.write(' ')
                    file_general.write('\n')
                file_general.write(f'Результат  возврата функции {result}')
                file_general.write('\n')
                file_general.write('Конец вызова')
                file_general.write('\n')
                file_general.write('\n')
            return result
        return loging
    return log_call_func
