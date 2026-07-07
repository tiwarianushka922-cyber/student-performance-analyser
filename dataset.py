import numpy as np
def load_data():
    data = np.genfromtxt(
        "exams.csv",
        delimiter=",",
        dtype=str,
        skip_header=1
    )
    marks = data[:, -3:]
    marks = np.char.strip(marks, '"')
    marks=marks.astype(int)
    students = np.arange(1,len(data)+1)

    subjects = ["Maths", "OOPS", "CP"]

    return students, marks, subjects,data
