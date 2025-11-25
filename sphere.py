# inspiration code for Python Unit Testing Project
import math

def SurfaceArea(rad):
    area = 4 * math.pi * rad * rad
    return area

def volume(rad):
    vol = (4/3) * math.pi * rad * rad * rad
    return vol

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    sa = SurfaceArea(radius)
    vol = volume(radius) 
   
    print(f"\nThe surface area is: {sa}")
    print(f"\nthe volume is: {vol}\n")

if __name__ == '__main__':
    prompt()
