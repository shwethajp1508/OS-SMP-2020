n=int(input("Enter number of processes:"))
bt=[0]
p=[0,0,0,0,0,0,0,0,0,0,0]
wt=[0,0,0,0,0,0,0,0,0,0,0]
tat=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,n):
    bt.append(int(input("Enter burst time for process {} :").format(i)))
for i in range(n):
    for j in range(i+1,n):
        if bt[i]>bt[j]:
            temp=bt[i]
            bt[i]=bt[j]
            bt[j]=temp

            tmp=p[i]
            p[i]=p[j]
            p[j]=tmp

wt[0]=0
tat[0]=bt[0]
avg_wt=0
avg_tat=0
for i in range(1,n):
    wt[i]=wt[i-1]+bt[i-1]
    tat[i]=tat[i-1]+bt[i]
for i in range(1,n):  
    avg_wt=(avg_wt+wt[i])
    avg_tat=(avg_tat+tat[i])
tot_wt=avg_wt/n
tot_tat=avg_tat/n
print("Avg waiting time ="+ str(tot_wt))
print("Avg turn around time ="+ str(tot_tat))