from dataclasses import dataclass
from datetime import *
import threading
import concurrent.futures

@dataclass()
class NewQuestion():
    text: str = 'some text'
    explanation: str = 'some explanation'
    is_true: bool = True

nq = NewQuestion('first question','answer')
#print(nq.text)

nq2 = NewQuestion()
nq2.text = 'second question'
nq2.is_true = False
nq2.explanation = 'xplntn'

#print(nq2.explanation)

class Question():
    def __init__(self, text, is_true, explanation):
        self.text = text
        self.is_true = is_true
        self.explanation = explanation




s = 0
num = 101
while num > 0:
    s += num % 10
    num = num // 10
print(s)

num = 101
lst = [x for x in range(1, num)]
print(sum(lst))

# from string import printable
# from random import *
#
# password = []
# for i in range(9):
#    x = choice(printable)
#    if x != ' ':
#        password.append(x)
#    else:
#        password.append('2')
# new_pass = ''.join(password)
# print(new_pass)

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in lst:
    for j in i:
        print(j, end=' ')
    print()

for i in range(3):
    for j in range(3):
        print(lst[i][j ], end=' ')
    print()

lst2 = []
#num1 = int(input('num of rows: '))
#num2 = int(input('num of stolbs: '))
#
#for i in range(num1):
#    lst2.append('*'*num2)
#
#for i in lst2:
#    print(i)

def printing_the_matrix():
    lst3 = []
    hm = int(input('hom much? '))

    for i in range(hm):
        lst3.append([0]*hm)

    for i in range(hm):
        for j in range(hm):
            if i==j:
                lst3[i][j] = 10
            elif i < j:
                lst3[i][j] = 5
            else:
                lst3[i][j] = 3

    for i in lst3:
        print(i)

def show_time_deco(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start, f'{func.__name__}')
        return result
    return wrapper

@show_time_deco
def making_list_by_cycle(n):
    lst = []
    for i in range(1, n):
        if i % 2 == 0:
            lst.append(i)
    return lst

@show_time_deco
def making_lst_by_generator(n):
    lst = [x for x in range(1, n) if x % 2 == 0]
    return lst

func1 = making_list_by_cycle(100001)
func2 = making_lst_by_generator(100001)
