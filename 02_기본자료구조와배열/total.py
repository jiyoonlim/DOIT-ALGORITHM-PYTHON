# 학생 5명의 시험 점수를 받아 합계와 평균 구하기
print('Find the average and sum of group score')

score1 = int(input('Enter the score for Student1: '))
score2 = int(input('Enter the score for Student2: '))
score3 = int(input('Enter the score for Student3: '))
score4 = int(input('Enter the score for Student4: '))
score5 = int(input('Enter the score for Student5: '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'total is {total}')
print(f'average is {total/5}')