import threading
import time

NUM_PHILOSOPHERS = 5
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

def philosopher(id):
    left_fork = id
    right_fork = (id + 1) % NUM_PHILOSOPHERS

    while True:
        # Think
        print(f"Philosopher {id} is thinking.")

        # Pick up forks
        forks[left_fork].acquire()
        forks[right_fork].acquire()

        # Eat
        print(f"Philosopher {id} is eating.")

        # Put down forks
        forks[left_fork].release()
        forks[right_fork].release()

if __name__ == "__main__":
    philosophers = []

    for i in range(NUM_PHILOSOPHERS):
        philosopher_thread = threading.Thread(target=philosopher, args=(i,))
        philosophers.append(philosopher_thread)
        philosopher_thread.start()

    for philosopher_thread in philosophers:
        philosopher_thread.join()
