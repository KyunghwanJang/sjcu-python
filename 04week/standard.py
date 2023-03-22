# 표준 라이브러리는 import하여 사용한다.

import datetime
date = datetime.date(2023, 3, 1)
print(date)
print(date.isoweekday())

import time
current = time.time()
print(current)
current = time.localtime(current)
print(current)
current = time.strftime('%c', current)
print(current)

import random
for count in range(5):
    print(f'count : {count}')
    print(random.randint(1,10))
    time.sleep(1)
    
# 객체를 직접 저장하고 읽어들이기
import pickle
data = {'chris':1, 'tommy':2, 'harry':3 }
file = open('picket.txt', 'wb')
pickle.dump(data, file)
file.close()

file = open('picket.txt', 'rb')
data = pickle.load(file)
file.close()
print(data)

import os
print(os.environ['PATH'])
os.system('dir')
file = os.popen('dir')
print(file.read())
file.close()


