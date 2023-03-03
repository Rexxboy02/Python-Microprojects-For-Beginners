import time
error = 0
while error == 0 :
    try:
        vi = int(input("Porcentaje a alcanzar: "))
        for num in range (vi):
            print (f"Loading...{num + 1}%")
            time.sleep (0.3)
        print("Ready")
        error = 1
    except:
        print("Solo se permite el uso de números, por favor, introduzca el valor numérico:")
#mejorado en base a feedback de:
#https://www.reddit.com/r/learnpython/comments/11gxdfq/first_project_ive_done/
