# ДЗ 1_1 - формат времени

duration = int(input('Введите длительность: '))

days = duration // 86400
hrs = (duration % 86400) // 3600
mins = ((duration % 86400) % 3600) // 60
secs = duration % 60

print(days, 'дн', hrs, 'ч', mins, 'мин', secs, 'сек')

#end
