# Love calculator

# Problem
''' Create a love calculator'''
# Solution
print("*** Welcome to the Love Calculator! ***\n")

# taking imputs
name1 = input("What is your name? \n Name:")
name2 = input("What is their name? \n Name: ")

n1 = name1.lower()
n2 = name2.lower()
T1 = n1.count('t') + n2.count('t') + n1.count('r') + n2.count('r') + \
    n1.count('u') + n2.count('u') + n1.count('e') + n2.count('e')

L1 = n1.count('l') + n2.count('l') + n1.count('o') + n2.count('o') + \
    n1.count('v') + n2.count('v') + n1.count('e') + n2.count('e')
tot = str(T1) + str(L1)

# print(f"Your percentage is {tot}%")
total = int(tot)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and 50 >= total:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

print("Warning: This calcutor is just for fun don't take it too seriously and enjoy your love life.\n ")
print("*** Thank You ***")
