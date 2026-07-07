import numpy as np

def total_marks(marks):
    return np.sum(marks, axis=1)


def average_marks(marks):
    return np.mean(marks, axis=1)


def topper(total):
    return np.argmax(total)


def lowest_scorer(total):
    return np.argmin(total)


def subject_average(marks):
    return np.mean(marks, axis=0)