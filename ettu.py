
# 65-90, 97-122
# Encryption
P="uvwx"
K=4
C=""
for i in range(len(P)):
    val=ord(P[i])
    if val>=65 and val<=90: #caps
        val+=K
        if(val>90):
            C+=(chr(val-90 + 64))
        else:
            C+=(chr(val))
    elif val>=97 and val<=122:
        val+=K
        if(val>122):
            C+=(chr(val-122 + 96))
        else:
            C+=(chr(val))
    else:
        print("Enter valid plaintext")

print(C)

# Decryption
P1=""
for i in range(len(C)):
    val=ord(C[i])
    if val>=65 and val<=90: #caps
        val-=K
        if(val<65):
            P1+=(chr(val+90 - 64))
        else:
            P1+=(chr(val))
    elif val>=97 and val<=122:
        val-=K
        if(val<=96):
            P1+=(chr(val+122 - 96))
        else:
            P1+=(chr(val))
    else:
        print("Enter valid plaintext")

print(P1)
# print(ord('A'))
