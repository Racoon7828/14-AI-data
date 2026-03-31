# 파이썬에서는 sys 모듈을 사용하여 프로그램에 인수를 전달할 수 있다. 
# sys 모듈을 사용하려면 다음 예의 import sys처럼 import 문을 사용해야 한다.
import sys

args = sys.argv[1:]
for i in args:
    print(i)