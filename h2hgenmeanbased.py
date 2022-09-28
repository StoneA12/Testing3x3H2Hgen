import random

l = int(input("people?"))
psychsheet = []
people = []
times = []
for i in range (0,l):
    o = input("psych?")
    t = o.split("	")
    psychsheet.append([t[1],t[4]])
    
for i in range (0,l-(l%3)):
    o = psychsheet[i]
    people.append(o[0])
    times.append(float(o[1]))

avg = sum(times)*3/len(times)
print("Average team result: " + str(avg))
taken = []
while len(taken)/4 < l/3:
    bestdif = 100
    for one in range (0,l):
        if(people[one] not in taken):
            for two in range (1,l):
                    if(two != one) and (people[two] not in taken):
                        for three in range (2,l):
                            if(three != one) and (three != two) and (people[three] not in taken):
                                if abs((times[one]+times[two]+times[three])-avg)<bestdif:
                                    bestdif = abs((times[one]+times[two]+times[three])-avg)
                                    bestcombo = [one, two, three]
    taken.append(people[bestcombo[0]])
    taken.append(people[bestcombo[1]])
    taken.append(people[bestcombo[2]])
    taken.append(times[bestcombo[0]]+times[bestcombo[1]]+times[bestcombo[2]])

for i in range(1,l//3+1):
    print("Team " + str(i) + ":" + str(taken[0]) + ", " + str(taken[1]) + ", " + str(taken[2]) + ". Expected time: " + str(taken[3]))
    taken.pop(0)
    taken.pop(0)
    taken.pop(0)
    taken.pop(0)
