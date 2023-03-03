import time
vi = int(input("Porcentaje a alcanzar: "))
for num in range (vi):
    print (f"Loading...{num}%")
    time.sleep (0.3)
print("Ready")

#updated based on feedback from:
#https://www.reddit.com/r/learnpython/comments/11gxdfq/first_project_ive_done/
