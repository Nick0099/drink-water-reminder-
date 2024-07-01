import time
N = input("what is you name? ")
Name = N.capitalize()
# greeting user
hour = time.strftime('%H%M')
if hour >= '00:00' and hour < '12:00':
  print("\nGood Morning ", Name)
elif hour >= '12:00' and hour < '16:00':
  print("\nGood Afternoon ", Name)
elif hour >= '16:00' and hour < '20:00':
  print("\nGood Evening ", Name)
else:
  print("\nGood Night ", Name)

# user input
age = int(input("\nwhat is your age?\n"))
wt = input("\nwhen was the last time you had water?\n")
sex = input("\nAre you biologically male or female(m/f)?\n").upper()
height = float(input("\nwhat is your height in centimeters?\n"))
weight = float(input("\nEnter weight in kgs\n"))
pi = int(
    input(
        "\nHow often do you exercise \n 1.Sedentary(little or no exercise) \n 2.Lightly active (light exercise/sports 1-3 days/week)\n 3.Moderately active (moderate exercise/sports 3-5 days/week):\n4.Very active (hard exercise/sports 6-7 days a week)\n5. Super active (very hard exercise/physical job & exercise 2x/day){choose from 1-5}:\n\n"
    ))
# calculates how much ml of water we should drink every day
wi = 0
BMRm = float((88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)))
BMRf = float((447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)))
if sex == "M":
  if pi == 1:
    wi = (BMRm * 1.2)
  elif pi == 2:
    wi = (BMRm * 1.375)
  elif pi == 3:
    wi = (BMRm * 1.55)
  elif pi == 4:
    wi = (BMRm * 1.725)
  elif pi == 5:
    wi = (BMRm * 1.9)
else:
  if pi == 1:
    wi = (BMRf * 1.2)
  elif pi == 2:
    wi = (BMRf * 1.375)
  elif pi == 3:
    wi = (BMRf * 1.55)
  elif pi == 4:
    wi = (BMRf * 1.725)
  elif pi == 5:
    wi = (BMRf * 1.9)
print(
    f"\n\nYou need to drink around {wi} ml of water in a day we will remind you 5 times a day every day\n\n"
)
# divides how much water you will need to drink into 6 equal parts 
cups_a_day = wi / 6
print(
    f"You need to drink 6 cups a day,\nyou will be reminded to you by us 5 times a day  and remeber to drink {cups_a_day*2}ml of water during exercise by yourself"
)

i = 0
while i < 365:
  
  j=0
  while j == 5:
     # it will run every minute until the one of the given condition is true after that it will run everyday for a year
    if time.strftime('%H%M') == "0630":
      print(f"Good morning!{Name}, Drink {cups_a_day}ml of water.")
      j=j+1
      time.sleep(1800)
    elif time.strftime('%H%M') == "0700":
      print(f"Time for breakfast!, Drink {cups_a_day}ml of water before breakfast.")
      j=j+1
      time.sleep(18000)
    elif time.strftime('%H%M') == "1200":
      print(f"Lunch time!, Drink {cups_a_day}ml of water before lunch.")
      j=j+1
      time.sleep(21600)
    elif time.strftime('%H%M') == "0600":
      print(f"Dinner time!, Drink {cups_a_day}ml of water before dinner.")
      j=j+1
      time.sleep(14400)
    elif time.strftime('%H%M')=="1000":
      print(f"Good night!{Name}, Drink {cups_a_day}ml of water before bed.")
      j=j+1
      time.sleep(30600)
    else:
      time.sleep(60)
  
i=i+1    
