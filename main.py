def lesson_2(*args):
    args = input("Введіть числа через пробіл: ").split(' ')
    args = [int(i)for i in args]
    print("Найбільше значення:" , max(args))
    print("Найменьше значення:" , min(args))
lesson_2()