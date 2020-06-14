phone = input("Phone: ")
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
output = ""
for i in phone:
    output += digits.get(i, "!") + " "
print(output)
