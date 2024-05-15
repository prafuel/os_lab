import threading
import time
import random

# Initialize semaphores and mutex
empty = threading.Semaphore(5)
full = threading.Semaphore(0)
mutex = threading.Lock()

buffer = [0] * 5
count = 0

def producer(num):
    global buffer, count
    empty.acquire()
    with mutex:
        buffer[count] = num * (random.randint(1, 1000))
        print(f"\n Producer {num + 1} produced: {buffer[count]}")
        print("\n")
        for i in buffer:
            print(i)
        count += 1
        time.sleep(1)
    full.release()

def consumer(num):
    global buffer, count
    full.acquire()
    with mutex:
        count -= 1
        print(f"\n Consumer {num + 1} consumed: {buffer[count]}")
        buffer[count] = 0
        print("\n")
        for i in buffer:
            print(i)
        time.sleep(1)
    empty.release()

def main():
    nt = int(input("Enter total number of threads to create: "))
    num_producer = nt // 2 + 1
    num_consumer = nt - num_producer

    producer_threads = []
    consumer_threads = []

    random.seed(time.time())
    
    for i in range(num_producer):
        thread = threading.Thread(target=producer, args=(i,))
        producer_threads.append(thread)
        thread.start()
        
    for i in range(num_consumer):
        thread = threading.Thread(target=consumer, args=(i,))
        consumer_threads.append(thread)
        thread.start()
        
    for thread in producer_threads:
        thread.join()
        
    for thread in consumer_threads:
        thread.join()

if __name__ == "__main__":
    main()
