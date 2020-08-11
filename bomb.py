import  os
from time import *
def make(n):
  f = open(n+".txt","a")
  x = 10**10**3
  while True:
    f.write(str(x))
    f.write(str(x))
    if os.stat(n+".txt").st_size > (10**8):
      break
i=0

while True:
     x = time()
     make(str(i))
     print(time()-x)
     i+=1

