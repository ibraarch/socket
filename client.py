# TCP-клиент
# Подключается к серверу и отправляет сообщения.
# Запуск: python client.py

import socket

HOST = "127.0.0.1"
PORT = 9090
BUFFER_SIZE = 1024


def start_client():
    """Запускает клиент."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"Подключение к {HOST}:{PORT} установлено")
        print("Введите сообщение (или 'exit' для выхода)\n")

        while True:
            message = input("Сообщение: ")
            if message.lower() == "exit":
                break

            client.send(message.encode("utf-8"))
            response = client.recv(BUFFER_SIZE).decode("utf-8")
            print(f"Ответ сервера: {response}\n")

    except ConnectionRefusedError:
        print(f"Сервер {HOST}:{PORT} недоступен. Запусти server.py первым.")
    finally:
        client.close()
        print("Соединение закрыто")


if __name__ == "__main__":
    start_client()