#https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python


def encrypt(text, n):
    while n>0:
        lst1=[]
        lst2=[]
        lst3=[]
        lst4=[]
        for i in range(len(text)):
            if i>0 and i%2 !=0:
                lst1.append(text(i))
            elif i>0 and i%2 ==0:
                lst3.append(text(i))
            elif i==0:
                lst2.append(text(i))
        lst4=lst1+lst2+lst4
        lstlast="".join(lst4)
        return lstlast
        lst1.clear()
        lst2.clear()
        lst3.clear()
        lst4.clear()

         
        




n=int(input("Enter number here: "))
text=str(input("Entere text here:  "))

print(encrypt(text, n))