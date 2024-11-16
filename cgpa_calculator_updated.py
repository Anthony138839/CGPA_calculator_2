
import pandas as pd

# Putting the courses, course unit and the scores entered by the user into their respective lists 

course_list = []
unit_list = []
score_list = []
n = int(input("Enter number of courses offered: "))
for i in range(n):
    courses = input(f"Course {i + 1}: ").upper()
    units = int(input(f"Unit for {courses}: "))
    scores = int(input(f"Score for {courses}: "))
    print()
    
    course_list.append(courses)
    unit_list.append(units)
    score_list.append(scores)
    
# Merging the three lists into one list using list comprehension 

result = [[i, j, k] for i, j, k in zip(course_list, unit_list, score_list)]

# Putting the merged list of lists in a dataframe using pandas for manipulation 

df = pd.DataFrame(result, columns = ["COURSE", "UNIT", "GRADE"])
print(df)
print()

# Calculating the total course units, total course points and the cgpa

total_course_unit = 0
total_course_point = 0

for index, item in df.iterrows():
    score = item["GRADE"]
    unit = item["UNIT"]
    if score >= 70:
        point = 4 * unit
    elif 60 <= score < 70:
        point = 3 * unit
    elif 50 <= score < 60:
        point = 2 * unit
    elif 45 <= score < 50:
        point = 1 * unit
    else:
        point = 0 * unit
        
    total_course_unit += unit
    total_course_point += point
    
print(f"Total course unit = {total_course_unit}")
print(f"Total course point = {total_course_point}")

# Rounding off tht cgpa to 2 decimal places

cgpa = round((total_course_point / total_course_unit), 2)
print(f"CGPA: {cgpa}")

