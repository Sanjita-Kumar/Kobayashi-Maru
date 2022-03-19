def weapon():
      print()
      print("Choose your weapon.")
      
      Choice = str(input("Do you want a phaser as your weapon? "))
      if Choice in('YES','Yes','yes'):
        print()
        print("Energy shields are at 100%")
        print()
        print("                YOU FAIL!")
        
      if Choice in('NO','No','no'):
        Choice = str(input("Do you want a photon torpedos? "))
        if Choice in('yes','YES','Yes'):
          print()
          print("You defeated the klingons and beamed the survivers only to be beamed to Apollo's planet to worship him. ")
          print()
          print("                YOU FAIL!")
        
        if Choice in('NO','No','no'):
          print()
          print("You beamed tribble aboard the enemy ship but a single tribble was left on your ship and your ship suffocates")
          print()
          print("               YOU FAIL!")
          
print("WELCOME TO THE KOBAYASHI MARU STIMULATION")
print()
NAME= str(input("What is your star trek name?  "))
print()
Choice =str(input("Captain "+NAME+" we have received a distress call. Would you like to ignore  it? "))

if Choice in ('Yes','YES','yes'):
  print()
  print("Your crew has turned against you due to your lack of morals.")
  print()
  print("               YOU FAIL! ")

if Choice in ('no','NO','No'):
  print()
  Choice= str(input("Do you enter the Klingon neutral zone to save the ship? "))
  
  if Choice in ('no','No','NO'):
    print()
    Choice = str(input("Will you send an unarmed vessel? "))
    if Choice in('no','No','NO'):
      weapon()
      
    if Choice in ('Yes','YES','yes'):
      print()
      print("Ship absorbed by Amoeba.")
      print("          YOU FAIL! ")
      
    Choice = str()
    
  if Choice in('Yes','YES','yes'):
    print()
    Choice= str(input("Klingon ship emerges from deep space. Do you want to try Diplomacy? "))
    
    if Choice in('no','No','NO'):
      weapon()  
       
    if Choice in ('yes','Yes','YES'):
      print()
      print("You beamed over Mccoy to negotiate. He is the worst diplomat.")
      print()
      print("        YOU FAIL! ")
  