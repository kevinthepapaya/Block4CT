"""

Program goals:
1. Get user input
2. Convert the input to input
3. Add input to list
4. Fill values from specific input positions
"""
#create functions that will perform those actions above
import random
myList = []
unique_list = []


    
def mainProgram():
    while True:
        try: 
            print ("Hello!")
            print("Choose one of the following options. Type numbers ONLY!")
            choice = input("""1. Add to list,
2. Add a bunch of numbers
3. Return the value at an index position
4. Sort list
5. Random choice
6. Linear Search
7. Print Lists
8. End Program """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice== "3":
                indexValues()
            elif choice ==  "4": 
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                printLists()
           # elif choice == "7":

           # elif choice == "8":
            else:
                break
        except:
            print("An error occurred")
    
def addToList():
    newItem = input("Please type an integer")
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("We're gonna add a bunch of numbers.")
    numToAdd = input("How many integers do you want to add?   ")#numbers
    numRange = input("And how high would you like these numbers to go?  ")#range the things that we need
    for x in range (0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")


def sortList (myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list? Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or un-sorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)

        
def indexValues():
    indexPos = input("At what index position would you like to see? ")
    print(myList[int(indexPos)-1])

def randomSearch():
    print("Here's a random value from your list")
    print(myList[random.ranint(0,len(myList)-1)])

def linearSearch():
    print("we're going to search through the list IN THE WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for? Number-wise. ")
    indexCount = 0
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            indexCount = indexCount + 1
            print("Your item is at index {}" .format(x))
    print("You're number appreadred {} times in the list ". format(indexCount))
            




if __name__ == "__main__":
    mainProgram()
