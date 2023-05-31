#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
if len(sys.argv) != 1:
    file = sys.argv[1]
else:
    file = 'students.txt'

# 출력을 위한 틀
def start():
    print("Student\t\t\tName\t\t\tMidterm\t\tFinal\t\tAverage\t\tGrade")
    print("-------------------------------------------------------------------------------------------------------")

# 학생 출력    
def show_function(slist):
    start()
    slist.sort(key=lambda x: x[4], reverse = True) #학생 평균을 내림차순정렬
    for i in slist:
        for j in i:
            print(j, end='\t\t')
        print()
    print()

# 학생 검색        
def search_function(slist):
    s_id = input("Student ID: ")
    found = False # 초기값으로 False 할당
    for i in slist:
        if s_id == i[0]: # 학생 ID가 일치하는 경우
            found = True # found 변수를 True로 변경
            start()
            for j in i:
                print(j, end='\t\t')
            print()
    if not found: # 검색 결과가 없는 경우
        print("NO SUCH PERSON.\n")

# 학점 변경            
def changescore_function(slist):
    s_id = input("Student ID: ")
    found = False
    for i in slist:
        if s_id == i[0]:
            found = True
            is_exam = input("Mid/Final? ").lower()
            if is_exam != 'mid' and is_exam != 'final':
                return # 'mid' 또는 'final' 외의 값이 입력된 경우 실행되지 않음
            new_score = int(input("Input new score: "))
            if new_score < 0 or new_score > 100:
                return # 0~100 외의 값이 입력된 경우 실행되지 않음
            start()
            for j in i:
                print(j, end='\t\t')
            print()
            print('Score changed.')
            
            if is_exam == 'mid':
                i[2] = new_score
            else:
                i[3] = new_score
            i[4] = (i[2] + i[3]) / 2  # 평균 계산
            if i[4] >= 90:
                i[5] = 'A'
            elif i[4] >= 80:
                i[5] = 'B'
            elif i[4] >= 70:
                i[5] = 'C'
            elif i[4] >= 60:
                i[5] = 'D'
            else:
                i[5] = 'F'
            for j in i:
                print(j, end='\t\t')
            print()
            return
    if not found:
        print("NO SUCH PERSON.\n")

#학생 추가
def add_function(slist):
    s_id = input("Student ID: ")
    found = False
    for i in slist:
        if s_id == i[0]: # 이미 등록된 학생 ID가 있는 경우
            found = True
            print("ALREADY EXISTS.")
            return
    name = input("Name: ")
    mid = int(input("Midterm Score: "))
    if mid < 0 or mid > 100: #중간고사 점수에 0~100외의 값이 입력된 경우
        return #실행되지않음
    final = int(input("Final Score: "))
    if final < 0 or final > 100: # 기말고사 점수에 0~100 외의 값이 입력된 경우
        return #실행되지 않음
    avg = (mid + final) / 2
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
    new_student = [s_id, name, mid, final, avg, grade]
    slist.append(new_student)
    print("Student added.")
    return

#학점 출력
def searchgrade_function(slist):
    grade = input("Grade to search: ").upper() # 소문자도 대문자로 입력받을 수 있도록
    if grade not in ['A', 'B', 'C', 'D', 'F']: # A,B,C,D,F 아니면 함수 종료
        return    
    found = False # 검색 결과를 찾았는지 여부를 저장하는 변수
    start()
    for i in slist:
        if i[5] == grade:
            found = True
            for j in i:
                print(j, end='\t\t')
            print()    
    if not found:
        print("NO RESULTS.\n")

#학생 삭제
def remove_function(slist):
    if not slist: #빈리스트라면
        print("List is empty.")    
    else:
        s_id = input("Student ID: ")
        found = False
        for i in slist:
            if s_id == i[0]: # 학생 ID가 일치하는 경우
                found = True
                slist.remove(i) # 해당 학생을 리스트에서 삭제
                print("Student removed")
                break
        if not found: # 검색 결과가 없는 경우
            print("NO SUCH PERSON.\n")
            
#프로그램 종료
def quit_function(slist):
    answer = input("Save data?[yes/no] ")
    if answer.lower() == 'yes':
        filename = input("File name: ")
        f = open(filename, 'w')
        slist.sort(key=lambda x: x[4], reverse=True) # 학생 평균을 내림차순정렬
        for i in slist:
            line = '\t'.join([str(elem) for elem in i]) + '\n'
            f.write(line)
        f.close()
    elif answer.lower() == 'no':
        pass
        
#파일 읽기               
f = open(file, 'r')
stu_list = []
for line in f:
    data = line.strip().split('\t') # strip함수를 통해 \n을 없애고 split함수를 통해 단어별로 나눔
    data[2] = int(data[2]) # 중간고사 점수를 정수형으로 변환
    data[3] = int(data[3]) # 기말고사 점수를 정수형으로 변환
    data.append((data[2] + data[3]) / 2) # 평균 계산
    if data[4] >= 90:
        data.append('A')
    elif data[4] >= 80:
        data.append('B')
    elif data[4] >= 70:
        data.append('C')
    elif data[4] >= 60:
        data.append('D')
    else:
        data.append('F')
    stu_list.append(data)
show_function(stu_list)
f.close()

#메인
while True:
    command = input("# ").lower() #대소문자를 구분하지 않고 동일하게 명령어의 기능을 수행하기위해
    if command == "show":
        show_function(stu_list)
    elif command == "search":
        search_function(stu_list)
    elif command == "changescore":
        changescore_function(stu_list)
    elif command == "add":
        add_function(stu_list)
    elif command == "searchgrade":
        searchgrade_function(stu_list)
    elif command == 'remove':
        remove_function(stu_list)
    elif command == "quit":
        quit_function(stu_list)
        break
        

