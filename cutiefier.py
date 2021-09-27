# Replace every 'r' in a string with a 'w'.
def replaceRWithW(string):
    string = string.lower()
    replacedString = string.replace("r", "w")
    return replacedString

# Replace every 'r' in a string with an 'uw'.
def replaceUWithUW(string):
    string = string.lower()
    replacedString = string.replace("u", "uw")
    return replacedString

# Replace every 'l' in a string with a 'w'.
def replaceLWithW(string):
    string = string.lower()
    replacedString = string.replace("l", "w")
    return replacedString

# Replace every '{line}' in a string and add a line.
def addLine(string):
    string = string.lower()
    replacedString = string.replace("{line}", "\n")
    return replacedString

# Run or stop the cutiefier() function.
def tryAgain():
    print("")
    cutiefier()

# Make a text cuter :3
def cutiefier():
    text = input("[*] Input your text: ")

    text = addLine(text)

    text = replaceRWithW(text)
    text = replaceUWithUW(text)
    text = replaceLWithW(text)

    print("")
    print(text)

    # Run the tryAgain() function.
    tryAgain()

print("'cutie'-fier v1.1")
print("https://github.com/AbrarRayva")
print("")
print("[*] Tips: Use {line} to add line!")
print("")

# Run the cutiefier() function and check for errors.
try:
    cutiefier()
except:
    print("[*] An error has occurred while trying to run the cutiefier.")

# Run the tryAgain() function. (Just in case if the tryAgain() function inside cutiefier() function not working.)
tryAgain()