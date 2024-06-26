from time import process_time

start = process_time()

for i in range(1,10):
  print(i)

end = process_time()

print(f'프로그램이 실행되는데 {end-start} 초가 걸렸습니다')