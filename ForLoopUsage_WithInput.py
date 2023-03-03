import time
vi = int(input("Porcentaje a alcanzar: "))
for num in range (vi):
    print (f"Loading...{num}%")
    time.sleep (0.3)
    num += 1
print("Ready")

#mejorado en base a feedback de:
#https://www.reddit.com/r/learnpython/comments/11gxdfq/first_project_ive_done/
