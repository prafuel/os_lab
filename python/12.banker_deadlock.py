def isSafe(processes, available, max, alloc, need, n, m, safeSeq):
    work = available[:]
    finish = [0] * n  # Initialize all processes as unfinished
    count = 0  # Count of finished processes

    while count < n:
        found = False
        for i in range(n):
            if finish[i] == 0:
                for j in range(m):
                    if need[i][j] > work[j]:
                        break
                else:  # All needs <= work
                    for x in range(m):
                        work[x] += alloc[i][x]
                    finish[i] = 1
                    safeSeq[count] = i
                    count += 1
                    found = True
        if not found:
            return False  # System is not in a safe state
    return True  # System is in a safe state


def main():
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resources: "))

    processes = list(map(int, input("Enter the process IDs: ").split()))
    available = list(map(int, input("Enter the available resources: ").split()))

    max = []
    print("Enter the maximum demand matrix:")
    for _ in range(n):
        max.append(list(map(int, input().split())))

    alloc = []
    print("Enter the allocation matrix:")
    for _ in range(n):
        alloc.append(list(map(int, input().split())))

    need = [[max[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

    safeSeq = [0] * n
    if isSafe(processes, available, max, alloc, need, n, m, safeSeq):
        print("System is in a safe state.\nSafe sequence:", end=" ")
        for i in range(n):
            print(processes[safeSeq[i]], end="")
            if i != n - 1:
                print(" -> ", end="")
        print()
    else:
        print("System is not in a safe state.")


if __name__ == "_main_":
    main()