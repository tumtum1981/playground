# enter a value
# tests valid (with python do this... i.e. strip off whitespace)
# loop chars in string
# generate integer
# print return


def GetIntValueOfChar(character):
    if character == "1": return 1
    elif character == "2": return 2
    elif character == "3": return 3
    elif character == "4": return 4
    elif character == "5": return 5
    elif character == "6": return 6
    elif character == "7": return 7
    elif character == "8": return 8
    elif character == "9": return 9
    else: return 0




valueAsString = input("Good day, please enter a value:")
valueAsInt = 0;
sign=1

for character in valueAsString:
    # check for -ve sign or dots or non ints
    if character == "-":
        sign = -1
        continue
    processText = "processing character {}"
    print(processText.format(character))
    valueAsInt *= 10
    valueAsInt += GetIntValueOfChar(character)

valueAsInt *= sign
outputTest = "I have calculated the integer value to be {}"
print(outputTest.format(valueAsInt))