import json

from datetime import datetime


def unpacking(filename):
    """Открываем файл Json"""
    try:
        with open(filename, encoding='utf-8') as file:
            data = json.load(file)
            info = 'Файл успешно открыт'
    except FileNotFoundError:
        data = None
        info = f"Ошибка. Файл {filename} не найден"
    return data, info


def get_filter(data, filtered_empy_from=False):
    """Фильтруем операции по значению 'EXECUTED' """
    data = [x for x in data if 'state' in x and x["state"] == "EXECUTED"]
    if filtered_empy_from:
        data = [x for x in data if 'from' in x]
    return data


def get_last(data, count_last):
    """Получем последние значения(поумолчанию 5)"""
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last]


def get_formatted_data(data):
    """Форматируем дату в нужный формат и подготавливаем информацию к выводу"""
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        sender = row['from'].split()
        sender_bill = sender.pop(-1)
        sender_bill = f'{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}'
        sender_info = ' '.join(sender)
        recipient = f'**{row["to"][-4:]}'
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
        formatted_data.append(f'{date} {description}\n{sender_info} {sender_bill} -> Счет {recipient}\n{amount}\n')
    return formatted_data