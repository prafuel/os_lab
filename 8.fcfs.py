def find_waiting_time(n, bt, at):
    wt = [0] * n
    wt[0] = 0  # Waiting time for the first process is 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1] - at[i]
        if wt[i] < 0:
            wt[i] = 0
    return wt

def find_turnaround_time(n, bt, wt):
    tat = [0] * n
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    return tat

def find_finish_time(n, at, bt):
    ft = [0] * n
    ft[0] = at[0] + bt[0]
    for i in range(1, n):
        if at[i] > ft[i - 1]:
            ft[i] = at[i] + bt[i]
        else:
            ft[i] = ft[i - 1] + bt[i]
    return ft

def main():
    n = int(input("Enter the number of processes: "))
    burst_time = []
    arrival_time = []
    print("Enter the burst time and arrival time for each process:")
    for i in range(n):
        bt, at = map(int, input(f"Process {i + 1}: ").split())
        burst_time.append(bt)
        arrival_time.append(at)

    waiting_time = find_waiting_time(n, burst_time, arrival_time)
    turnaround_time = find_turnaround_time(n, burst_time, waiting_time)
    finish_time = find_finish_time(n, arrival_time, burst_time)

    print("Process\tBurst Time\tArrival Time\tFinish Time\tTurnaround Time\tWaiting Time")
    for i in range(n):
        print(f"{i + 1}\t{burst_time[i]}\t\t{arrival_time[i]}\t\t{finish_time[i]}\t\t{turnaround_time[i]}\t\t\t{waiting_time[i]}")

if __name__ == "__main__":
    main()
