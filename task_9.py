print('Задача 8. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
#
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
#
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBBGBBG
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
children_row = ''

# if (boys > girls * 2) or (girls > boys * 2):
  # print('Нет решения')
# else:
  # if boys == girls:
    # for i in range(boys + girls):
      # if boys > 0:
        # children_row += 'B'
        # boys -= 1
      # if girls > 0:
        # children_row += 'G'
        # girls -= 1
  # elif boys < girls:
    # for i in range(boys + girls):
      # if girls > boys * 2:
        # children_row += 'G'
        # girls -= 1
      # if girls > 0:
        # children_row += 'G'
        # girls -= 1
      # if boys > 0:
        # children_row += 'B'
        # boys -= 1
  # else:
    # for i in range(boys + girls):
      # if boys > girls * 2:
        # children_row += 'B'
        # boys -= 1
      # if boys > 0:
        # children_row += 'B'
        # boys -= 1
      # if girls > 0:
        # children_row += 'G'
        # girls -= 1
  # print(children_row)

if (boys > girls * 2) or (girls > boys * 2):
  print('Нет решения')
elif boys >= girls:
  k = boys - girls
  for bgb in range(k):
    children_row += 'BGB'
  for bg in range(girls - k):
    children_row += 'BG'
else:
  k = girls - boys
  for gbg in range(k):
    children_row += 'GBG'
  for gb in range(boys - k):
    children_row += 'GB'
print(children_row)