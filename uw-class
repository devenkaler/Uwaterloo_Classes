import requests

API_KEY = #---API_KEY_HERE---
url = 'https://openapi.data.uwaterloo.ca/'

# MONTH YYYY (string)
def getTermCode(term):
    months = {'Winter': '1', 'Spring': '5', 'Fall': '9'}
    t = term.split()
    return '1'+t[1][2:]+months[t[0]]


def getClassSchedule(term_code, subject, cnum):
    r = requests.get(url+f'v3/ClassSchedules/{term_code}/{subject}/{cnum}', headers={'X-API-KEY': API_KEY})
    return r.json()


def getClass(sub, code):
    r = requests.get(url+f'v3/Courses/{1251}/{sub}/{code}', headers={'X-API-KEY': API_KEY})
    return r.json()

#returns class availability in even and odd years
def getClassAvailability(sub, code):
    start_year = 2023
    res = {'even': [], 'odd': []}
    for i in range(2):
        for s in ['Winter', 'Spring', 'Fall']:
            term = s + ' ' + str(start_year + i)
            if (type(getClassSchedule(getTermCode(term), sub, code)) == list):
                if (i == 1): res['even'].append(term[:1])
                else: res['odd'].append(term[:1])
                

    return res

#returns string of basic class info
def getClassInfo(class_name):
    c = class_name.split()
    sub = c[0]
    code = c[1]
    clss = getClass(sub, code)[0]
    res = ''

    res += 'NAME:        '+str(clss['title'])+'\n'
    res += 'OFFERED:     '+str(getClassAvailability(sub, code))+'\n'
    res += 'DESCRIPTION: '+str(clss['descriptionAbbreviated'])+'\n'
    reqs = str(clss['requirementsDescription']).replace('Prereq: ','-----prereq:').replace('Coreq: ','-----coreq:').replace('Antireq: ','-----antireq:').split('-----')
    for r in reqs:
        if (r.find('coreq') != -1): res += 'COREQ:       '+r.replace('coreq:','').replace(';','\nCOREQ:     ')+'\n'
        elif (r.find('prereq') != -1): res += 'PREREQ:      '+r.replace('prereq:','').replace(';','\nPREREQ:     ')+'\n'
        elif (r.find('antireq') != -1): res += 'ANTIREQ:     '+r.replace('antireq:','').replace(';','\nANTIREQ:     ')+'\n'

    LOAD = False

    return res

#outputs basic class info to terminal
def main():
    c = input('\nEnter Class (SUBJECT CLASSNUMBER) "q" to exit: ') #class name
    c  = c.upper()
    try:
        ci = getClassInfo(c).split('\n') #class info
    except:
        return c
    
    longest = len(max(ci, key=len))
    link = f"\x1b]8;;https://uwflow.com/course/{c.replace(' ','').lower()}/\x1b\\UWFLOW\x1b]8;;\x1b\\"

    print('\n\n')
    for n in range(longest+4): print('-',end='')
    print()

    print('|',end='')
    for n in range(int((longest-len(c)+2)/2)): print(' ',end='')
    print(c,end='')
    for n in range(int((longest-len(c)+2)/2)): print(' ',end='')
    print(' |')

    for n in range(longest+4): print('-',end='')
    print()

    for l in ci:
        print('| '+l,end='')
        for n in range(longest-len(l)): print(' ',end='')
        print(' |')

    print('| '+link,end='')
    for n in range(longest-len('UWFLOW')): print(' ',end='')
    print(' |')

    for n in range(longest+4): print('-',end='')

    print('\n\n')

    return c

if __name__ == '__main__':
    while main() != 'Q': pass
