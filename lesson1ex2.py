user_time = int(input("Здравствуйте.Введите время в секундах"))

hours = user_time // 3600
remainder_hours = user_time % 3600
minutes = remainder_hours // 60
seconds = remainder_hours % 60

print(f"Введенное Вами количество секунд в формате 'чч:мм:сс' выглядит так: '{hours:02}:{minutes:02}:{seconds:02}'")