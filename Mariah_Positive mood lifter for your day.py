#features used:
#A for loop
#Random numbers
#String formatting
#An if/elif/else statement

#Goal of program:
#-To give users randomized quotes that they can use as reassurance throughout their day.
#-Offers a check in of how the quote made them feel/how it effected them. 
import random
print("""
~Positive Mood Lifter For Your Day~

Welcome. It might be strange for you to feel calm with the help of a computer
but I assure you, if you just trust me and lean into your own breathing and senses
for guidance, we will have a lovely time together.
""")

posQuotes = ["It's only when you have the courage to step off the ledge that you'll realize you've had wings all along.",
"Trust is knowing that we're exactly where we are supposed to be in life, especially when it doesn't feel like it.",
"Everything starts from gratitude. Everything. From there, all else lines up for you.",
"Never underestimate the power of an unlimited being--YOU",
"Your actions, thoughts and words today are but seeds for tomorrow’s garden. ",
"Gratitude must be part magic, for when I fill my heart with gratitude, anything is possible.",
"When you surround yourself with people who support your dreams, you will achieve success morequickly."
"Instead of cursing the darkness, be the one to light a candle.",
"You were born an in!nite being with unlimited potential--and you still are that magni!cence.",
"Take love with you in all things that you do and leave only ripples of kindness behind you",
"Adversity provides the opportunity for the best part of us to shine." ,
"Challenge is nothing more than a seed of opportunity. "
            ]
#fix .format
#make sure y and n works
hello = input("What is your name?"){}.format
print("Good to have you here {}")

ready = input("I will randomly select a quote to brigten your day. Ready? Y/N   ")
if ready == "n":
    print("Ok, I can wait a minute. Type y when you are ready.")
else :
    for x in range: 
        random_index = random.randint(0,len(posQuotes)-1)

    print(posQuotes[random_index])

