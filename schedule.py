import json

schedule_location = 'schedule.json'

#adds class to schedule
def addSchedule(term, class_name):
    with open(schedule_location) as rf:
        data = json.load(rf)
    
    data[term].append(class_name)

    with open(schedule_location, 'w') as wf:
        json.dump(data, wf)


#removes class from schedule
def remSchedule(class_name):
    with open(schedule_location) as rf:
        data = json.load(rf)
    
    for t in data.keys():
        if (len(data[t]) == 0): break
        idx = data[t].index(str(class_name))
        if idx != -1:
            data[t].pop(idx)

    with open(schedule_location, 'w') as wf:
        json.dump(data, wf)


#resets schedule
def resetSchedule():
    data  = {"A1": [], "A2": [], "B1": [], "B2": [], "C1": [], "C2": [], "D1": [], "D2": [], "E1": [], "E2": []}

    with open(schedule_location, 'w') as wf:
        json.dump(data, wf)


#displays schedule
def printSchedule():
    end = False
    idx = 0

    print('\n\n')

    with open(schedule_location) as rf:
        data = json.load(rf)

    for i in range(10*len(data.keys())): print('-',end='')
    print()

    for k in data.keys(): print('|   '+k+'   |',end='')
    print()

    while end == False:
        end = True
        for k in data.keys():
            if idx >= len(data[k]): 
                continue

            print('|'+data[k][idx],end='')
            for i in range(8-len(data[k][idx])): print(' ',end='')
            print('|',end='')

            end = False

        idx += 1

    print('\n\n')
