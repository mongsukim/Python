# 2021.11.29
# 4-3. 문자열 처리 함수 

#함수이름 | 의미
# lower 소문자로 변환
# upper 대문자로 변환
# isupper 대문자인지 확인
# islower 소문자인지 확인
# replace 문자열 바꾸기
# index 찾으려는 문자열의 인덱스(없으면 에러)
# find 찾으려는 문자열의 인덱스(없으면 -1)
# count 문자열이 나온 횟수 

## 문자열 처리함수는 모두 python.으로 시작하는데, 
## 문자열의 길이 정보를 확인해주는 len()함수는 사용법이 조금 다르다. 

python = "Python is Amazing"

print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True : 0 번째 인덱스의 값이 대문자인지 확인
print(len(python)) # 17 : 띄어쓰기를 포함한 문자열의 전체 길이 (length)
print(python.replace("Python", "Java")) # Java is Amazing


print('-------------------------')
## 문자열 내에 어떤 문자가 어느 위치에 있는지를 확인하기 위한 함수는 index() 와 find() 가 있다.
index = python.index("n") # 처음으로 발견된 n 의 인덱스
print(index) # 5 : Python 의 n
index = python.index("n", index + 1) # 6 번째 인덱스 이후에 처음으로 발견된 n 의 인덱스 
print(index) # 15 : Amazing 의 n

find = python.find("n") # 처음으로 발견된 n 의 인덱스
print(find) # 5 : Python 의 n
find = python.find("n", find + 1) # 6 번째 인덱스 이후에 처음으로 발견된 n 의 인덱스 
print(find) # 15 : Amazing 의 n


##index() 와 find() 는 비슷한 역할을 하지만 만약 찾으려는 문자열이 없는 경우에는 동작이 달라집니다. 
##index() 사용 시 에러가 발생하면 이후의 문장은 실행되지 않고 프로그램이 종료된다.

#print(python.index("Java"))
print(python.find("Java"))

##찾으려는 문자열이 총 몇 번 사용되었는지도 확인할 수 있습니다. 만약 사용되지 않았다면 결과는 0 이 된다.

print(python.count("n")) # 2 : 문자열 내에서 n 이 나온 횟수

print('-------------------------')
