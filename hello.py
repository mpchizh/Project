guest = ['косой', 'хромой', 'сиплый']
print(f"Привет {guest[0].title()},приглашаю тебя на день рождение!") # Косой
print(f"Привет {guest[1].title()},приглашаю тебя на день рождение!") # Хромой
print(f"Привет {guest[2].title()},приглашаю тебя на день рождение!") # Сиплый
print(f"К сожалению {guest[0].title()},приехать не сможет.")
guest[0] = 'лысый'
print(guest)
print(f"Привет {guest[0].title()},приглашаю тебя на день рождение!") # Лысый
print(f"Привет {guest[1].title()},приглашаю тебя на день рождение!") # Хромой
print(f"Привет {guest[2].title()},приглашаю тебя на день рождение!") # Сиплый
extension_list = 'Я заказал стол и могу пригласить еще парочку гостей.'
print(extension_list)
guest.insert(0, 'кривой')
guest.insert(2, 'конченый')
guest.append('глухой')
print(f"Привет {guest[0].title()},приглашаю тебя на день рождение!") # Кривой
print(f"Привет {guest[1].title()},приглашаю тебя на день рождение!") # Лысый
print(f"Привет {guest[2].title()},приглашаю тебя на день рождение!") # Конченый
print(f"Привет {guest[3].title()},приглашаю тебя на день рождение!") # Хромой
print(f"Привет {guest[4].title()},приглашаю тебя на день рождение!") # Сиплый
print(f"Привет {guest[5].title()},приглашаю тебя на день рождение!") # Глухой
print(guest[0])
print(guest[1])
print(guest[2])
print(guest[3])
print(guest[4])
print(guest[5])
cut_list = 'К сожалению на пьянку могу позвать только двоих.'
print(cut_list)
no_alco = 'прости не могу позвать тебя на синеву(('

not_list = guest.pop()
print(f'{guest[0].title()} {no_alco}')
not_list = guest.pop()
print(f'{guest[1].title()} {no_alco}')




