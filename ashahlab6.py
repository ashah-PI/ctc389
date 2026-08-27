# Arpita Shah
#CTC 389
#Lab 6
count = 0
num=0
student = ["John", "Makeyla", "Zionel", "Carmen", "Ruth"]

print("----------------------------------------------")
print("Option 1: Add student to the list ")
print("Option 2: Modify student name")
print("Option 3: Remove student")
print("----------------------------------------------")

option = int(input("Enter the option number that you would like to pick: "))

#Option 1

if (option ==1):
  print("Current list:")
  for i in student:
      print(count, i)
      count = count+1
  add = str(input("Enter the name you want to add to the list: "))
  student.append(add)
  for i in student:
    print(num, i)
    num=num+1

#Option 2
if (option==2):
  print("Current list")
  for i in student:
    print(count, i)
    count = count +1
  m = int(input("Enter the index number that you want to modify the student name: "))
  n= str(input("What name do you want to enter?  "))
  student[m]=n
  print("New list with removed student")
  for i in student:
    print(num, i)
    num = num+1  
    
#Option 3   

if (option ==3):
  print("Current list")
  for i in student:
    print(count, i)
    count = count +1
  remove = int(input("Enter a the index number of the student that you want to remove: "))

  student.pop(remove)
  print("New list with removed student")
  for i in student:
    print(num, i)
    num = num+1
