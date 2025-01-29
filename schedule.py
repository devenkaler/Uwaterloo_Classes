import json

schedule_location = 'schedule.json'

#adds class to schedule
def addSchedule(term, class_name):
    with open(schedule_location) as rf:
        data = json.load(rf)
    
    data[term].append(class_name)

    with open(schedule_location, 'w') as wf:
        json.dump(data, wf)

    print('Course added succesfully')


#removes class from schedule
def remSchedule(class_name):
    with open(schedule_location) as rf:
        data = json.load(rf)
    
    for t in data.keys():
        try: idx = data[t].index(str(class_name))
        except: break
        
        if idx != -1:
            data[t].pop(idx)

    with open(schedule_location, 'w') as wf:
        json.dump(data, wf)


#resets schedule
def resetSchedule():
    data  = {"1A": [], "1B": [], "2A": [], "2B": [], "3A": [], "3B": [], "4A": [], "4B": [], "5A": [], "5B": []}

    with open(schedule_location, 'w') as wf:
        json.dump(data, wf)


#displays schedule
def printSchedule():
    end = False
    idx = 0

    print('\n\n')

    with open(schedule_location) as rf:
        data = json.load(rf)

    for i in range(14*len(data.keys())): print('-',end='')
    print()

    for k in data.keys(): print('|     '+k+'     |',end='')
    print()
    for i in range(14*len(data.keys())): print('-',end='')
    print()

    while end == False:
        end = True
        for k in data.keys():
            if idx >= len(data[k]): 
                print('|            |',end='')
                continue

            print('|'+data[k][idx],end='')
            for i in range(12-len(data[k][idx])): print(' ',end='')
            print('|',end='')

            end = False

        idx += 1
        print()

    for i in range(14*len(data.keys())): print('-',end='')
    print('\n\n')
