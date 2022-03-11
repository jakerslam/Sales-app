import random
from random import randint
import os
from re import S
import names # requires pip install names

class Person:
  def __init__(self, age, gender, type, houseSize,name,company,pronoun,buyingTemp):
    self.name = name
    self.age = age
    self.gender = gender
    self.type = type
    self.houseSize = houseSize
    self.company = company
    self.pronoun = pronoun
    self.buyingTemp = buyingTemp

def getObjections():
    fileObj = open('objections.txt', "r") #opens the file in read mode
    text = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return text

def main():
  objections = getObjections()
  os.system('cls' if os.name=='nt' else 'clear')
  cstmr = Person(randint(25,75),gender(),rndType(),randint(1800,4000),"",genCompany(),"",initButTemp())
  cstmr.name = names.get_first_name(gender=cstmr.gender)
  if (cstmr.gender == "male"): cstmr.pronoun = "he" 
  else: cstmr.pronoun = "she"

  print  ("Situation: " ,cstmr.name, "is a" ,cstmr.age, "year old" ,
cstmr.gender, "who is" ,cstmr.type, "and lives in a", cstmr.houseSize, "sqft house and" ,
cstmr.pronoun , "has",cstmr.company,"\n")
  quit = 0
  while (quit == 0):
    option = input("\n- Enter to get an objection\n- 'o' to enter a new objection\n- 's' for a new situation\n- 'q' to quit\n>")
    if (option == ''): 
      if (cstmr.buyingTemp == 10):
          print("\nYou convinced them!")
          input("\n - Enter to continue")
          main()
      cstmr.buyingTemp += 1
      giveObjection(objections)
    if (option == 's'):
      main()
    if (option == 'o'):
      newObjection()
    elif (option == 'q'):
      os._exit()
      
      
def rndType():
  type = {
        1: "a bull",
        2: "a tiger",
        3: "a lamb",
        4: "an owl"
  }
  return type.get(randint(1,4), "Bull")

def gender():
  gender = randint(0,1)
  if (gender == 0):
    return 'male'
  else:
    return 'female'

def genCompany():
    propability = randint(1,9) # propability 1/3
    if (propability < 4):
        randint(1,5)
        companies = {
            1: "Terminix",
            2: "Orkin",
            3: "Fox",
            4: "Brooks",
            5: "a family friend who does it"
        }
        return companies.get(randint(1,5), "no company")
    return "no company"

def initButTemp(): # There's a much higher propability of a lower buying temprature than high
    prop = randint(1,100)
    if (prop < 5):
        return randint(7,10)
    if (prop < 20):
        return randint(5,6)
    else: return randint(1,4)

def newObjection():
    with open("objections.txt", "a") as file_object:
     file_object.write("\n")
     file_object.write(input("Write your objection"))

def giveObjection(objections):
  os.system('cls' if os.name=='nt' else 'clear')
  print("\n" , random.choice(objections))
  input("\n - Enter to continue")
  os.system('cls' if os.name=='nt' else 'clear')
  return

if __name__ == "__main__":
  main() 