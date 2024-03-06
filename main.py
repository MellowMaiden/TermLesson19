#Lesson 19 Term2
#Dictionaries

#Examole 1
myDict={
    "one":1,
    "two":2,
    "three":3
}
print(myDict["two"])
#we made our first dictionary in python
#one two three are the KEYS
#1 2 3 are the VALUES

#Example 2
aStudent={
    "name":"Stephen",
    "year":1900,
    "year":1984
}
print(aStudent["year"])

#Example 3
studentStephen={
    "name":"stephen easley walsh",
    "year":1984,
    "paid":True,
    "subjects":["AES","MATH","PROGRAMMING","PHYSICS"]
}
studentJcak={
    "name":"jack pumpkin",
    "year":1990,
    "paid":False,
    "subjects":["AES","MATH","PROGRAMMING","Chemistry"]
}
print(studentStephen["name"],"is studying",studentStephen["subjects"])
print(studentJcak["name"],"was born in",studentJcak["year"])

#Example 4
studentStephen={
    "name":"stephen easley walsh",
    "year":1984,
    "paid":True,
    "subjects":["AES","MATH","PROGRAMMING","PHYSICS"]
}
studentJcak={
    "name":"jack pumpkin",
    "year":1990,
    "paid":False,
    "subjects":["AES","MATH","PROGRAMMING","Chemistry"]
}
studentLeo={
    "name":"Leo pumpkin",
    "year":1990,
    "paid":False,
    "subjects":["AES","MATH","PROGRAMMING","Chemistry"]
}
students=[studentStephen,studentJcak,studentLeo]
for student in students:
    if student["paid"]==False:
        print(student["name"],"has not paid!")

#Example 5
points = []
while True:
    try:
      x=int(input("x:"))
      y=int(input("y:"))
      point={
          "x":x,
          "y":y
      }
      points.append(point)
      print(x,",",y,"was added to the list")
    except:
      break
print(points)

#Example 6
menu={
    "breakfast":"bran flakes",
    "lunch":"curry pot",
    "supper":"pizza"
}
print(menu["lunch"])
menu["lunch"]="subway"
print(menu["lunch"])
