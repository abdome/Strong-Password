import string
import random
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)
char_count=input("Enter length of your generate password ? : ")
while True:
    try:
        char_count=int(char_count)
        if(char_count<6):
            char_count=input("Please enter number from 6 to ... : ")
        else:
            break
    except:
        char_count=input("Please enter number only : ")

#shuffle lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

#calculate percentage
part1=round(char_count*30/100)
part2=round((char_count*20/100))

password=[]

for i in range(part1):
    password.append(s1[i])
    password.append((s2[i]))
for i in range(part2):
    password.append(s3[i])
    password.append((s4[i]))
random.shuffle(password)
password="".join(password[0:])
print(password)