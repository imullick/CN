done=[]
import numpy as np
def matrix(key):
  m = [[0 for i in range (5)] for j in range(5)]
   #letters added
  row=0
  col=0
  for letter in key:
    if letter not in done:
      m[row][col]=letter
      done.append(letter)
      col=col+1
      if(col>4):
        col=0
        row+=1

  for letter in range(65,91):
    if letter==74: # for i,j 
      continue
    if chr(letter) not in done:
      m[row][col]=chr(letter)
      done.append(chr(letter))
      col=col+1
      if(col>4):
          col=0
          row+=1
  print(m)
  return m


def letters_check(pt):
  index=0 
  while(index<len(pt)-1):
    l1=pt[index]
    l2=pt[index+1]
    if(l1==l2):
      pt=pt[:index+1]+'X'+pt[index+1:]
    index+=2
    # print(pt)
  if(len(pt)%2!=0):
    pt+='X'
  # print(pt)
  return pt


def getindex(m,letter):
  for i in range(5):
    try:
      j=m[i].index(letter)
      return (i,j)
    except:
      continue
  

pt='INSTRUMENTS'
key='MONARCHY'
m=matrix(key)
pt=letters_check(pt)
val=1 # (put -1 for decryption)
final=[]
index=0
while(index<len(pt)-1):
  l1=pt[index]
  l2=pt[index+1]
  index+=2
  if(l1=='J'):
    row1,col1=getindex(m,'I')
  else:
    row1,col1=getindex(m,l1)
  if(l2=='J'):
    row2,col2=getindex(m,'I')
  else:
    row2,col2=getindex(m,l2)

  print(row1,col1)
  print(row2,col2)

  if(row1==row2):
    final+=(m[row1][(col1+val)%5])
    final+=(m[row2][(col2+val)%5])
  elif(col1==col2):
    final+=(m[(row1+val)%5][col1])
    final+=(m[(row2+val)%5][col2])
  else:
    final+=(m[row1][col2])
    final+=(m[row2][col1])

print(pt)
print(final)
