print (not(5>10))

name="쿠키"
animal="강아지"
age=4
hobby="산책"
is_adult = age>=3 

#age값이 3 이상이면 true, 미만이면 false
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")

#age가 숫자 자료형이기 때문에 , 문자열 자료형을 뜻하는 str에 괄호를 붙이고
#안에 age라는 숫자 자료형 변수를 넣었다. 형 변환.

print(name + "는 어른일까요? " + str(is_adult))

#지금까지는 ‘문자열 + 변수 + 문자열’ 같은 형태로 변수를 사용했는데 + 대신 쉼표를 사용할 수도 있습니다. 이때 기억할 점은 두 가지입니다.
#str() 같은 형변환을 사용하지 않아도 된다.
#, 를 사용하면 값과 값 사이에 공백이 하나 포함된다.

# 수정 후
print(name, "는 ", age, "살이며, ", hobby, "(을)를 아주 좋아해요")

#은 파이썬에서 주석 처리이다. 작은따옴표 3개로 ``` 여러줄 주석 가능함.
# 주석 단축키 ctrl+ 또는 Ctrl + k + c

station = '사당'
print(station , '행 열차가 들어오고 있습니다')

#숫자 처리 함수

# abs (절대값)
# pow (제곱)
# max(가장 큰 값)
# min (가장 작은 값)
# round (반올림)
print(abs(-5)) # -5 의 절대값 = 5
print(pow(4, 2)) # 4의 2제곱 = 4 * 4 = 16
print(max(5, 12)) # 5 와 12 중 큰 값 = 12
print(min(5, 12)) # 5 와 12 중 작은 값 = 5
print(round(3.14)) # 3.14 의 반올림 = 3
print(round(4.99)) # 4.99 의 반올림 = 5

from math import * # math 모듈 내의 모든 내용을 가져다 쓰겠다는 의미

print(floor(4.99)) # 4.99 의 내림 = 4
print(ceil(3.14)) # 3.14 의 올림 = 4
print(sqrt(16)) # 16 의 제곱근 = 4