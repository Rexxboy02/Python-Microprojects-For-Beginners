import time
error = 0
#added while-loop + try-except to handle errors when entering strings with text on the input
while error == 0 :
    try:
        vi = int(input("Porcentaje a alcanzar: "))
        for num in range (vi):
            print (f"Loading...{num + 1}%")
            time.sleep (0.3)
        print("Ready")
        error = 1
    except:
        print("Only numbers are allowed, please, enter a number:")
        
#updated based on:
#https://www.reddit.com/r/learnpython/comments/11gxdfq/first_project_ive_done/
#https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/more-conditional-structures

#this script runs a countdown until it reaches the number from the input
