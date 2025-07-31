import socket
import threading
from modules.logger import log_event

clients = []

def handle_client(client_socket, addr):
    log_event(f"Bağlantı alındı: {addr[0]}:{addr[1]}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            command = data.decode().strip()
            if command.lower() == 'exit':
                break
            log_event(f"{addr[0]}:{addr[1]} komut gönderdi: {command}")
            client_socket.send(b"Komut alindi\n")
        except:
            break
    client_socket.close()
    log_event(f"Bağlantı kapandı: {addr[0]}:{addr[1]}")
    clients.remove(client_socket)

def start_listener(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    log_event(f"Listener {port} portunda dinlemeye başladı...")
    try:
        while True:
            client_socket, addr = server.accept()
            clients.append(client_socket)
            thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            thread.start()
    except KeyboardInterrupt:
        server.close()
        log_event("Listener durduruldu.")
