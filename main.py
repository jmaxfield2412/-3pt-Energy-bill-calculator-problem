#Write a subroutine that will output the raw cost of energy usage by taking 3 parameters:
#previous reading, current reading, calorific value 
PreReading = int(input("What was the previous reading? "))
CReading = int(input("What is the current reading? "))
C = 39.3

#Subroutine to find the cost:
def Cost(C):
  return (((PreReading - CReading) * 1.022 * C / 3.6) * 0.0284)

#Main programme
X = Cost(C) 
Y = round(X,2)
print("£",Y)