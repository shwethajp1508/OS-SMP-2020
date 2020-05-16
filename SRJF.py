def waitingTime(p, n, bt, wt, at):  
    st = [0] * n  
    st[0] = 0
    wt[0] = 0
    for i in range(1, n):  
        st[i] = (st[i - 1] +bt[i - 1])   
        wt[i] = st[i] - at[i]  
        if (wt[i] < 0): 
            wt[i] = 0

def TAT(p, n, bt, wt, tat):  
    for i in range(n): 
        tat[i] = bt[i] + wt[i]  
    
def avgTime(p, n, bt, at):  
    wt = [0] * n 
    tat = [0] * n  
    waitingTime(p,n,bt,wt,at)
    TAT(p, n, bt, wt, tat)  
    total_wt = 0
    total_tat = 0
    for i in range(n): 
      total_wt = total_wt + wt[i]  
      total_tat = total_tat + tat[i]  
      tot_time = tat[i] + at[i]
  
    print("Average waiting time = %.5f "%(total_wt /n)) 
    print("\nAverage turn around time = ", total_tat / n)  



if __name__ =="__main__":  
    p = [1, 2, 3] 
    n = 3
    burst_time = [5, 9, 6]   
    arrival_time = [0, 3, 6]  
    avgTime(p, n, burst_time, arrival_time)