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
7. Recursive Binary Search
8. Iterative Binary Search
9. Print Lists
10. End Program """)
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
                binSearch = input("What number are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                  binSearch = input("What number are you looking for?  ")
                  result = iterativeBinarySearch(unique_list, int(binSearch))
                  if result != -1:
                      print("Your number is at index position {}".format(result))
                  else:
                      print("Your number was not found in that list, buddy!")
                
            elif choice == "9":
                printLists()

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
    if len(unique_list) > 0:
        print(unique_list[random.randint(0,len(unique_list)-1)])

def linearSearch():
    print("we're going to search through the list IN THE WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for? Number-wise. ")
    indexCount = 0
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            indexCount = indexCount + 1
            print("Your item is at index {}" .format(x))
    print("You're number appreadred {} times in the list ". format(indexCount))

def recursiveBinarySearch (unique_list, low, high, x):
    if high >= low:
        mid = (high + low) //2

        if unique_list[mid] == x:
            print("Oh, what luck. Your number is at postion {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
        

    else:
        print("Your number isn't here!")

def interativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) //2

        if unique_list[mid] < x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
                
            




if __name__ == "__main__":
    mainProgram()
