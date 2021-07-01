from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

import csv
import random

with open('Egyptian_gods.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)

question_ans = random.choice(data)

question = question_ans[1]
answer = question_ans[0]

print("Question: ", question)
print("Answer: ", answer)