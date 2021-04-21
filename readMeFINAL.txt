Program Directions:
1.The program will give you a list of options. Type in #1 to choose "Edit List" so you can add values to your list.
We have to create a list so we have data to work with. 
2.Edit List will give you 3 options: 	1.Add a single value, 
					2. Add multiple values, 
					3. remove item from list. 

Choose option 1 or 2 to add values to your list.
3.If you chose 1, type in the numerical value you want to add. Be sure to press enter after.
4.If you chose 2, type in how how many numbers you want to generate as well as how high you want them to go. Be sure to press enter after.
5.The initial list of options will appear again after you hit enter. This menu list will appear after the program runs any of the options. 
6.Once you have data in your list, you can choose any of the functions, listed 1-9.
7.Simply type in the number that correlates to your desire, press enter and let the program do it's thing!

	-If you don't create a list first, you will simply not have any data to work with, and the program will inform you that an error has occured.
	If during the running of the program an error occurs, or you enter in something that doesn't compute, it will print "An error occurred"
	before printing the menu list again.

	-If you add a single value, the program will let you choose which list to add to.
	-If you add multiple values, we have to create two lists, one that will have all the generated values, and one that will take the
	values and sort them from lowest to highest. By creating a sorted list, it makes it much easier to search through (using a binary
	search algorithm) to find specific values.
  
Section 2: Binary Search
How binary search works:Binary searches function on conditionals, primarily by comparing a the value you are searching
for to the midpoint, and then based on if the value is < = or > the value, making the list shorter to narrow in on your value.
Both recursive searches and iterative searches accomplish the same thing, by iterating through your list and using conditionals
to test the value you are looking against the mid value. If your value is greater than mid, it redefines low to be mid+1, so you eliminate
the whole part of your list that doesn't contain your value. Each function cycles through this (the same thing happens if your value is less
than mid, then the top of the list is eliminated) however they just do it in a slightly different ways.

Recursive algorithm: The recursive binary algorithm uses recursion as the method for iteration. This just means that it calls iteself as a
function within itself, and only stops when high=low. This is a very quick way to search for a value, but you run the risk of overloading
your little computer. I mean who know, you might be the kind of user that wants to add 3000000000 numbers to your list and then search through them
recursively, and your computer would crash, or at least freeze. So if you ARE that kind of person, please, for the love of god, use the iterative search, as 
explained BELOW.
Iterative algorithm: The iterative binary search sets up the same conditionals as the recursive search, however it's method for using repetition to search 
through the list is done by the use of a while loop. It runs while low <= high, and when they are equal, it stops. The difference is that the recusive search
calls itself (not using a while loop) until high=low. 



Section 3: Changes you made/want to make
I wanted to change the initial menu that printed, so I took the addABunch and addToList functions and grouped them together under a new function called editList.
This made the inital menu shorter and also allowed me to create a way for users to remove a value from their list by using the .pop() method. I also made it so the
user could clear both lists. I think it would be a good idea to have this called under editList, as well as to give the user an option of which lis they want to clear. 
Here is the code for editList. The only really new thing is the remove option, other than that I just reorganized.
 
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
        unique_list.pop(byeBye)
        print("{} has been removed from your list".format(byeBye))
