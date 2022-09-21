import os
os.system("clear");
son = int(input("n => "));
sch = 2;
lamp = True;
while sch <= son**(1/2):
    if(son%sch==0):
        print("Murakkab");
        lamp = False;
        break;
    sch+=1;
if lamp == True:
    print("Tub");
# Xudoyberdiyev Kamoliddin Zafar o'g'li