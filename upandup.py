# encryption

# 97 - 122
# 65 - 90
import numpy as np

pt= 'act' # 3 letters only
key='gybnqkurp' # 9 letters only
x=np.zeros(3)
y=np.zeros((3,3))

for i in range(3):
  t=ord(pt[i])
  x[i]=t-97           # one less to count a as 1

m=0
for i in range(3):
  for j in range(3):
    t=ord(key[m])
    y[i,j]=t-97           # one less to count a as 1
    m+=1

# print(y)

res=np.matmul(y,x)

# THIS IS IMPORTANT IDK WHYYYY - do it alag se
for i in res:
  i=int(i%26)
  # print(i)

# print(res)
first=''

for i in range(3):
  # print(res[i])
  first+=chr(int(int(res[i]%26)) + 97)

  
print(first)


# decryption 

#  make matrix out of key 
key='gybnqkurp' # 9 letters only
cw='poh'
# print(cw)
x=np.zeros(3)
y=np.zeros((3,3))

for i in range(3):
  t=ord(cw[i])
  x[i]=t-97           # one less to count a as 1

# print(x)
# print(res)
m=0
for i in range(3):
  for j in range(3):
    t=ord(key[m])
    y[i,j]=t-97           # one less to count a as 1
    m+=1

# print(y)

yi=np.linalg.inv(y)

res1=np.matmul(x,y)

# 222 319 0
# for i in 
# print(res1)
final1=''
for i in range(3):
  final1+=chr(int(int(res1[i])%26) + 97)
  
print(final1)
