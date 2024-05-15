import threading
import time

BUFFER_SIZE = 5
buffer = [None] * BUFFER_SIZE
in_index = 0
out_index = 0

# Conditions to handle empty and filled states of the buffer
condition = threading.Condition()

def producer():
    global in_index
    item = 1
    while True:
        with condition:
            while (in_index + 1) % BUFFER_SIZE == out_index:
                condition.wait()  # Buffer is full, wait for the consumer to consume
            
            buffer[in_index] = item
            print(f"Producer produced: {item}")
            in_index = (in_index + 1) % BUFFER_SIZE
            
            condition.notify()  # Notify the consumer that there's an item to consume
        item += 1
        time.sleep(1)  # Added sleep to slow down production for demonstration

def consumer():
    global out_index
    while True:
        with condition:
            while in_index == out_index:
                condition.wait()  # Buffer is empty, wait for the producer to produce
            
            item = buffer[out_index]
            print(f"Consumer consumed: {item}")
            out_index = (out_index + 1) % BUFFER_SIZE
            
            condition.notify()  # Notify the producer that there's space to produce
        time.sleep(2)  # Added sleep to slow down consumption for demonstration

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
