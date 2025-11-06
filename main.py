# name = "abolfazl"
# welcome = "hello"
# a = 2
# b = 5

# c = a * b + a 

# print(welcome + " " + name , "are you" , c ,"Years Old?")

# a = str('a = 2x + 5 = 15')

# print(a)


# Converting a word to the same word but in reverse #
# Word = "Hello World ! \n we start Python "
# ShowRes = '\n and this is Reverse'
# print(Word[::-1] + " " + ShowRes)

# #  Convert the first letter of the name to uppercase.  #
# names = ["abolfazl","ali","erfan","chama","rajab"];
# firstLetter = names[1][0];

# if firstLetter.islower():
#      upperCase = firstLetter.upper()
#      sum = upperCase + names[1][1:]
#      print(f"Before = {names[1]} \n After = {sum}")

# else:
#      print("your first letter is allready upperCase")

# # Specify the type of the variable #
# StringTest = "Ali";
# IntTest = 13;
# floatTest = 19.15;
# print(type(StringTest) , '\n' ,  type(IntTest) ,  '\n'  , type(floatTest))



# lists , Dicts , topples and Sets # 

# favoriteNumber = [3 , 6 , 9 , 13 , 7]
# favoriteNumber.pop()  --> delete last index
# print(favoriteNumber)

# Skills = {"abolfazl" : "web" , "ali" : "football" , "erfan" :"ai"}
# print(Skills.keys())
# print(Skills.values())
# print(Skills.items())

# Club = set()
# Club.add("Abolfazl")
# Club.add("erfan")
# Club.add("Rajab")

# School = set()
# School.add("Abolfazl")
# School.add("Chama")
# School.add("Ali")

# print(Club)
# print(School)

# print(Club.union(School))
# print(Club.intersection(School))


## open file with py

# openFile = open('one.txt')

# print(openFile.read())

# openFile.close();

# with open('one.txt' ,  'a') as openFile:
#      # print(openFile.readlines())
#      newLine = openFile.write(" \n this is the new fucking line! \n ")
#      print(newLine)
#      openFile.close();


# strTest = 'hello python';
# res = type(strTest) == str;
# print(res)
# if res == True :
#      print('yes, you are right')
# else:
#      print('no, you are wrong')
     

#name to binery
# name = 'abolfazl';

# float binaryInt = int(0110000101100010011011110110110001100110011000010111101001101100) 

# search = name == binary;
# print(search)

# age = 18
# gender = "Transgender";
# carAviable = True;

# if(age >= 18) and  (gender == "male" or gender == "female") and (carAviable == True):
#      print("you can take your Govahinameh")
# else:
#      print(" Sorry . you can not take your Govahinameh")
     
# People = (('ali',17,196),('erfan',17,183),('moein',17,173));
 
# for person in People :
#      firstName,age,height = person;
#      print(f"he is '{firstName}' and he is '{age}' years old and he is '{height}' cm tall! \n")


# getNum = int(input("Enter a number to start your game : "))
# while  getNum != 7 :
#      print('the number is wrong')
#      print(f'your number was {getNum}');
#      anotherChanse = input('do you want to exit? -> yes/no \n')
#      if  anotherChanse == "yes" or anotherChanse == "Yes" :
#           break   
     
# n = 0
# numforUsers = int(input("Enter a number between 1-1000 : "))
# while n < numforUsers:
#      n += 1 
#      numOfSorosh = 0

#      if  n % 3 == 0 and n % 5 == 0 :
#           print("hiphopologist")
#           numOfSorosh += 1
#           continue
#      elif   n % 3 == 0 :
#           print('hip')
#           continue
#      elif n % 5 == 0 :
#           print ('hooooop')
#           continue
#      print (n)
          
#      if   numOfSorosh >= 3 :
#           print("you got Dildo talayii")

# score = [0 , 20 , 18 , 19 , 3 , 12]
# listToInt = score.index();
# print(f"{listToInt} is first Score");
# if   listToInt <= 18 :
#      newScore = []
#      for  nScore in score :
#           newScore.append(nScore + 2)
#      print(f"{newScore} is Score + 2 more score!")

# elif listToInt == 19 :
#      rint(f"{score} is {score} without any more score");
#      newScoreForNineteen = [];
#      for  nScoreForNineTeen in score :
#           newScoreForNineteen.append(nScoreForNineTeen + 1)
#           print(f"{newScoreForNineteen} is your first Score + 1 more score!")
          
          
# score = [0 , 16 , 18 , 15 , 3 , 12] ;
 
# newScore = [x + 2 for x in score]
# print (newScore)

# for tool in range (1,6) :
#      for arz in range (1,11) :
#           print (tool * arz , end="\t")
#      print(" ")


# myFriends = ["arsalan" , 'ali' , 'erfan' , 'chama']
# BestFriendInfo = {
#                'arsalan' : {'ghad' : 183 , 'sen' : 19},
#                'ali' : {'ghad' : 174 , 'sen' : 18},
#                'erfan' : {'ghad' : 185 , 'sen' : 17},
#            }
# for  bestFrineds in myFriends :
#      if   bestFrineds in BestFriendInfo :
#           print(f"my best friend is {bestFrineds} and he is {BestFriendInfo[bestFrineds]['sen']} y/o and he has {BestFriendInfo[bestFrineds]['ghad']} c'm tall!")
#      else :
#           print(f"{bestFrineds} dosen't find in data Base !")

# print(max(1, 20 , 100 , 1234 , 1005)) #output -> 1234     مهم
# print(min(1, 20 , 100 , 1234 , 1005)) #output -> 1       مهم


# from random import randint
# a = randint(1,101)
# print(a)


# def avrage(a , b) :
#      Scores = [5 , 8 , 13 , 18 , 14 , 20];
#      for  avgScore in Scores :
#            a = avgScore 
#            b = Scores.count()
#            return a / b    
#      print(avrage())
     

# def is_fardOrIs_zoj(num) :
#      if   num  % 2 == 0 :
#           print(f"adad zoj ast! adad to {num} bood")
#      else :
#           print(f"adad fard ast! adad to {num} bood")

# num = input("yek adad vared konid : ")
# num = int(num)
# is_fardOrIs_zoj(num)

# firstName = input("Enter your firstName : ")
# def callName(firstName) :
#      print(f"hello {firstName} welcome to my python project!")
# callName(firstName)


# def callName(firstName) :
#      print(f"hello {firstName} welcome to my python project!")
# callName(firstName = input("Enter your firstName : "))

# def find_letter_in_word(word,letter) :
#      NumOfLetter = 0
     
#      for  howMuch in word :
#           if   howMuch == letter :
#                NumOfLetter += 1 ;
#      return (NumOfLetter)


# word = input("enter your word : ")
# letter = input("enter your letter : ")
# print(f"your word is {word} and it has {find_letter_in_word(word,"a")} {letter}")

# def is_odd_or_even(num,statue):
#      if   num % 2 != 0 :
#           statue = 'Odd'
#           return statue
#      else :
#           statue = 'even'
#           return statue
     
# number = input("tell us your number to see it is odd or even : ")
# number = int(number)

# is_odd_or_even(number,statue)

# def is_even(number):
#      return number % 2 == 0

# def return_all_odd(number_List):
#      newList = []
#      for n in number_List:
#           if not is_even(n):
#                newList.append(n)
#           return newList
     
# lst = [1,2,3,4,5,6,7,8,9,10]
# lst_odd = return_all_odd(lst)
# print(lst_odd)
 
# donate = {
#      'arsalan' : 40,
#      'ali' : 80,
#      'erfan' : 40
# }

# def totally_Donation(Donation):
     
     
          
# jam , miangin , bishtarin = totally_Donation(Donation)
# print (f"dar majmoe {jam} tooman va miangin {miangin} tooman donate shode \n {bishtarin} az hame 
#        bishtar donate karde!")


# import random
# pcNum = random.randint(1,100)
# isWin = False;
# def  game():
#      while(isWin == False):
#           systemText = input("enter a number between 1/100 : ")
#           systemText = int(systemText)
#           if   systemText == pcNum :
#                print(f"you win ! system_number was {pcNum} and your number is {systemText}")
#                isWin == True
#           elif systemText < pcNum :
#                print("your number is less than system number")
#           else :
#                print("your number is more than system number")
               
# game();


          #**kwargs -> dictionary
          #*args
# print(f"args is {args}")

# def plus(listOfNumbers):
#      f = 0
#      for i in listOfNumbers :
#           f += i
#      return f
# numOfUsers = []
# resume = True;
# while (resume):
#      userWantsToResume = input("do you want to enter number? (yes/no) --> ")
#      if   userWantsToResume == "yes" or userWantsToResume == "Yes":
#           numOfUser = input("inter a number : ") 
#           for io in numOfUser :
#                io = int(numOfUser)
#                numOfUsers.append(io)
#                break
#      elif   userWantsToResume == "no" or userWantsToResume == "No":
#           resume = False;
#      else :
#           print("please enter right word to resume or end program! ")
# res = plus(numOfUsers)
# print(res)

          #anonymos functions                               مهمه

# def darsad(i):
#      return i % 2;

          # lambda darsad:i%2                               مهمه

# numOfUsers = []
# resume = True;
# while (resume):
#      userWantsToResume = input("do you want to enter number? (yes/no) --> ")
#      if   userWantsToResume == "yes" or userWantsToResume == "Yes":
#           numOfUser = input("inter a number : ") 
#           for io in numOfUser :
#                io = int(numOfUser)
#                numOfUsers.append(io)
#                break
#      elif   userWantsToResume == "no" or userWantsToResume == "No":
#           resume = False;
#      else:
#           print("please enter right word to resume or end program! ")
          
# val = map(darsad,numOfUsers)
          # val = map(lambda i:i%2,numOfUsers)         مهمه    
# print( list(val))

# def is_float(i):
#      if   not i == int(i):
#           return i
# lst = [1,2,2.3,3.3,4,5.1,2421.123,123.0]
# print(list(filter(lambda i: i != int(i),lst)))

# lst = [172,178,181,180,192,200,211]
# short_height = filter(lambda i: i >= 180,lst)
# print(list(short_height))


          # Score Variables ->      local         ,          global         ,       build-in
          

          #         Start OOP
          
          
# class clName():
#      def __init__(self,param1):
#           self.param1 = param1;
#           print(f"Obj Created!");
#      def sayHello(self):
#           print("hello OOP")
          
# newClass = clName(10)
# print(newClass.param1)

# class Calculator():
#      def Calc(self,numOne,numTwo,operation):
#           self.operation = operation;
#           self.numOne = numOne;
#           self.numTwo = numTwo;
#           if   operation == '+':
#                  return numOne + numTwo;
#           elif   operation == "-":
#                  return numOne - numTwo;
#           elif   operation == "/":
#                  return numOne / numTwo;
#           elif   operation == "*":
#                     return numOne * numTwo;
#           else:
#                     print("put a valid operation")
          
# newCalc = Calculator(); 
# CalculatorStart = False;
# wannaCalc = input("do you want to Calculate some math? (yes/no) : ");
# if   wannaCalc == "yes" or wannaCalc == "Yes":
#      CalculatorStart = True
     
# while(CalculatorStart):
#      a = int(input("please put First number : "));
#      b = int(input("please put Second number : "));
#      Op = input("please put operation (+,*,/,-) : ");
#      print(newCalc.Calc(a,b,Op))
#      res = input("Do you want to resume ? (yes/no) : ")
#      if   res == "no" or wannaCalc == "No":
#           break;


# from rich import print

# class Book():
#      def __init__(self,name,page):
#           self.page = page;
#           self.name = name;
#      def openBook(self):
#           print(f"you opened the book called '{self.name}' and this book has '{self.page}' pages")
# # bookInfo = Book("rastakhiz",752)
# # bookInfo.openBook()

# class schoolBook(Book):
#      def __init__(self,name,page,subject,grade):
#           Book.__init__(self,name,page)
#           self.name = name;
#           self.page = page;
#           self.subject = subject;
#           self.grade = grade;
#      def openSchoolBook(self):
#           print(f"You opened the book called [bold red]{self.name}[/bold red] "
#               f"and this book has [cyan]{self.page}[/cyan] pages, "
#               f"the subject is [green]{self.subject}[/green], "
#               f"and you are in [purple]{self.grade}[/purple] grade.")
# ketabeDarsi = schoolBook("Arabic",40,"IT",12);
# ketabeDarsi.openSchoolBook();
