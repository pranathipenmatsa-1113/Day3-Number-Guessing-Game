secret=10
guess=int(input("guess a number:"))
if guess>secret:
    print("To High")
elif guess<secret:
    print("To Low")
else:
    print("Correct Guess!")

print("\nProgram Executed Successfully:")
input("Press enter to exit....")
