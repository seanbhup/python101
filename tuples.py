a_tuple = (1,3,4)
# print a_tuple[2]

# for number in a_tuple:
#     print number
#
# teams = ("Knicks", "Mets", "Jets")
#
# for team in teams:
#     if team == "Knicks":
#         print "CARMELO ANTHONY"
#     elif team == "Mets":
#         print "MATT HARVEY"
#     elif team == "Jets":
#         print "DAVID HARRIS"

# message = raw_input("Please enter the name of your favorite Sean: ")

# height = raw_input("In inches, how tall are you?\n")
# if int(height) >= 42:
#     print "You are tall enough"
# else:
#     print "You're a little baby probs"


# while loop
# current = 1;
# while current < 10:
#     print current;
#     current+=1;
from random import randint
random_number = randint(1,1001)

answer = "blob"
while answer != random_number:
    answer = int(raw_input("Guess a number between 1 and 1000: "))
