# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы,
# с которыми вызвалась и возвращаемое значение.

from datetime import datetime
from path_file import PATH

def log_call_func(call_func):
    def loging(*args, **kwargs):
        with open(PATH, 'a', encoding='utf-8') as file_general:
            result = call_func(*args, **kwargs)
            file_general.write(f'Дата вызова: {datetime.now()}')
            file_general.write('\n')
            file_general.write(f'Имя вызываемой функции: {call_func.__name__}')
            file_general.write('\n')
            file_general.write(f'Аргументы функции:')
            for i in args:
                file_general.write(i)
                file_general.write(' ')
            file_general.write('\n')
            for i in kwargs:
                file_general.write(kwargs[i])
                file_general.write(' ')
            file_general.write('\n')
            file_general.write(f'Результат  возврата функции {result}')
            file_general.write('\n')
            file_general.write('Конец вызова')
            file_general.write('\n')
            return result
    return loging

@log_call_func
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    return (arguments, keywords)

word = ("It's very runny, sir.",
        "It's really very.",
        "VERY runny, sir.")
kword = {'shopkeeper' : "Michael Palin",
        'client':"John Cleese",
        'sketch':"Cheese Shop Sketch"}

if __name__ == "__main__":
    result = cheeseshop("Limburger", *word, **kword)
    print(result)