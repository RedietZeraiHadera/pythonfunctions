def my_country(country="Rwanda"):
    print(f"Hello from {country}")
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

def concatenate_args(*args):
    
    result = ""
    for arg in args:
        result += arg
    return result


def concatenate_kwargs(**kwargs):
    result=""
    for key,value in kwargs.items():
        result+=value
    return result 