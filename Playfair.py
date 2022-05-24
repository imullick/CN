import string
def matrix(key):
    m=[[ 0 for j in range(5)]for i in range(5)]
    done=[]
    row=0
    col=0
    for letter in key:
        if letter not in done:
            m[row][col]=letter
            done.append(letter)
            col+=1
            if(col>4):
                col=0
                row+=1
    alpha=string.ascii_uppercase
#    print(alpha[0])
    for letter in alpha:
#        print(m)
        if letter not in done:
            if letter=='J':
                continue
            m[row][col]=letter
            done.append(letter)
            col+=1
            if(col>4):
                col=0
                row+=1      
#    print(m)
    return m

def letters_match(pt):
    index=0
    while(index<len(pt)-1):
        l1=pt[index]
        l2=pt[index+1]
        if(l1==l2):
            pt=pt[:index+1]+'X'+pt[index+1:]
            index=index-1
        index+=2
    if(len(pt)%2!=0):
        pt+='X'
        index+=1
           
    return pt

def getindex(m,letter):
#    print('HERE')
    for i in range(5):
        try:
#            print('hereeeeeee')
            j=m[i].index(letter)
#            print(i,j)
            return (i,j)
        except:
            continue        
    return

def check(val):
#    print(val)
#    print(val)
    if(val==-1):
#        print(val)
        return 4
    else:
#        print(val)
        return val

print()
pt='RACCOON'
print('Initial encrypted text: ',pt)
key='BSCDHRMN'
m=matrix(key)
print('Matrix - ')
for i in m:
    print(i)
    print()
pt=letters_match(pt)
res=''
row1=0
col1=0
row2=0
col2=0
print('Corrected encrypted text: ',pt)
index=0


# use this for decryption
while index<len(pt)-1:
   
    l1=pt[index]
#    print(l1)
    l2=pt[index+1]
#    print(l2)
    if l1=='J':
        row1,col1=getindex(m,'I')
    else:
        row1,col1=getindex(m,l1)
    if l2=='J':
        row2,col2=getindex(m,'I')
    else:
        row2,col2=getindex(m,l2)

    if row1==row2:

        res+=m[row1][check(col1-1)]
        res+=m[row2][check(col2-1)]
    elif col1==col2:

        res+=m[check(row1-1)][col1]
        res+=m[check(row2-1)][col2]
    else:
        res+=m[row1][col2]
        res+=m[row2][col1]
    index+=2
#stri=str('')
print('Decrypted message: ',res)


# # use this for encryption
# while(index<len(pt)-1):
#   l1=pt[index]
#   l2=pt[index+1]
#   index+=2
#   if(l1=='J'):
#     row1,col1=getindex(m,'I')
#   else:
#     row1,col1=getindex(m,l1)
#   if(l2=='J'):
#     row2,col2=getindex(m,'I')
#   else:
#     row2,col2=getindex(m,l2)

#   print(row1,col1)
#   print(row2,col2)

#   if(row1==row2):
#     final+=(m[row1][(col1+val)%5])
#     final+=(m[row2][(col2+val)%5])
#   elif(col1==col2):
#     final+=(m[(row1+val)%5][col1])
#     final+=(m[(row2+val)%5][col2])
#   else:
#     final+=(m[row1][col2])
#     final+=(m[row2][col1])

# print(pt)
# print(final)
  
