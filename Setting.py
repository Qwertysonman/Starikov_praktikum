import os

'''Cоздание новой папки для работы менеджера: '''

# Определение пути к рабочему столу пользователя
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Путь к новой папке на рабочем столе
folder_path = os.path.join(desktop_path, 'Folder_for_test')

# Создание папки на рабочем столе
os.makedirs(folder_path, exist_ok=True)



'''Задание пути существующей папки'''

# folder_path = 
