#5-1. 리스트

#리스트를 사용하는 방법 : 대괄호 속에 원하는 값들을 콤마로 구분하여 넣어준다.

subway = ['유재석','조세호','박명수']
print(subway)

# 몇 번째 칸에 있는지 확인하려면 index()함수 이용.
print(subway.index('조세호'))

# append() 리스트의 맨 마지막에 데이터를 추가
subway.append('하하')
print(subway)

# insert() 인덱스 값을 이용해 중간에 삽임
subway.insert(1,'정형돈')
print(subway)

# pop() 맨 뒤에 있는 데이터를 하나씩 뺀다.
print(subway.pop()) # 하하 내림
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석") # 설명을 위해 유재석씨를 맨 뒤에 태운다.
print(subway) # ['유재석', '정형돈', '유재석']
print(subway.count("유재석")) # 유재석씨가 2명이 있다.

#숫자 예제
num_list = [5, 2, 4, 3, 1]

#sort() 함수를 이용하면 오름차순으로 정렬
print(num_list)
num_list.sort() # 정렬
print(num_list)

#reverse() 를 이용하여 거꾸로 뒤집기
num_list.reverse() # 순서 뒤집기
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) # []

mix_list = ["조세호", 20, True] # 다양한 자료형을 함께 사용할 수 있어요
print(mix_list) 

#서로 다른 리스트를 확장
num_list = [5, 2, 4, 3, 1] # num_list 값 다시 정의
num_list.extend(mix_list) # 리스트 확장
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]



### 5-2 . 사전
# 사전은 key 와 value 가 쌍으로 이루어져 있다.

# 먼저 사전 형태의 사물함인 cabinet 을 정의하고 
# 유재석씨에게는 3번 사물함 열쇠를, 김태호씨에게는 100번 사물함 열쇠를 준다.
cabinet = {3: "유재석", 100: "김태호"}

# 각 사물함이 누구 것인지 확인 해보기. 
#  대괄호 속에 key 값을 넣음으로써 key 에 해당하는 value 를 가져올 수 있습니다.

print(cabinet[3]) # 유재석 -> key 3 에 해당하는 value
print(cabinet[100]) # 김태호 -> key 100 에 해당하는 value

# 대괄호가 아닌 get() 을 이용하는 방법.
print(cabinet.get(3)) # 유재석 -> key 3 에 해당하는 value

print(cabinet[5]) # key 가 5 인 값이 없을 땐 에러 발생 후 프로그램 종료 (hi 출력 안됨)
print("hi")

print(cabinet.get(5)) # key 가 5 인 값이 없을 땐 None 반환 후 계속 진행 (hi 출력됨)
print("hi")

# 사전 자료형에 값이 있는지 여부 확인
print(3 in cabinet)  # True
print(5 in cabinet)  # False

# key 는 정수형이 아닌 문자열도 가능
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호