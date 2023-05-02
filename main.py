def lesson_1(*args):
    args = input('Введіть текст: ')
    if not args:
        return 0
    return ' , '.join(finish for finish in args)
print(lesson_1())