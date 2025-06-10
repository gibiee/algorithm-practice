코테 공부

[![Solved.ac 프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=gibiee)](https://solved.ac/gibiee)

### input.txt 활용
```py
from sys import stdin as s
s = open("input.txt", "r")

N = int(s.readline().strip())
N, M = map(int, s.readline().split())
nums = list(map(int, s.readline().split()))
```