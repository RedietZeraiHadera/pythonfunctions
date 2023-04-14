def add(a,b):
    answer1= a+b
    return answer1
def subtract(c,d):
    answer2= c-d
    return answer2
def divide(e,f):
    answer3=e/f
    return answer3
def multiply(g,h):
    answer4= g*h
    return answer4
def modulus(i,j):  
    answer5=i%j
    return answer5
def sum(*numbers):
    answer = 0
    for number in numbers:
        answer+=number
    return answer 
def multiply1(*numbers):
    answer1 = 1
    for numb in numbers:
        answer1+=numb
    return answer1   

