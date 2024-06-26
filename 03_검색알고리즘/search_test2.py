# seq_search() 함수를 사용하여 특정 인덱스 검색하기

from search_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}에서 5.6의 인덱스는 {seq_search(t, 5.6)}')
print(f'{s}에서 t의 인덱스는 {seq_search(s, "t")}')
print(f'{a}에서 "AAC"의 인덱스는 {seq_search(a, "AAC")}')