import time

def fcfs_scheduling(processes):
    n = len(processes)
    wait_time = [0] * n
    turnaround_time = [0] * n
    total_wait_time = 0
    total_turnaround_time = 0

    
    for i in range(1, n):
        wait_time[i] = processes[i - 1][1] + wait_time[i - 1] - processes[i][0] + processes[i - 1][0]

    
    for i in range(n):
        turnaround_time[i] = processes[i][1] + wait_time[i]

    
    for i in range(n):
        total_wait_time += wait_time[i]
        total_turnaround_time += turnaround_time[i]

    
    avg_wait_time = total_wait_time / n
    avg_turnaround_time = total_turnaround_time / n

    return avg_wait_time, avg_turnaround_time, wait_time, turnaround_time

def main():
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append((arrival_time, burst_time))

    avg_wait_time, avg_turnaround_time, wait_time, turnaround_time = fcfs_scheduling(processes)

    print(f"\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(num_processes):
        print(f"{i + 1}\t{processes[i][0]}\t\t{processes[i][1]}\t\t{wait_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_wait_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

    
    current_time = 0
    while current_time < sum([p[1] for p in processes]):
        time.sleep(1)
        current_time += 1

    
    print("\nProcess Representation:")
    for i in range(num_processes):
        print(f"{wait_time[i]}[P{i + 1}]{turnaround_time[i]}", end=" -> " if i < num_processes - 1 else "\n")

if __name__ == "__main__":
    main()
