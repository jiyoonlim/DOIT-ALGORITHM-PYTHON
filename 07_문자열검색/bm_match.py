# 보이어 무어법으로 문자열 검색하기 (문자열 길이는 0-255개)

def bm_match(txt: str, pat: str) -> int:
  """보이어-무어법으로 문자열 검색"""
  skip = [None] * 256 # 건더뛰기 표

  # 건너뛰기 표 만들기
  for pt in range(256):
    skip[pt] = len(pat)
  for pt in range(len(pat)):
    skip[ord(pat[pt])] = len(pat) - pt -1

  # 검색하기
  while pt < len(txt):
    pp = len(pat) - 1
    while txt[pt] == pat[pp]:
      if pp == 0:
        return pt
      pt -= 1
      pp -= 1
    pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp

  return -1

if __name__ == '__main__':
  