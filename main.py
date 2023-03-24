from faker import Faker
from random import randint

fake = Faker()

a = []
b = []
c = []

for _ in range(100):
    b.append(randint(40000, 70000))


for _ in range(100):
    a.append(fake.name())

for _ in range(100):
    c.append(randint(20, 100))


Salary_list = [[]for _ in a]


for j, val in enumerate(a):
    Salary_list[j].append(val)
for k, val in enumerate(b):
    Salary_list[k].append(val)
for i, val in enumerate(c):
    Salary_list[i].append(val)
print(Salary_list)



