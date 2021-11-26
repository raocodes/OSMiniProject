def findWaitingTimeForAllProcesses(processes, n, bt, wait):
    wait[0] = 0
    for i in range(1, n):
        wait[i] = bt[i - 1] + wait[i - 1]


def findTurnAroundTimeForAllProcesses(processes, n, bt, wait, tat):
    for i in range(n):
        tat[i] = bt[i] + wait[i]


def findAverageTime(processes, n, bt):
    wait = [0] * n
    tat = [0] * n
    totalWaitingTime = 0
    total_tat = 0
    findWaitingTimeForAllProcesses(processes, n, bt, wait)
    findTurnAroundTimeForAllProcesses(processes, n, bt, wait, tat)

    print("Processes Burst time " + " Waiting time " + " Turn around time")

    for i in range(n):
        totalWaitingTime = totalWaitingTime + wait[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
              str(bt[i]) + "\t " + str(wait[i]) + "\t\t " + str(tat[i]))
    print("Average waiting time = "+str(totalWaitingTime / n))
    print("Average turn around time = "+str(total_tat / n))


if __name__ == "__main__":
    # process id's
    processes = [1, 2, 3]
    n = len(processes)
    # Burst time of all processes
    burst_time = [10, 5, 8]
    findAverageTime(processes, n, burst_time)
