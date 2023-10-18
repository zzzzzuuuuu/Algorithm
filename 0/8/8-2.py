def solution(age):
    answer = ''
    alpha = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    if 0 < age < 10:
        answer = alpha.get(age%10)
    elif 10 <= age < 100:
        answer = alpha.get(age//10) + alpha.get(age%10)
    elif 100 <= age < 1000:
        answer = alpha.get(age//100) + alpha.get((age - age//100*100)//10) + alpha.get((age%100)%10)
    else: answer = 'baaa'
    return answer

# 또 다른 풀이
def solution2(age):
    age = str(age)
    age = age.replace("0", "a")
    age = age.replace("1", "b")
    age = age.replace("2", "c")
    age = age.replace("3", "d")
    age = age.replace("4", "e")
    age = age.replace("5", "f")
    age = age.replace("6", "g")
    age = age.replace("7", "h")
    age = age.replace("8", "i")
    age = age.replace("9", "j")
    return age

def solution3(age):
    dict = {'0':'a','1':'b','2':'c','3':'d','4':'e'
            ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
    return ''.join(dict[i] for i in str(age))