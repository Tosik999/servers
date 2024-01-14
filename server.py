import socket

# Создаем сокет TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Указываем IP-адрес и порт сервера
server_address = ("127.0.0.1", 12345)

# Привязываем серверный сокет к заданному адресу и порту
server_socket.bind(server_address)

# Начинаем прослушивание входящих подключений
server_socket.listen(1)

print("Сервер запущен и ожидает подключений...")

while True:
    # Ждем подключений
    client_socket, client_address = server_socket.accept()
    print("Подключение от:", client_address)

    # Получаем данные от клиента
    data = client_socket.recv(1024).decode()
    print("Получено сообщение от клиента:", data)

    # Отправляем ответ клиенту
    response = "Привет от сервера!"
    client_socket.send(response.encode())

    # Закрываем соединение с клиентом
    client_socket.close()
