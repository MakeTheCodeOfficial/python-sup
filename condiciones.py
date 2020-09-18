#Are you underage?

#Input
def inputValue(repeat):
    if repeat == False:
        try:
            age = int(input("Put your age: "))
            if age >= 18:
                print("You can pass. You're an adult.")
            elif age <= -1:
                 print("Not valid age. Please DO NOT use negative numbers.")
                 inputValue(False)
            else:
                print("You can't pass, you're under age.")
        except ValueError:
            print("ValueError detected. Please DO NOT use letters or decimals.")
            inputValue(False)

inputValue(False)
