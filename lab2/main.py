msg = input()

r1=(int(msg[2])+int(msg[4])+int(msg[6]))%2
r2=(int(msg[2])+int(msg[5])+int(msg[6]))%2
r3=(int(msg[4])+int(msg[5])+int(msg[6]))%2

s1=(int(msg[0])+r1)%2
s2=(int(msg[1])+r2)%2
s3=(int(msg[3])+r3)%2

if(s1!=0 or s2!=0 or s3!=0):
    print('Нашли ошибку в бите №' + str(s1+s2*2+s3*4))
    if msg[s1+s2*2+s3*4-1]=='1':
       msg=msg[0:s1+s2*2+s3*4-1]+'0'+msg[s1+s2*2+s3*4:8]
    else:
        msg=msg[0:s1+s2*2+s3*4-1]+'1'+msg[s1+s2*2+s3*4:8]
else:
    print('Ошибок не найдено!')

print('Верное сообщение:' + msg) 