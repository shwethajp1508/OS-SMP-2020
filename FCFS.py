def waitingTime(p,n,wt,bt): 
    wt[0] = 0
    for i in range(1, n ): 
        wt[i] = bt[i - 1] + wt[i - 1]  
def TAT(p,n,wt,bt,tat): 
    for i in range(n): 
        tat[i] = bt[i] + wt[i] 
def avgTime( p,n,bt):
    wt = [0] * n 
    tat = [0] * n  
    total_wt = 0
    total_tat = 0
    waitingTime(p,n,wt,bt) 
    TAT(p,n,wt,bt,tat) 
    for i in range(n): 
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
    print( "Average waiting time = "+ str(total_wt / n)) 
    print("Average turn around time = "+str(total_tat / n)) 



if __name__ =="__main__": 
     
    proc = [1,2,3,4] 
    n = len(proc) 
    burst_time = [21,3,6,2] 
  
    avgTime(proc,n,burst_time)