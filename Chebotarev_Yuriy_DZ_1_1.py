"""Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

print('конвертер секунд v1')

duration = 400153
minutes = duration // 60
hours = duration // 3600
days = duration // 86400

if duration < 60:
    time = f'{duration} сек'
elif duration < 3600:
    time = f'{minutes} мин {(duration - (minutes * 60))} сек'
elif duration < 86400:
    time = f'{hours} час {minutes - (hours * 60)} мин {duration - (minutes * 60)} сек'
else:
    time = f'{days} дн {hours - (days * 24)} час {minutes - (hours * 60)} мин {duration - (minutes * 60)} сек'
print(time, '\n')

print('конвертер секунд v2')
duration_list = [53, 153, 4153, 400153, 40000153]
idx = 0
for index in duration_list:
    minutes = duration_list[idx] // 60
    hours = duration_list[idx] // 3600
    days = duration_list[idx] // 86400
    if duration_list[idx] < 60:
        time = f'{duration_list[idx]} сек'
        print(f'Ответ а. до минуты: {time}')
    elif duration_list[idx] < 3600:
        time = f'{minutes} мин {(duration_list[idx] - (minutes * 60))} сек'
        print(f'Ответ b. до часа:   {time}')
    elif duration_list[idx] < 86400:
        time = f'{hours} час {minutes - (hours * 60)} мин {duration_list[idx] - (minutes * 60)} сек'
        print(f'Ответ c. до суток:  {time}')
    else:
        time = f'{days} дн {hours - (days * 24)} час {minutes - (hours * 60)} мин {duration_list[idx] - (minutes * 60)} сек'
        print(f'Ответ d. до суток:  {time}')
    idx += 1
