
from dataset import load_data
from analysis import *

students, marks, subjects,data = load_data()

total = total_marks(marks)
avg = average_marks(marks)

top = topper(total)
low = lowest_scorer(total)

sub_avg = subject_average(marks)

print("\nTopper Student ID:", students[top])
print("Topper Total Marks:", total[top])

print("\nLowest Scorer Student ID:", students[low])
print("Lowest Total Marks:", total[low])

print("\nSubject Averages:")
for i in range(len(subjects)):
    print(subjects[i], ":", sub_avg[i])
students, marks, subjects, data = load_data()

print("\nTopper Details:")
print(data[top])

print("\nLowest Scorer Details:")
print(data[low])