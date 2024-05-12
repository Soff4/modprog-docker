import platform
import psutil

def get_system_info():
    system_info = {}

    # Отримати версію операційної системи
    system_info['os_version'] = platform.platform()
    
    # Отримати інформацію про процесор
    system_info['processor'] = platform.processor()
    
    # Отримати кількість ядер процесора
    system_info['num_cores'] = psutil.cpu_count(logical=False)
    
    # Отримати кількість логічних ядер процесора
    system_info['num_threads'] = psutil.cpu_count(logical=True)
    
    # Отримати обсяг доступної пам'яті
    memory_info = psutil.virtual_memory()
    system_info['total_memory'] = round(memory_info.total / (1024 ** 3), 2)  # Переведення в гігабайти

    return system_info

# Викликати функцію для отримання інформації про систему
system_info = get_system_info()
for info in system_info:
    print(system_info[info])
    print("\n Оновлено для перевірки докера!")
