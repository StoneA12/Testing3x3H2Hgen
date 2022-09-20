import random

l = int(input("people?"))
n = int(input("team size?"))
psychsheet = []
people = []
times = []
for i in range (0,l):
    o = input("psych?")
    t = o.split("	")
    psychsheet.append([t[1],t[4]])
    
for i in range (0,l-(l%n)):
    o = psychsheet[i]
    people.append(o[0])
    times.append(float(o[1]))


for i in range (0, (l-(l%n))//n):
    p = []
    psum = 0
    for a in range (i*n, i*n+n):
        p.append(people[a])
        psum+=(times[a])
    print("Team", i+1, ":", p, "Expected time:", psum)


