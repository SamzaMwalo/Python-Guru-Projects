"""
STUDENT MARK ANALYSER
Goal: Analyse marks using lists, loops, conditions, dictionary etc
Problem Statement:
    -Store students marks
    -Calculate totals and average
    -Find highest and lowest marks
    -Count pass and fail students
Let: Pass Marks = 40
     Marks out of 100
"""

#storing data
students = {"Samwel":34, "Benjamin":78, "Stanley":91, "Grace":80, "Felister":75}

#initialisation of variables
total = 0
highest = -1
lowest = 101
highest_scorer =""
lowest_scorer =""
pass_count = 0
fail_count = 0

#analysis of marks
for name, marks in students.items():
    total = total + marks
    if marks > highest: 
        
        highest = marks
        highest_scorer = name
    if marks < lowest:
        lowest = marks
        lowest_scorer = name
    if marks >= 40:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

#calculating average
average = total / len(students)  #here "len" is a python in-built feature that returns the number of items in a given situation eg The no. of student for this case

#displaying the final results
print("Total students:", len(students))
print("Total marks:", total)
print("Average marks:", average)
print("Highest marks:",highest, "by",highest_scorer)
print("Lowest marks:",lowest, "by",lowest_scorer)
print("Pass count:", pass_count)
print("Fail count:", fail_count)


"""
ASSIGNMENT
-Take marks using input
-Change pass marks
-Add grade logic A B C Fail
-Store marks in list instead of dict
"""






