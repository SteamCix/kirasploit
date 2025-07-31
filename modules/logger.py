import threading

logs = []
logs_lock = threading.Lock()

def log_event(event):
    with logs_lock:
        logs.append(event)
        print(f"[LOG] {event}")

def get_logs():
    with logs_lock:
        return logs.copy()
