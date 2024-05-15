import threading
import time

# Initialize mutexes and shared variables
db_mutex = threading.Lock()
x_mutex = threading.Lock()
reader_count = 0

def reader(reader_id):
    global reader_count
    with x_mutex:
        reader_count += 1
        if reader_count == 1:
            db_mutex.acquire()
    
    # Critical section
    print(f"Reader {reader_id} entered db")
    print(f"Reader {reader_id} is reading...")
    time.sleep(1)  # Simulate reading

    with x_mutex:
        reader_count -= 1
        if reader_count == 0:
            db_mutex.release()

def writer(writer_id):
    db_mutex.acquire()
    # Critical section
    print(f"Writer {writer_id} entered db")
    print(f"Writer {writer_id} is writing...")
    time.sleep(1)  # Simulate writing
    print(f"Writer {writer_id} exited from db")
    db_mutex.release()

if __name__ == "__main__":
    readers = []
    writers = []

    for i in range(5):
        r_thread = threading.Thread(target=reader, args=(i,))
        w_thread = threading.Thread(target=writer, args=(i,))
        readers.append(r_thread)
        writers.append(w_thread)

    for r_thread, w_thread in zip(readers, writers):
        r_thread.start()
        w_thread.start()

    for r_thread, w_thread in zip(readers, writers):
        r_thread.join()
        w_thread.join()
