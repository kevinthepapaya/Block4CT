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


    
def mainProgram():
    while True:
        try: 
            print ("Hello!")
            print("Choose one of the following options. Type numbers ONLY!")
            choice = input("""1. Add to list,
                            2. Return the value at an index position
                            3. Random choice
                            4. End Program """)
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice== "3":
                randomSearch()
            else:
                break
        except:
            print("An error occurred")
    
def addToList():
    newItem = input("Please type an integer")
    myList.append(int(newItem))
    print(myList)
    
        
def indexValues():
    indexPos = input("At what index position would you like to see? ")
    print(myList[int(indexPos)-1])

def randomSearch():
    print("Here's a random value from your list")
    print(myList[random.ranint(0,len(myList)-1)])




if __name__ == "__main__":
    mainProgram()
