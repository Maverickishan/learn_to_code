x,y = map(int,input().split())
"""l=(int(x)-1)/2
b=(int(y)-1)/2


for i in range(int(l)):
    print(('.|.'*i).rjust(int(b)-1,"-")+".|."+('.|.'*i).ljust(int(b)-1,"-"))

for i in range(1):
    print("WELCOME".center((int(b)*2)+1,"-"))

for i in range(int(l)):
    print((".|."*(int(l)-i-1)).rjust(int(b)-1,"-")+".|."+(".|."*(int(l)-i-1)).ljust(int(b)-1,"-"))"""

for i in  range(x):
    if i%2==1:
        print((".|."*i).center(y,"-"))
        

print("WElCOME".center(y,"-"))

for i in range(1,x):
    if (x-i) % 2 ==1:
        print((".|."*(x-i)).center(y,"-"))





