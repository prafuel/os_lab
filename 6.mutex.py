import threading
import time

resource_mutex = threading.Lock()
readers_count_mutex = threading.Lock()
shared_resource = 0
readers = 0

def reader(id):
    global shared_resource, readers
    print(f"Reader {id} is trying to read")
    with readers_count_mutex:
        readers += 1
        if readers == 1:
            resource_mutex.acquire()  # Lock the resource for the first reader
    # Reading the shared resource
    print(f"Reader {id} read: {shared_resource}")
    time.sleep(1)
    with readers_count_mutex:
        readers -= 1
        if readers == 0:
            resource_mutex.release()  # Unlock the resource when the last reader is done

def writer(id):
    global shared_resource
    print(f"Writer {id} is trying to write")
    resource_mutex.acquire()
    # Writing to the shared resource
    shared_resource = id
    print(f"Writer {id} wrote: {shared_resource}")
    resource_mutex.release()

def main():
    num_readers = 4
    num_writers = 3

    reader_threads = []
    writer_threads = []

    for i in range(num_readers):
        reader_thread = threading.Thread(target=reader, args=(i+1,))
        reader_thread.start()
        reader_threads.append(reader_thread)

    for i in range(num_writers):
        writer_thread = threading.Thread(target=writer, args=(i+1,))
        writer_thread.start()
        writer_threads.append(writer_thread)

    for reader_thread in reader_threads:
        reader_thread.join()

    for writer_thread in writer_threads:
        writer_thread.join()

if __name__ == "__main__":
    main()
