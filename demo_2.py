#new project time
#lets get started with it !
#how hard can it even be to model covid
import random
import numpy as np
import matplotlib.pyplot as plt


#the next line helps us simulate probability of an infection event 
#print(random.uniform(0,100))

class STUDENTS:
    def __init__(self,susceptible,infectious,recov_time,still_infected):
        self.susceptible = susceptible
        self.infectious = infectious
        self.recov_time = recov_time
        self.still_infected = still_infected
  
no_of_students = 1800
all_students = []
for i in range(no_of_students):
    all_students.append(STUDENTS(True,False,-1,False))

#marking 0.5% of the incoming students as covid carriers

for i in range(9):
    x = random.randrange(no_of_students)
    all_students[x].susceptible = False
    all_students[x].infectious = True
    all_students[x].recov_time = 0
    all_students[x].still_infected = True

        
#assuming 1800 students in LBS hall and 600 rooms where 3 people live
#initially we assume there to be no contact between each rooms

adj_graph = {}
infected_students = []

for i in range(no_of_students):
    adj_graph[i] = []
    if i%3==0:
        adj_graph[i].append(i+1)
        adj_graph[i].append(i+2)
    if i%3==1:
        adj_graph[i].append(i-1)
        adj_graph[i].append(i+1)
    if i%3==2:
        adj_graph[i].append(i-1)
        adj_graph[i].append(i-2)

#going hour by hour in our simulation

#I'm assuming for now every hour 30 random students from different rooms come
#into contact with each other

#within a room I'm assuming there's a 10% probabilty with proper precautions
#that every time someone comes in contact with someone else
#there's an infection event

#I'll write the actual functions to calculate more accurate infection
#probabilities later on
        
#roomates are pretty much guaranteed to catch covid

for i in range(no_of_students):
    if all_students[i].infectious == True:
        for j in adj_graph[i]:
            all_students[j].infectious = True
            all_students[j].recov_time = 0
            all_students[j].susceptible = False
            all_students[j].still_infected = True

            
##for i in range(no_of_students):
##    if all_students[i].infectious==True:
##        print(i)
##
##print()
##print()
##print()
            
count = []
count2 = []
conta_no = 30
Time = 2*720 #30 days
for i in range(Time):
    #creating the 30 random contacts
    y_1 = []
    y_2 = []
    for j in range(conta_no):
        y_1.append(random.randrange(no_of_students))
        y_2.append(random.randrange(no_of_students))
        adj_graph[y_1[j]].append(y_2[j])
        adj_graph[y_2[j]].append(y_1[j])
        

    #starting a massive BFS-y search
    for l in range(no_of_students):
        if all_students[l].infectious==True:
            all_students[l].recov_time += 1
            for k in adj_graph[l]:
                if all_students[k].susceptible==True:
                    if random.uniform(0,100) < 10:
                        all_students[k].infectious = True
                        all_students[k].susceptible = False
                        all_students[k].recov_time = 0
                        all_students[k].still_infected = True
                        
        if all_students[l].still_infected==True and all_students[l].infectious==False:
            all_students[l].recov_time +=1
            
        #assuming after 5 days they show symptoms and get quarantined            
        if all_students[l].recov_time > 140:
            all_students[l].infectious = False
            all_students[l].susceptible = False

        if all_students[l].recov_time > 360:
            all_students[l].still_infected = False
    count_1 = 0
    count_2 = 0
    for m in range(no_of_students):
        if all_students[m].infectious==True:
            count_1 +=1

    for m in range(no_of_students):
        if all_students[m].still_infected==True:
            count_2 +=1

    count.append(count_1)
    count2.append(count_2)
        
    for j in range(conta_no):
        adj_graph[y_1[j]].remove(y_2[j])
        adj_graph[y_2[j]].remove(y_1[j])

x_1 = [i for i in range(Time)]

print(count)                
##for i in range(no_of_students):
##    if all_students[i].infectious==True:
##        print(i)

plt.plot(x_1,count,label='infected and present in campus')
plt.plot(x_1,count2,"-r",label='infected total')
plt.xlabel("Number of hours passed")
plt.ylabel("Active cases in LBS")
plt.legend(loc=1)
plt.show()
        

    

    

    
        


    
    




    
