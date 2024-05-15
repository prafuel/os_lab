import threading
import time

NUM_PHILOSOPHERS = 5

forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]
philosophers = []

def philosopher(id):
    left_fork = id
    right_fork = (id + 1) % NUM_PHILOSOPHERS

    while True:
        # Think
        print(f"Philosopher {id} is thinking.")
        time.sleep(1)  # Simulate thinking

        # Pick up forks
        forks[left_fork].acquire()
        forks[right_fork].acquire()

        # Eat
        print(f"Philosopher {id} is eating.")
        time.sleep(1)  # Simulate eating

        # Put down forks
        forks[left_fork].release()
        forks[right_fork].release()

def main():
    for i in range(NUM_PHILOSOPHERS):
        t = threading.Thread(target=philosopher, args=(i,))
        philosophers.append(t)
        t.start()

    for t in philosophers:
        t.join()

if __name__ == "__main__":
    main()
