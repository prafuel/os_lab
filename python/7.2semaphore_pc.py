import threading

bs = 8
es = threading.Semaphore(bs)
fs = threading.Semaphore(0)
buffer = [None] * bs
in_index = 0
out_index = 0

def producer():
    item = 1
    while True:
        print(f"Produced item: {item}")

        es.acquire()

        global in_index
        buffer[in_index] = item
        in_index = (in_index + 1) % bs

        fs.release()

        item += 1

def consumer():
    while True:
        fs.acquire()

        global out_index
        consumed = buffer[out_index]
        print(f"Consumed item: {consumed}")

        out_index = (out_index + 1) % bs

        es.release()

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
