''' Module 3 Assignment '''
#Program-1
import random
def quiz():
  level = str(raw_input("Choose level (easy:E, intermediate:I, and hard:H):")).lower()
  c = int(raw_input("number of question you want to attempt:")) 
  qtype = str(raw_input("Specify the question type (multiplication:M, addition:A, subtraction:S, division:D)")).lower()
  rnum = 0
  if level == "e": 
    l = 0
    h = 5
  elif level == "i": 
    l = 6
    h = 10 
  elif level == "h":
    l = 11
    h = 20 
  while(c > 0):
    rnum = random.randint(l,h) 
    rnum2 = random.randint(l,2*h) 
    if qtype == "d":
      if input("%s divided by %s ="%(rnum2,rnum)) == rnum2/rnum :
        print "Correct!	Go on"
      else:
        print "Wrong. Better Luck"
    elif qtype == "m":
      if input("%s Multiplied by %s ="%(rnum2,rnum)) == rnum2*rnum :
        print "Correct! Go on"
      else:
        print "Wrong. Better Luck"
    elif qtype == "a":
      if input("%s Added to %s ="%(rnum2,rnum)) == rnum2+rnum :
        print "Correct! Go on"
      else:
        print "Wrong. Better Luck"
    elif qtype == "s":
      if input("%s Subtracted By %s ="%(rnum2,rnum)) == rnum2-rnum :
        print "Correct! Go on"
      else:
        print "Wrong. Better Luck"
    c-=1

while(True):
  quiz()
  if(str(raw_input("press 'E' to exit Or Any Other Key to Continue): ")).lower()=="e"):
    break
  

#Program-2
def find_power( x, n=1 ):
	if n==1:
		return x
	elif n<0:
		return 1/find_power(x,-n)
	else:
		return x*find_power(x,n-1)
		
print find_power(3,3)



#Program-4
mylist= [["john", 1, "a"], ["larry", 0, "b"]]
sorted(mylist, key=itemgetter(1))