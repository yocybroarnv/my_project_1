Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
... import os
... import string
... 
... img = cv2.imread("ArnavRaj")
... 
... 
... msg = input("Enter secert message")
... 
... password = input("Enter password")
... 
... d={}
... c={}
... 
... for i in range(255):
...     d[chr(i)]=i
...     c[i] = chr(i)
... 
... m=0
n=0
z=0

for i in range(len(msg)):
    img[n,m,z] = d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite("Encryptedmsg.jpg",img)

os.system("start Encryptedmsg.jpg")


message =""

n=0
m=0
z=0

pas = input("Enter passcode for Decryption")

if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1) % 3
    print("Decryption message",message)
else:
