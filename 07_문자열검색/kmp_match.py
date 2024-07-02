# KMP 법으로 문자열 검색하기

def kmp_match(txt: str, pat: str) -> int:
  """KMP법으로 문자열 검색"""
  pt = 1 # txt를 따라가는 커서
  pp = 0 # pat을 따라가는 커서
  skip = [0] * (len(pat) + 1) # 건너뛰기 표

  # 건너뛰기 표 만들기
  skip[pt] = 0
  while pt != len(pat):
    if pat[pt] == pat[pp]:
      pt += 1
      pp += 1
      skip[pt] = pp
    elif pp == 0:
      pt += 1
      skip[pt] == pp
    else:
      pp = skip[pp]

  # 문자열 검색하기
  pt = pp = 0
  while pt != len(txt) and pp != len(pat):
    if txt[pt] == pat[pp]:
      pt += 1
      pp += 1
    elif pp == 0:
      pt += 1
    else:
      pp = skip[pp]
  return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
  s1 = input("enter text: ")
  s2 = input("enter pattern: ")

  idx = kmp_match(s1, s2)

  if idx == -1:
    print('pattern does not exist within text')
  else:
    print(f'{(idx + 1)} 번째 문자가 일치합니다.')
