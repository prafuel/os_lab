import threading

db = threading.Semaphore(1)
x = threading.Semaphore(1)
reader_count = 0

def reader(reader_id):
    global reader_count
    x.acquire()
    reader_count += 1
    print(f"Reader {reader_id} entered db")
    if reader_count == 1:
        db.acquire()
    print(f"Reader {reader_id} is reading...")
    x.release()

    x.acquire()
    reader_count -= 1
    print(f"Reader {reader_id} exited from db")
    if reader_count == 0:
        db.release()
    x.release()

def writer(writer_id):
    db.acquire()
    print(f"Writer {writer_id} entered db")
    print(f"Writer {writer_id} is writing...")
    db.release()
    print(f"Writer {writer_id} exited from db")

if __name__ == "__main__":
    readers = []
    writers = []

    for i in range(5):
        reader_thread = threading.Thread(target=reader, args=(i,))
        writer_thread = threading.Thread(target=writer, args=(i,))
        readers.append(reader_thread)
        writers.append(writer_thread)

    for reader_thread, writer_thread in zip(readers, writers):
        reader_thread.start()
        writer_thread.start()

    for reader_thread, writer_thread in zip(readers, writers):
        reader_thread.join()
        writer_thread.join()
