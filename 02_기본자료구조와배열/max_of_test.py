# 각 배열 원소와 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

from max import max_of

t = (4,7,5.6,2,3.14,1)
s='string'
a = ['DTS', 'ABC', 'BTS']

print(f'{t}의 최대값은은 {max_of(t)}')
print(f'{s}의 최대값은 {max_of(s)}')
print(f'{a}의 최대값은 {max_of(a)}')