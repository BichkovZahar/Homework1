def lesson_4(*args):
    dictionary = []
    args = input("Введіть значення через пробіл: ").split(' ')
    args = [int(i) for i in args]
    for rezult in args:
      if rezult % 2 != 0:
          dictionary.append(rezult)
    return dictionary
print(lesson_4())