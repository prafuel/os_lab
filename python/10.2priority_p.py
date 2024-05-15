def preemp_priority():
    print("Enter the number of processes: ")
    n = int(input())

    pid = [i + 1 for i in range(n)]
    at = []
    bt = []
    ct = [0] * n
    ta = [0] * n
    wt = [0] * n
    f = [0] * n
    k = []
    priority = []

    for i in range(n):
        at.append(int(input(f"Enter arrival time for process {i + 1}: ")))
        bt.append(int(input(f"Enter burst time for process {i + 1}: ")))
        k.append(bt[i])
        f.append(0)
        priority.append(int(input(f"Enter priority for process {i + 1}: ")))

    st = 0
    tot = 0

    while True:
        min_priority = 999
        c = -1  # Initialize 'c' to an invalid index
        if tot == n:
            break

        for i in range(n):
            if at[i] <= st and f[i] == 0 and priority[i] < min_priority:
                min_priority = priority[i]
                c = i  # Store the index of the process with the highest priority

        if c == -1:
            st += 1
        else:
            bt[c] -= 1
            st += 1
            if bt[c] == 0:
                ct[c] = st
                f[c] = 1
                tot += 1

    for i in range(n):
        ta[i] = ct[i] - at[i]
        wt[i] = ta[i] - k[i]

    print("\nPid|Arrival| Burst |Complete | Turn|Waiting")
    for i in range(n):
        print(f"{pid[i]}\t{at[i]}\t{k[i]}\t{ct[i]}\t{ta[i]}\t{wt[i]}")

if __name__ == "__main__":
    preemp_priority()
