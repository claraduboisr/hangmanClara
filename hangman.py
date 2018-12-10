
solution = input("Choose a word: ")
hidden = ""
errors = ""
max_errors = 5
for letter in solution:
    hidden += "_ "

while hidden != solution and len(errors) < max_errors:

    if len(errors) > 0:
        print("\nWrong letters you have tried: ", end="")
        for letter in errors:
            print(letter, end=" ")

    print("\nWord to find: ", end="")
    for letter in hidden:
        print(letter, end=" ")

    attempt = input("\nTry a letter: ") + " "
    found = False

    if attempt in hidden or attempt in errors:
        print("\nYou already tried with ", attempt)
        continue

    for i, letter in enumerate(solution):
        if letter == attempt:
            temp = list(hidden)
            temp[i] = letter
            hidden = "".join(temp)
            found = True

    if found:
        print("Congrats! The letter is in the word")
    else:
        errors += attempt
        print("Sorry wrong letter, you have", max_errors-len(errors),"errors left")

if len(errors) == max_errors:
    print("\nYou lost!")
else:
    print("\nYou won!")
