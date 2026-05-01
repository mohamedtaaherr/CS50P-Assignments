# DEEP THOUGHT PROBLEM
'''
answer = input("what is answer ?").strip().lower()
if answer =="42" or "forty two " or "forty-two":
    print("yes")
else:
    print("no")
#another solution

answer = input("what is answer ?").strip().lower()
match answer:
    case "42" | "forty-two" | "forty two" :
        print("yes")
    case _ :
        print("no")
'''


#HOME FEDERAL SAVINGS BANKS
'''
greeting = input("Greeting :").strip().lower()
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else :
    print("$100")
'''

#FILE EXTENSION
'''
filename = input("File name: ").strip().lower()

if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
'''

#MATH INTERPRETER
'''
expression = input("expression :").strip()
x,y,z = expression.split()
x=float(x)
z=float(z)
if y == "+":
    print(x+z)
elif y =="-":
    print(x-z)
elif y=="/":    
    print(x/z)
else:
    print("invalid")
'''

'''
def main():
    time = input("What time is it? ").strip()
    hours, minutes = convert(time)

    # Check meal times
    if 7.0 <= hours + minutes / 60 <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours + minutes / 60 <= 13.0:
        print("lunch time")
    elif 18.0 <= hours + minutes / 60 <= 19.0:
        print("dinner time")

def convert(time):
    # Split into hours and minutes
    if ":" in time:
        hours, minutes = time.split(":")
    else:
        hours, minutes = time.split()  # Fallback for space-separated input

    return float(hours), float(minutes)


if __name__ == "__main__":
    main()
'''
'''
def main ():
    time = input("what time it is ? ").strip()
    hours,minutes=convert(time)
    y=hours+minutes/60
    if 7<=y<=8:
        print(hours,":",minutes,"is breakfast time")
    elif 12 <= y<= 13:
        print(hours ,":",minutes,"is lunch time ")
    elif 18<=y<=19 :
        print (hours ,":",minutes,"is dinner time ")

def convert(t)  :
    if ":" in t:
        h,m=t.split(":")
    else :
        h,m=t.split()
    return float(h),float(m)

main()
'''
#CAMEL CASE PROBLEM


'''
s = input("Enter camelCase name: ").strip()
result=[]
for i, char in enumerate(s):
    if char .isupper() and i!= 0:
        result.append("_"+char.lower())
    else :
        result.append(i)
print ("" .join(result))
'''
#COKE MACHINE PROBLEM
'''
y: int = 50
z=0
accepted = [25,10,5]
while y>0 :
    x=int(input("insert coin : "))
    if x in accepted :
     y-=x
     if y>0 :
         print("amount due : ", y)
     elif y <0 :
         z=abs(y)
         print ("change : " , z)

    else :
        print("invalid coin")
'''
# JUST SETTING UP MY TWTTR PROBLEM
'''
x= input("input : ")
output = []
vowels = ['a','e','i','o','u']
for i in x :
    if i in vowels :
        print("",end="")


    else :
        output.append(i)
# ANOTHER SOLUTION


print ("" .join(output))

x = input("Input: ")
output = []
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for char in x:
    if char not in vowels:
        output.append(char)

print("".join(output))
'''
# vanity plate Liscense
'''
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    

def is_valid(s):
     if not 2 <= len(s) <= 6:
         return False
     if not s[:2].isalpha():
         return False
     if not s.isalnum():
         return False
     n=len(s)
     found_number = False
     for i, char in enumerate(s):
         if char.isdigit():
             if not found_number and char=='0':
                 return False
             found_number= True
         elif found_number :
          return False
     return True

main()
'''
#NUTRIRION
'''
def main():
    fruit= input("Item : ").strip().lower()
    print ("calories : ", calories(fruit))

def calories(item):
    nutrition = {
        "apple": 130,
        "banana": 110,
        "kiwifruit": 90,
        "pear": 100,
        "sweet cherries": 100
    }
    return nutrition.get(item,"")

main()
'''
# Guess Game
'''
words = {
    'pair':4,
    'chair':5,
    'hair':4,
    'graphic':7
}
answer= input("this is my game do you want to play : ").strip().lower()

if answer == "yes" :
    print (" the letters are : r,c,a,g,p,h,i")
    while len(words) > 0:
        print (f'you have {len(words)} guesses')
        g = input("enter your guess :")
        if g=="graphic" :
            words.clear()
        elif g  in words:
            print (f"your guess: {g}  is right ")
            words.pop(g)
        else:
            print ("your guess is not right try again")
else :
    print ("okay")
print ("Game Over ")
'''
#FUEL GAUGE
'''
while True :
    try :
        fraction = input("enter fraction : ")
        x,y=map(int,fraction.split("/"))
        if y ==0 :
          raise(ZeroDivisionError)
        if x>y or x<0 :
            raise (ValueError)
        percent = round ((x/y)*100)
        if percent>98 :
            print ("F")
        elif percent<2 :
            print ("E")
        else :
            print (f'{percent}%')
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        print ("divide error ")
'''
#BETTER SOLUTION
'''
while True:
    try:
        fraction = input("Fraction: ")
        x, y = map(int, fraction.split('/'))
        
        # Only business logic validation (no zero division check)
        if x > y:
            raise ValueError
            
        percent = round(x / y * 100)
        print("E" if percent <= 1 else "F" if percent >= 99 else f"{percent}%")
        break
        
    except (ValueError, ZeroDivisionError):
        pass
'''
#Felipe’s Taqueri
'''
total=0
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00

}
while True :
    try:
        item = input("item : ").title()
    except EOFError:
        break

    if item in menu :
        total = total + menu[item]
        print (f'$ {total}')
    else :
        pass

'''
# Grocery Listy
'''
grocery = {}
while True :
    try :
        item = input("enter item :").strip().lower()
        if item in grocery:
            grocery[item]+=1
  onths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",      else :
            grocery[item]=1
    except EOFError:
         break
for item in sorted(grocery):
          print (f'{grocery[item]} - {item}')
'''
# OUTDATED
'''
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        # Format 1: MM/DD/YYYY (US numeric format)
        if "/" in date:
            x, y, z = map(int, date.split("/"))

            # Assume MM/DD/YYYY - first number must be valid month
            if 1 <= x <= 12 and 1 <= y <= 31:  # x=month, y=day, z=year
                print(f"{z}-{x:02d}-{y:02d}")  # YYYY-MM-DD
                break
            else:
                continue  # Invalid date, reprompt

        # Format 2: Month Day, Year (text format)  
        elif " " in date and "," in date:
            parts = date.split(" ")
            if len(parts) == 3:
                month_name = parts[0].title()  # Capitalize first letter
                day_str = parts[1].replace(",", "")  # Remove comma
                year_str = parts[2]

                # Check if valid month name and numbers
                if month_name in months and day_str.isdigit() and year_str.isdigit():
                    month_num = months.index(month_name) + 1
                    day_num, year_num = int(day_str), int(year_str)

                    if 1 <= day_num <= 31:
                        print(f"{year_num}-{month_num:02d}-{day_num:02d}")
                        break

    except (ValueError, IndexError):
        pass
'''
#IMOJIZE
'''
import emoji
def main():
    text = input("input :")
    emojiliz_text= emoji.emojize(text,language="alias")
    print (f'output : {emojiliz_text}')
main()
'''
#Frank, Ian and Glen’s Letters
'''
from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts_menu=figlet.getFonts()
if len(sys.argv)==1:
    font = random.choice(fonts_menu)

elif len(sys.argv)==3:
    if sys.argv[1]not in ["-f","--font"]:
        sys.exit("-f and --font not found")
    font = sys.argv[2]
    if font not in fonts_menu:
        sys.exit("invalid font")
else :
    sys.exit("invalid number of argument part 2")

text = input(" Text :")
figlet.setFont(font = font)
print(figlet.renderText(text))
'''
#Adieu, Adieu
'''
import inflect
p=inflect .engine()
names=[]
while True:
    try :
        x=input("Enter :")
        names.append(x)
    except  EOFError:
        if len(names) == 0:
            ("error at leat enter one name")
        else :
            break
organized = p.join(names)
print(f"Adieu, adieu, to {organized}")
'''
#Guessing Game
'''
import random
def getpositive(msg):
    while True:
        try:
            l = int(input(msg))
            if l > 0:
                return l
            else:
                print("plz enter positive number")
        except ValueError :
            print ("invalid input")
def main():
    level = getpositive("Level : ")
    number = random.randint(1,level)
    
    while True :
        try:
            guess = getpositive("Guess : ")

            if guess > number:
                print("too large")
            elif guess<number :
                print("too small")
            else :
                print ("just right ")
                break
        except ValueError:
            print ("invalid input")

if __name__ == "__main__":
    main()
'''
# Little Professor
'''
import random
def getlevel(msg):
    while True:
        try:
            l=int(input(msg))
            if 0<l<4:
                return l
            else:
                print ("plz enter number from 1 to 3")
        except ValueError:
            print("print invalid input")


def generateinteger(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3")

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:  # level == 3
        return random.randint(100, 999)

def main():
    level=getlevel("Level :")
    score=0
    nu_error=0


    for i in range (1,11):
        x= generateinteger(level)
        y= generateinteger(level)
        if i == 10:
            break
        print (f'{x}+{y} = ')
        z=int(input())
        answer= x+y
        if z == answer :
            score +=1
        else :
            nu_error+=1
            print ("EEE")
        if nu_error ==3:
            print(f'{x}+{y} = {answer}')
            nu_error=0
    print(score)
main()
'''
'''
    while True:
        try:
            x = generateinteger(level)
            y = generateinteger(level)
            print(f'{x}+{y}= ')
            z = input()
            attempt+=1
            if z == x + y:
                score += 1
            else:
                print("EEE")
                nu_error+=1
            if nu_error==3:
                print (f"{x}+{y}={x+y}")
                nu_error=0
            if attempt==10:
                print(f"score = {score}")
                break

        except ValueError:
            pass
'''

'''
import sys
import requests
def main() :
    if len(sys.argv) != 2:
        sys.exit("not required number of arguments")
    try:
        amount =float(sys.argv[1])
    except ValueError:
        sys.exit("wrong value")
    try:
        response=requests.get("https://api.coincap.io/v3/assets/bitcoin")
        data=response.json()
        price=float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("request error")
    except (KeyError,ValueError):
        sys.exit()
    cost=amount*price
    print(f'${cost:,.4f}')

if __name__ == "__main__":
    main()

        '''
import sys
import os
if len(sys.argv)!=2:
    sys.exit("too few arguments ")
file_name=sys.argv[1]
if not file_name.endswith(".py"):
    sys.exit("wrong extension")
try:
    file=open(file_name,"r")
    count = 0
    for line in file:
        clean = line.strip()
        if clean == "":
            continue
        if clean.startswith("#"):
            continue
        count += 1
except FileNotFoundError:#file not exist
    sys.exit("file not found")
print (count)































