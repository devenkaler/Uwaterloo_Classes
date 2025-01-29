# Uwaterloo_Classes


This python scripts searches uw classes using the official University of Waterloo open AI

Ability to schedule future classes while focusing on past prereq/ antireq

To use the program, replace #---API_KEY_HERE--- with your api key, which you can configure [here](https://openapi.data.uwaterloo.ca/api-docs/index.html)

##  Run

Install requests module:

```pip install requests```

```python3 uw-class-search``` begins the program

## Commands
Enter class (SUBJECT CLASS-CODE) - display class info

h - help

q - quit

v - view current schedule

r - reset current schedule

q - quit

## Class Details
When searching for a class, the script will return:

name - title of the course

offered - which terms the course is  offered in (even/ odd years)

description - brief description of the course

prereq - prerequisits

coreq - corequisites

antireq - antirequisites

UWFLOW - link to UWFLOW page for the course

## Example
```python3 uw-class-search```

```
Enter Class "q" to exit "h" for help: amath 250



----------------------------------------------------------------------------------------------------------
|                                               AMATH 250                                                |
----------------------------------------------------------------------------------------------------------
| NAME:        Introduction to Differential Equations                                                    |
| OFFERED:     {'even': ['W', 'S', 'F'], 'odd': ['W', 'S', 'F']}                                         |
| DESCRIPTION: Intro Differential Equations                                                              |
| PREREQ:      (One of MATH 106, 114, 115, 136, 146, NE 112) and (One of MATH 118, 119, 128, 138, 148).  |
| ANTIREQ:     AMATH 251, 350, MATH 218, 228                                                             |
|                                                                                                        |
| UWFLOW                                                                                                 |
----------------------------------------------------------------------------------------------------------


Alter Schedule? (a - add, r - remove): a
Enter term: 3A
Course added succesfully

Enter Class "q" to exit "h" for help: v



--------------------------------------------------------------------------------------------------------------------------------------------
|     1A     ||     1B     ||     2A     ||     2B     ||     3A     ||     3B     ||     4A     ||     4B     ||     5A     ||     5B     |
--------------------------------------------------------------------------------------------------------------------------------------------
|MATH 135    ||MATH 136    ||CLAS 104    ||AMATH 231   ||AMATH 250   ||            ||            ||            ||            ||            |
|CS 135      ||CS 136      ||MATH 235    ||CO 250      ||            ||            ||            ||            ||            ||            |
|COMMST 100  ||MATH 138    ||MATH 237    ||PHYS 121    ||            ||            ||            ||            ||            ||            |
|PHIL 145    ||CS 136L     ||MATH 239    ||STAT 231    ||            ||            ||            ||            ||            ||            |
|MATH 137    ||ECON 101    ||STAT 230    ||CS 246      ||            ||            ||            ||            ||            ||            |
|            ||MUSIC 240   ||            ||            ||            ||            ||            ||            ||            ||            |
|            ||PD 1        ||            ||            ||            ||            ||            ||            ||            ||            |
|            ||            ||            ||            ||            ||            ||            ||            ||            ||            |
--------------------------------------------------------------------------------------------------------------------------------------------
