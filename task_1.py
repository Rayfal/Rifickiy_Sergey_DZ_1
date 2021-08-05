#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#до минуты: <s> сек;
#до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
#* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#duration = 53
#53 сек
#duration = 153
#2 мин 33 сек
#duration = 4153
#1 час 9 мин 13 сек
#duration = 400153
#4 дн 15 час 9 мин 13 сек

duration = int(input('Введите число: '))
while duration <= 60:
    print(f'{duration / 60} сек')
if duration > 60 and duration <= 360:
    print(f'{duration // 60} мин {duration % 60} сек')
elif duration >= 3600 and duration < 86400:
    duration_hour = duration // 3600
    duration_minute = ((duration - 3600) // 60) % 60
    duration_sek = (duration - 3600) % 60
    print(f'{duration_hour} час {duration_minute} мин {duration_sek} сек')
elif duration >= 86400:
    duration_day = duration // 86400
    duration_hour = ((duration - 86400) % 86400) % 60
    duration_minute = ((duration - 3600) // 60) % 60
    duration_sek = (duration - 3600) % 60
    print(f'{duration_day} день {duration_hour} час {duration_minute} мин {duration_sek} сек')
