import random
import time
mystr = "This is a sentance about the hobgoblin Jace"
list_of_words = mystr.split() #if we specify nothing, it will split on " "
print(list_of_words)
list_of_words[-1] = "Mykita" 
print(list_of_words)
mystr = " ".join(list_of_words)
print(mystr)
#simulated csv (comma seperated values)
str2 = "name,type,strength,health"
p1 = "zach,orc,5,1"
p2 = "Isaac,loot goblin,1,5"
headers = str2.split(",")
p1list = p1.split(",")
p2list = p2.split(",")

#iterate through p1list with index and value (with enumerate)
for idx, val in enumerate(p1list):
    print(f"{headers[idx]}: {val}")


for idx, val in enumerate(p2list):
    print(f"{headers[idx]}: {val}")


playerlists = [p1list,p2list]
p1list.append(0)
p2list.append(0)
wins = [0,0]
playerlists = [p1list,p2list]
print(f"it's the big battle of {p1list[0]} vs {p2list[1]}!")
input("Press enter to continue")
for i in range(5):
    print(f"Round {i+1}")
    choice = random.randint(0,2)
    outcomes = []
    if choice < 2:
        attacker = playerlists[choice]
        defender = playerlists[1-choice]
        outcomes.append(attacker[0])
        playerlists[choice][-1] += 1 
        print(f"{attacker[0]} delivered {attacker[2]} damage to {defender[0]} and defeated him/her ")
    else:
        outcomes.append("tie")
        print("Twas a tie")
    time.sleep(1)
print(f"{p1list[0]} won {p1list[-1]} rounds")
print(f"{p2list[0]} won {p2list[-1]} rounds")
print("f")