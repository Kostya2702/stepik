# Как узнать сервер

# from requests import get
#
# responce = get('https://stepic.org/favicon.ico').headers['Server']
# print(responce)

# Декодирование урл кода в utf-8

# from urllib.parse import unquote
# resp = unquote("%D0%A3%D1%87%D0%B5%D0%BD%D1%8C%D0%B5%20-%20%D1%81%D0%B2%D0%B5%D1%82", encoding="utf-8")

# Первая задача 1.7

# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("0.0.0.0", 2222))
# s.listen(10)
# while True:
#     conn, addrs = s.accept()
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             break
#         if data == b'close':
#             conn.close()
#         conn.send(data)
#     conn.close()

# Вторая задача 1.7

# import socket
# import threading

# # Определение сокета и установка адреса
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(("0.0.0.0", 2222))
# # Количество слушателей в очереди
# s.listen(10)
#
# while True:
#     # Принимает акцепт когда соединение "тройное рукопожатие" установлено
#     conn, addrs = s.accept()
#     while True:
#         # Читает данные и отправляет их назад, потом обслуживает следующего клиента
#         data = conn.recv(1024)
#         thred = threading.Thread(args=(conn, addrs))
#         thred.start()
#         if not data:
#             break
#         if data == b'close':
#             conn.close()
#         conn.send(data)
#     conn.close()


# def mess():
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             break
#     conn.close()
#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('0.0.0.0', 2222))
# s.listen(10)
# print('Server started! Please waiting for connection')
#
# conn, addr = s.accept()
# print('Connection ', addr)
# t = threading.Thread(target=mess, args=(conn, addr))
# t.start()

import re

pattern = r'/(img+|css+|js+)/.*\..*'
strs = '123123123qweadas/img/1jpeg'
print(re.findall(pattern, strs))


