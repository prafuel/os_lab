import random

class Process:
    def _init_(self, pid, bt, at):
        self.pid = pid
        self.bt = bt
        self.at = at
        self.rt = bt
        self.ft = 0
        self.tat = 0
        self.wt = 0

def sort_processes(processes):
    return sorted(processes, key=lambda x: (x.at, x.bt))

def count_iteration(processes, tq):
    total = 0
    for p in processes:
        total += (p.bt + tq - 1) // tq  # Ceiling division
    return total

def execute(processes, tq):
    t = 0
    execution = []
    while processes:
        for i, p in enumerate(processes):
            if p.rt > 0:
                bt = min(tq, p.rt)
                p.rt -= bt
                t += bt
                p.ft = t
                execution.append(p)
                if p.rt == 0:
                    processes.pop(i)
    return execution, t

def print_chart(execution):
    print("\n\t+", end="")
    for p in execution:
        print("-" * p.bt, end="+")
    print("\n\t|", end="")
    for p in execution:
        print(" P%d" % p.pid, end="")
        print(" " * (p.bt - 1), end="|")
    print("\n\t+", end="")
    for p in execution:
        print("-" * p.bt, end="+")
    print("\n\t", execution[0].at, end="")
    for p in execution:
        print(" " * p.bt, end="")
        print(p.ft, end="")
    print()

def print_table(processes):
    avg_wt = sum(p.wt for p in processes) // len(processes)
    avg_tat = sum(p.tat for p in processes) // len(processes)
    print("\n\n\tpid\tAt\tBt\tFt\tTAt\tWt\n")
    for p in processes:
        print("\t%d\t%d\t%d\t%d\t%d\t%d" % (p.pid, p.at, p.bt, p.ft, p.tat, p.wt))
    print("\n\n\tAverage waiting time: %d units\n\tAverage turn-around time: %d units" % (avg_wt, avg_tat))

def main():
    n = int(input("\n\tEnter the total number of processes: "))
    tq = int(input("\n\tEnter the time quantum: "))

    processes = []
    for i in range(n):
        at = int(input("\n\tProcess %d:\n\tArrival time: " % (i + 1)))
        bt = int(input("\tBurst time: "))
        processes.append(Process(i + 1, bt, at))

    processes = sort_processes(processes)
    u = count_iteration(processes, tq)
    execution, t = execute(processes, tq)
    for i, p in enumerate(execution):
        p.wt = p.ft - p.at - p.bt
        p.tat = p.ft - p.at

    print_table(processes)
    print("\n\n\tGnatt chart\n")
    print_chart(execution)

    upbt, lowbt = 4, 1
    s = t + 2
    m = int(input("\n\n\n\t\t\tRandom CPU Burst\n\n\tEnter the total number of processes: "))
    random_processes = []
    for i in range(m):
        rand_at = s
        s += 1
        rand_bt = random.randint(lowbt, upbt)
        random_processes.append(Process(i + 1, rand_bt, rand_at))

    random_processes = sort_processes(random_processes)
    v = count_iteration(random_processes, tq)
    random_execution, t = execute(random_processes, tq)
    for i, p in enumerate(random_execution):
        p.wt = p.ft - p.at - p.bt
        p.tat = p.ft - p.at

    print_table(random_processes)
    print("\n\n\tGnatt chart\n")
    print_chart(random_execution)

    print("\n\n\n\tCombined Gnatt chart\n")
    print_chart(execution)
    print("\n\n\t\t--IO of 2 units--\n")
    print_chart(random_execution)

if __name__ == "__main__":
    main()