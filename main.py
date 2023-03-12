def sing(n):
    if (n==1):
        objects = "bottle"
        objectminusone = "bottles"
    elif (n==2):
        objects = "bottles"
        objectminusone = "bottle"
    else:
        objects = "bottles"
        objectminusone = "bottles"

    if n >0:
        print(str(n), objects, "of beer on the wall", str(n), objects, "of beer on the wall")
        print("take one down and pass it around, now there is" ,str(n-1), objectminusone, "on the wall")

    elif n ==0:
        print("No more bottles of beer on the wall, no more bottles of beer.")

    else:
        print("wheres the booze ")

bottles = 22
while bottles >=0 :
    sing(bottles)
    bottles = bottles -1
