# Порт-сканнер
import socket
import sys

TIMEOUT = 0.5  # таймаут подключения (сек)

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP"
}


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0


def scan(host, start, end):
    print(f"Сканирование {host} ({start}-{end})\n")
    found = 0

    for port in range(start, end + 1):
        if scan_port(host, port):
            service = COMMON_PORTS.get(port, "unknown")
            print(f"[+] Порт {port} открыт ({service})")
            found += 1

    print(f"\nНайдено открытых портов: {found}")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        host = sys.argv[1]
        start = int(sys.argv[2])
        end = int(sys.argv[3])
    else:
        host, start, end = "127.0.0.1", 1, 1024
        print("Аргументы не указаны, использую значения по умолчанию.\n")

    scan(host, start, end)