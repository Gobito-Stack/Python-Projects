print("Text to number Converter")
numbers = input("Type in number: ")
number_list = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output =""
for number in numbers:
    output += number_list.get(number, "Not a digit")+ " "
print(output)