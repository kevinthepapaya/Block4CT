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
    print ("Hello! Let's work with some cool list functions. Edit your list first so you actually have data to work with.")
           
    while True:
        try:
            print("Choose one of the following options. Type numbers ONLY!")
            choice = input("""1. Edit List
2. Return the value at an index position
3. Random choice
4. Linear Search
5. Recursive Binary Search
6. Iterative Binary Search
7. Print List
8. Clear List
9. End Program """)
            if choice == "1":
                editList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                randomSearch()
            elif choice == "4":
                linearSearch()
            elif choice == "5":
                binSearch = input("What number are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "6":
                  binSearch = input("What number are you looking for?  ")
                  result = iterativeBinarySearch(unique_list, int(binSearch)) #output of the search is equal to the variable result.
                  if result != -1: #if does not equal is the !
                      print("Your number is at index position {}".format(result))
                  else:
                      print("Your number was not found in that list, buddy!")  
            elif choice == "7":
                printList()
            elif choice =="8":
                clearList()
            else:
                print("Goodbye!")
                break
        except:
            print("An error occurred")
            
    
def editList():
    print("""Here are the ways you can edit your list.
    Type in the number that correlates to your desire."""  )
    edit = input("""
1.Add a single value
2.Add multiple values
3.Remove a value""" )
    if edit == "1":
        addToList()
    elif edit == "2":
        addABunch()
    else:
        byeBye = input("What value do you want to remove?")
        byeBye = int(byeBye)

        while byeBye in unique_list:
            unique_list.pop = unique_list.index(int(byeBye))
        print("{} has been removed from your list".format(byeBye))
        


def addToList():
    change = input("Which list do you want to add to, sorted or unsorted?")
    if change.lower() == "sorted":
        newItem = input("Please type an integer")
        unique_list.append(int(newItem))
        unique_list.sort()
        see = input("Do you want to see your list? Y/N")
        if see.lower() == "y":
            print(unique_list)
        else:
            pass
    else:
        newItem = input("Please type an integer")
        myList.append(int(newItem))
        look = input("Do you want to see your list? Y/N")
        if look.lower() == "y":
            print(myList)
    
            
def addABunch():
    print("We're gonna add a bunch of numbers.")
    numToAdd = input("How many integers do you want to add?   ")#numbers
    numRange = input("And how high would you like these numbers to go?  ")#range the things that we need
    for x in range (0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    print("Your list is now complete!")
    showMe = input("Type 'print' to print your list")
    if showMe.lower() == "print":
        printList()
    else:
        pass
              
    
def clearList():
    unique_list.clear()
    print("Your list is now cleared, nothing is stored in it now.")

def printList():
    print(unique_list)

        
def indexValues():
    indexPos = input("At what index position would you like to see? ")
    print(myList[int(indexPos)-1])

def randomSearch():
    print("Here's a random value from your list")
    print(myList[random.randint(0,len(myList)-1)])
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

def iterativeBinarySearch(unique_list, x): #how to use this search method to remove all doubled items from the list?
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
    return -1   #return makes something available to the user. almost like an output that the computer uses again. Used recursively. Truthy and falsey statements.
                
            




if __name__ == "__main__":
    mainProgram()
