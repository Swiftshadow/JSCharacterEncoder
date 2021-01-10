input = raw_input("Enter the text to convert: ")
print(input)
output = "eval("
length = len(input)
counter = 0
for char in input:
    output += "String.fromCharCode(" + str(ord(char) - 1) + " %2B 1)"
    counter = counter + 1
    if counter < length:
        output += " %2B "


output += ")"
print(output)