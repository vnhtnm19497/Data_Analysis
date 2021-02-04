import matplotlib.pyplot as plt
import numpy as np

with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

total_students = len(students)
#split header 
header = header.split(",")
subjects = header[5:]
#split students
for i in range(len(students)):
    students[i] = students[i].split(",")
    
not_take_exam = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#loop through all student
for s in students:
    for i in range(5,16):
        if s[i] == "-1":
            not_take_exam[i-5] += 1

not_take_exam_percentage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(11):
    not_take_exam_percentage[i] = round((not_take_exam[i] / total_students)*100, 2)
# Barchart
fig, ax = plt.subplots()
y_pos = np.arange(len(subjects))

plt.bar(y_pos, not_take_exam_percentage)
plt.xticks(y_pos,subjects)
ax.set_ylim(0,100)
plt.title('Biểu đồ số học sinh không đăng kí hoặc bỏ thi THPT quốc gia 2020 tại TPHCM theo môn học')
plt.ylabel('Percentage')
rects = ax.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')
plt.show()

#Number of students who took 0,1,2,3,... subjects 
num_of_exam_taken = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
average = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
for s in students:
    count = 0
    total = 0
    for i in range(11):
        if s[i+5] != "-1":
            total += float(s[i+5])
            count += 1

    num_of_exam_taken[count] += 1
    average[count] += total/count

for i in range(12):
    if num_of_exam_taken[i] != 0:
        average[i] = round(average[i]/num_of_exam_taken[i], 2)

print(average)

#Pie chart
labels = '0 môn', '1 môn', '2 môn', '3 môn', '4 môn', '5 môn', '6 môn', '7 môn', '8 môn', '9 môn', '10 môn', '11 môn' 
sizes = num_of_exam_taken

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Biểu đồ biểu diễn số lượng học sinh theo số môn thi')
plt.legend(loc='best')
plt.show()

#Barchart_average_score
x = np.arange(12)
y = np.arange(12)

fig, ax = plt.subplots()
plt.bar(x, average)
plt.xticks(x,y)
ax.set_ylim(0,10)
plt.title('Biểu đồ điểm trung bình theo số lượng môn thi')
plt.xlabel('Số lượng môn thi của thí sinh')
plt.ylabel('Điểm trung bình')
rects = ax.patches
labels = average
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')
plt.show()

#Classification students by age
#Year of birth: 2003 2002 2001 ... 1994 <= 1993
num_of_student_per_age_group = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
avg_of_student_per_age_group = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for s in students:
    age = 2020 - int(s[4])
    if age >= 27:
        age = 27
    num_of_student_per_age_group[age - 17] += 1

#Calculate sum score 
    sum_score = 0 
    count_score = 0
    for i in range(11):
        if s[i+5] != "-1":
            count_score += 1
            sum_score += float(s[i+5])

    average = sum_score/count_score
    avg_of_student_per_age_group[age - 17]  += average 

for i in range(len(avg_of_student_per_age_group)):
    avg_of_student_per_age_group[i] = avg_of_student_per_age_group[i]/num_of_student_per_age_group[i]

#Scale up in chart
for i in range(len(avg_of_student_per_age_group)):
    avg_of_student_per_age_group[i] = avg_of_student_per_age_group[i] * 7000

x = np.arange(11)
y = np.arange(11)
age_label = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, ">26"]
fig, ax = plt.subplots()
plt.bar(x, num_of_student_per_age_group)
plt.plot(x, avg_of_student_per_age_group, color='r', marker='o')
plt.xticks(x,age_label)
ax2 = ax.twinx()
ax2.ticks_params('y', color='r')
ax2.set_ylim(0,10)
ax2.ylabel('Điểm trung bình')
ax.set_ylim(0,70000)
plt.title('Biểu đồ điểm trung bình theo số lượng môn thi')
plt.xlabel('Tuổi')
ax.ylabel('Số học sinh')
rects = ax.patches
labels = num_of_student_per_age_group
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height, label, ha='center', va='bottom')
plt.show()


#Bar chart to find the most popular last name in examination
last_name = [] 
last_name_count = []

for s in students:
    s_name = s[1].split(" ")
    lastname = s_name[0]
    if lastname not in last_name:
        last_name.append(lastname)
        last_name_count.append(0)
        last_name_count[last_name.index(lastname)] += 1
    else:
        last_name_count[last_name.index(lastname)] += 1

#Find max in list last_name_count
counted_max_num = [] #Number of repetitions of each last name  
sort_index = [] #Number of last name's positions after were sorted

for i in last_name_count:
    max = 0
    for j in range(len(last_name)):
        if last_name_count[j] > max and last_name_count[j] not in counted_max_num:
            max = last_name_count[j]

    counted_max_num.append(max)

for max_num in counted_max_num:
    for i in range(len(last_name)):
        if last_name_count[i] == max_num and i not in sort_index:
            sort_index.append(i)

last_name_sorted = [] #List of each last name have been sorted
last_name_count_sorted = [] # List of the number of repetitions of each last name have been sorted

#Using sort_index for arrange 
for index in sort_index:
    last_name_sorted.append(last_name[index])
    last_name_count_sorted.append(last_name_count[index])

num = 20
x = np.arange(num)
y = np.arange(num)

fig, ax = plt.subplots()
plt.bar(x, last_name_count_sorted[0:num])
plt.xticks(x, last_name_sorted[0:num])
ax.set_ylim(0,25000)
plt.title('Biểu đồ ' + str(num) +  ' họ phổ biến nhất trong kì thi THPT năm 2020 tại TPHCM')
plt.xlabel('Các họ phổ biến nhất')
plt.ylabel('Số lượng thí sinh')
rects = ax.patches
labels = last_name_count_sorted[0:num]
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height+2, label, ha='center', va='bottom')
plt.show()
