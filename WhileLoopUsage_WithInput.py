import time
var1 = 0
vi = input("Percentage to achieve:")
while var1 != int(vi) + 1:
    print ("Loading...", var1,"%")
    #(a = a + b)  Es lo mismo que... (a += b)
    time.sleep (0.3)
    var1 += 1
print("Ready!")
