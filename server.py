# TCP-сервер (эхо)
# Принимает сообщения и отправляет обратно.
# Запуск: python server.py

import socket

HOST = "127.0.0.1"
PORT = 9090
BUFFER_SIZE = 1024


def start_server():
    """Запускает сервер."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Сервер запущен на {HOST}:{PORT}")
    print("Ожидание клиента...\n")

    conn, addr = server.accept()
    print(f"Подключился клиент: {addr}\n")

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break

        message = data.decode("utf-8")
        print(f"Получено: {message}")

        response = f"Эхо: {message}"
        conn.send(response.encode("utf-8"))
        print(f"Отправлено: {response}\n")

    conn.close()
    server.close()
    print("Соединение закрыто")


if __name__ == "__main__":
    start_server()