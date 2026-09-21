# Баннер-граббер
# Подключается к порту и читает баннер сервиса.
# Запуск: python banner_grabber.py 127.0.0.1 22

import socket
import sys

TIMEOUT = 3
BUFFER_SIZE = 1024


def grab_banner(host, port):
    """Читает баннер с порта."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        sock.connect((host, port))
        banner = sock.recv(BUFFER_SIZE)
        sock.close()

        if banner:
            print(f"Баннер {host}:{port}:\n")
            print(banner.decode("utf-8", errors="ignore").strip())
        else:
            print(f"Порт {port} открыт, но баннер пустой")

    except ConnectionRefusedError:
        print(f"Порт {port} закрыт")
    except socket.timeout:
        print(f"Таймаут подключения к {host}:{port}")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        host, port = "127.0.0.1", 22
        print("Аргументы не указаны, использую значения по умолчанию.\n")

    grab_banner(host, port)