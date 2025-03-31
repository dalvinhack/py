#!/usr/bin/env python
# -*- coding: utf-8 -*-

from routeros_api import RouterOsApiPool

# Подключение к MikroTik
connection = RouterOsApiPool(
    host='192.168.1.1',  # IP-адрес MikroTik
    username='admin',     # Имя пользователя
    password='',          # Пароль
    plaintext_login=True  # Использовать plaintext login (не рекомендуется для production)
)

# Получение API
api = connection.get_api()

# Выполнение команды "interface print"
interfaces = api.get_resource('/interface').get()

# Вывод результатов
for interface in interfaces:
    print(f"Interface: {interface.get('name')}, Type: {interface.get('type')}, Status: {interface.get('running')}")

# Закрытие соединения
connection.disconnect()
