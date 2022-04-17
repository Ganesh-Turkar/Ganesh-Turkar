if __name__ == '__main__':
    student_data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_data.append([name,score])
        
score_list  = [scr[1] for scr in student_data]
min_score = min(score_list)
new_score = []
for i in range(len(score_list)):
    if score_list[i]>min_score:
        new_score.append(score_list[i])
        
new_min = min(new_score)
second_lowest_grade = []

for j in range(len(score_list)):
    if score_list[j]==new_min:
        second_lowest_grade.append(student_data[j][0])
        
second_lowest_grade = sorted(second_lowest_grade)
for k in range(len(second_lowest_grade)):
    print(second_lowest_grade[k])
    
