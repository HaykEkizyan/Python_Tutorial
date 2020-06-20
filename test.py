def convertTabs(code, x):
    return code.replace("\t", " " * x)

print(convertTabs("\tyield\t", 7))