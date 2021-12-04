import sys
def write():
         n = input("write here: ")
         decrypt(n)
         encrypt(n)  
         question = "yes"
         while question == "yes":
            first = []
            second = []
            for i in range(len(n)):
                if i % 2 :
                    first.append(n[i])
                else:
                    second.append(n[i])
    
            print(first+second)
            question = input("again ? 'yes/no' : ")   
            n = (first+second)

def decrypt(n):
    if n == "NULL":
        print("NULL")
    elif n == " ":
        print(" ")

def encrypt(n):
    if n == "NULL":
        print("NULL")
    else: 
        print("")
write()
       
        

   

