# Uwaterloo_Classes


This python scripts searches uw classes using the official University of Waterloo open AI

To use the program, replace #---API_KEY_HERE--- with your api key, which you can configure [here](https://openapi.data.uwaterloo.ca/api-docs/index.html)

```python3 uw-class-search``` begins the program

## Details
The script will return:

name - title of the course

offered - which terms the course is  offered in (even/ odd years)

description - brief description of the course

prereq - prerequisits

coreq - corequisites

antireq - antirequisites

UWFLOW - link to UWFLOW page for the course

## Example
```python3 uw-class-search```

```Enter Class (SUBJECT CLASSNUMBER) "q" to exit: math 235```


```
-----------------------------------------------------------------------------------------------------------------------------
|                                                         MATH 235                                                          |
-----------------------------------------------------------------------------------------------------------------------------
| NAME:        Linear Algebra 2 for Honours Mathematics                                                                     |
| OFFERED:     {'even': ['W', 'S', 'F'], 'odd': ['W', 'S', 'F']}                                                            |
| DESCRIPTION: Linear Algebra 2 (Honours)                                                                                   |
| PREREQ:      (MATH 106 or 114 or 115 with a grade of at least 70%) or (MATH 136 with a grade of at least 60%) or MATH 146 |
| PREREQ:      Honours Mathematics or Mathematical Physics students.                                                        |
| COREQ:       MATH 128 or 138 or 148.                                                                                      |
| ANTIREQ:     MATH 225, 245                                                                                                |
|                                                                                                                           |
| UWFLOW                                                                                                                    |
-----------------------------------------------------------------------------------------------------------------------------
