def lesson_3(*args):
    dictionary = {}
    args = input("Введіть значення чере з пробіл: ").split(' ')
    args = [int(i) for i in args]
    for rezult in args:
        dictionary[rezult] = rezult**2
    print(dictionary)
lesson_3()