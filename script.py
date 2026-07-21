#print("hello class");
balance = 10
#here is a statment to add two numbers 
#print(10+10)
#sami_age = 20
#print(sami_age)

#student_name = "sami"
#student_age = 13
#print (student_name)
#age = input("input your age: ")
#age = int(age)
#nextyear = (age + 1)
#print(nextyear)
#salary = input ("enter your slalary: ")

#print (float(salary) + 1000)

#balance =(float(salary) + 90000)
#if balance >= 100000:
 #   print(f"{student_name} you are not broke")
#else:
 #   print(f"{student_name} you are broke")
    #for phyton it is elif 
    #and you dont run it on python in the terminal just bash 
# while loop
#while balance >=0:
    #balance -= 1
   # print(f"i have {balance} laft")

# for loop
#for i in range(10):     #in this i starts from 0 so it is from 1-9 but we can make i start from 1 by making range (1,10)
 #   print(f"current number is{i}")

#break
#for i in range( 1, 10):
 #   if i >= 5:
  #      break
   # print (f"current number is {i}")

#function
# def myFunction(balance):
    
#     print("hellow world")
#     while balance >=0:
#         balance -= 1
#     print(f"i have {balance} left")

# myFunction(20) #calling the function


def NumbersList():
    num = []  
    try:
        tot = int(input("how much numbers do you want to enter"))
        if tot <= 0:
            print("enter the ammount of numbers you want in your list")
        else:
            for i in range(tot):
                user_in = input (f"enter numbers {i+1} one by one oe type finish to stop")
                if user_in == "finish":
                     break
                try:
                    num = float(user_in)
                except ValueError:
                     print("u didnt enter numbers try again")
    except ValueError:
        print("That was not a number.")
    return num 
            
def Linear(num , target):         
    for i, x in enumerate(num):
        if x == target:
            return i
        return -1
    num = NumbersList()

    if num:
        try:
            target = float(input("enter the target"))
            ind = Lin(num, target)
            if index != -1:
                print(f"target foun dat index {index}")
            else:
                print("target not found :(")
        except ValueError:
            print("invalid input")
    else:
        print("none given numbers")

if __name__ == "__main__":
    num = NumbersList()
    target = int(input("Enter your target number: "))
    idx = Linear(num, target)
    if idx != -1:
        print(f"Target found at index {idx}")
    else:
        print("Target not found.")
