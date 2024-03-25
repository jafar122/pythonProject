print('Вы проснулись.')
def bedroom():
  print('Вы в спальне. Варианты:')
  print('1 - в ванну')
  print('2 - в коридор')
  chouse = int(input('Куда идем? '))
  if chouse == 1:
    bath()
  elif chouse == 2:
    corridor()


def corridor():
  print('Вы в коридоре. Варианты:')
  print('1 - в спальню')
  print('2 - в ванну')
  print('3 - в на кухню')
  print('4 - в дверь')
  chouse = int(input('Куда идем? '))
  if chouse == 1:
    bedroom()
  elif chouse == 2:
    bath()
  elif chouse == 3:
    kitchen()
  elif chouse == 4:
    door()


def bath():
  print('Вы в ванне. Варианты:')
  print('1 - в спальню')
  print('2 - в коридор')
  chouse = int(input('Куда идем? '))
  if chouse == 1:
    bedroom()
  elif chouse == 2:
    corridor()


def kitchen():
  print('Вы на кухне. Варианты:')
  print('1 - в коридор')
  print('2 - в окно')
  chouse = int(input('Куда идем? '))
  if chouse == 1:
    corridor()
  elif chouse == 2:
    print('Вы упали с 5 этажа =(')


def door():
  ('Вы вышли из дома.')


bedroom()