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
"""
editList()
Function description: The user is given 3 choices for which to edit their list, option
1 and 2 call functions as described below. The 3rd choice allows the user to remove a value from the sorted list.
(I would want to allow the user to choose which list to remove an item from).
We create an input of the value the user wants to remove, force that value into an integer (using int() function),
and then create a while loop so that we go through the list removing the desired value each time it appears.
Using the .pop() function, we remove the desired value.
"""
    
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
#now remove a value isn't working...
        unique_list.pop(byeBye)
        print("{} has been removed from your list".format(byeBye))
        
"""
addToList()
Function Description: We let the user choose which list they want to add to. Then an input
lets the user add a single value to their desired list.
If they want to add to the sorted list, the values automatically get sorted using the .sort() function.
Otherwise the values are added in no specific order.
"""

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
"""
addABunch()
Function Description: We create an input for the distance and range that the user wants to add to their list.
Then, from 0 to the number of values the user wants to add, the function adds random VALUES that
go up to the desired range of the user.
Then we take an extra step to create a seperate list that is sorted, and contains only unique numbers that appeared once
when you generated the random numbers. Then we allow the user to print their compleated list.
"""
            
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

"""
clearList()
Function Description:
Using the .clear() function, we remove everything from the list.
"""    
def clearList():
    unique_list.clear()
    print("Your list is now cleared, nothing is stored in it now.")

"""
printList()
Function Description:
If there is nothing in the sorted list, then we print the unsorted list.
But if there are values in both lists, we give the user a choice of which list they want
to print.
"""

def printList():
    if len(myList) == 0:
        print("Your list is empty!")
    elif len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or un-sorted?")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)
                         
    
   
"""
indexValues()
Function Explanation: we created a variable called 'indexPos',and stored
the result of an input function inside it.

We then force the value stored in indexPos into an integer (using the int() function)
and used that variable to call a value at a specific index position.
"""     
def indexValues():
    indexPos = input("At what index position would you like to see? ")
    print(myList[int(indexPos)-1])

    
"""
randomSearch()
Function Description:
We generate a random number from myList using the random library.
The parameters are that the random number must be in myList, between 0
and the lenght of the list.
If there are values stored in unique_list, we do the same thing, printing a random value.
We have to be sure to subtract 1 from the number of values (len() function) so we have the correct
number of intex values. 
"""
def randomSearch():
    print("Here's a random value from your list")
    print(myList[random.randint(0,len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randint(0,len(unique_list)-1)])
"""
linearSearch()
Function Description:
We create a for loop that runs through the lenght of myList,
and each time that the value you are searching for is found,
we add to indexCount to keep track of how many times the value appears.
"""
def linearSearch():
    print("we're going to search through the list IN THE WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for? Number-wise. ")
    indexCount = 0
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            indexCount = indexCount + 1
            print("Your item is at index {}" .format(x))
    print("You're number appreadred {} times in the list ". format(indexCount))
    
"""
recursiveBinarySearch()
Function Description:
In this function we call unique_list, low, high and x, and then by
comparing the defined mid variable to x, the value you are searching for,
we make the list smaller and smaller, eliminating the part of the list
that does not have our value, until we eventually find our value. If the value
does not exist, then the user is notified of that. 


"""
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
        
"""
iterativeBinarySearch()
Function Description:
We create 3 variables, low, mid and high, as defined at the top
and using coditinals, we run through a while loop that compares the desired value
to the value of mid. If the desired value is lower than mid, we are able to eliminate the whole
upper half of the list because we know we only have to search through part of the list. We do
this until the desired value is found.

"""
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
