import random
a= random.randint(1,100)
print("Hii, This is a number guessing game\nyou will get 7 chances to guess the number\nWith each guess you will be told if your guess is higher or lower than the number\nGood Luck!")
chances=7
while chances>0:
  guess=int(input("Enter your guess: "))
  if guess==a:
    print("You guessed it right")
    break
  elif guess>a:
    print("Your guess is higher than the number")
  elif guess<a:
    print("Your guess is lower than the number")
  chances-=1
if chances==0:
  print("You lost :( the number was",a)
  