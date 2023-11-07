#Encode.
encodeDict = {
    "a": "^",
    "b": "@",
    "c": "$",
    "d": "#",
    "e": "*",
    "f": "%",
    "g": ">",
    "h": "`",
    "i": "+",
    "j": "/",
    "k": "!",
    "l": "-",
    "m": "~",
    "n": "|",
    "o": "?",
    "p": "<",
    "q": ".",
    "r": ";",
    "s": "&",
    "t": "{",
    "u": "=",
    "v": "_",
    "w": "(",
    "x": "]",
    "y": "}",
    "z": ")",
    "!": "q",
    ".": "w",
    ",": "e",
    "(": "r",
    ")": "t",
    "-": "y",
    "'": "o",
    "0": "l",
    "1": "a",
    "2": "k",
    "3": "s",
    "4": "j",
    "5": "d",
    "6": "h",
    "7": "f",
    "8": "g",
    "9": "x",
    ";": "p",
    "?": "c",
    "/": "v",
    ":": "b",
    " ": "z"
    }
encodeDict2 = {
    "^": "a",
    "@": "b",
    "$": "c",
    "#": "d",
    "*": "e",
    "%": "f",
    ">": "g",
    "`": "h",
    "+": "i",
    "/": "j",
    "!": "k",
    "-": "l",
    "~": "m",
    "|": "n",
    "?": "o",
    "<": "p",
    ".": "q",
    ";": "r",
    "&": "s",
    "{": "t",
    "=": "u",
    "_": "v",
    "(": "w",
    "]": "x", 
    "}": "y",
    ")": "z",
    "q": "!",
    "w": ".",
    "e": ",",
    "r": "(",
    "t": ")",
    "y": "-",
    "o": "'",
    "l": "0",
    "a": "1",
    "k": "2",
    "s": "3",
    "j": "4",
    "d": "5",
    "h": "6",
    "f": "7",
    "g": "8",
    "x": "9",
    "p": ";",
    "c": "?",
    "v": "/",
    "b": ":",
    "z": " "
    }
def function():
    message = input("Enter your message here: ")
    messageLower = message.lower()
    length = len(messageLower)
    number = 0
    lst = []
    lst2 = []
    lst2.extend(messageLower)
    for i in range(0, length):
        if lst2[number] == "a":
            number += 1
            lst.append(str(encodeDict["a"]))
        elif lst2[number] == "b":
            number += 1
            lst.append(str(encodeDict["b"]))
        elif lst2[number] == "c":
            number += 1
            lst.append(str(encodeDict["c"]))
        elif lst2[number] == "d":
            number += 1
            lst.append(str(encodeDict["d"]))
        elif lst2[number] == "e":
            number += 1
            lst.append(str(encodeDict["e"]))
        elif lst2[number] == "f":
            number += 1
            lst.append(str(encodeDict["f"]))
        elif lst2[number] == "g":
            number += 1
            lst.append(str(encodeDict["g"]))
        elif lst2[number] == "h":
            number += 1
            lst.append(str(encodeDict["h"]))
        elif lst2[number] == "i":
            number += 1
            lst.append(str(encodeDict["i"]))
        elif lst2[number] == "j":
            number += 1
            lst.append(str(encodeDict["j"]))
        elif lst2[number] == "k":
            number += 1
            lst.append(str(encodeDict["k"]))
        elif lst2[number] == "l":
            number += 1
            lst.append(str(encodeDict["l"]))
        elif lst2[number] == "m":
            number += 1
            lst.append(str(encodeDict["m"]))
        elif lst2[number] == "n":
            number += 1
            lst.append(str(encodeDict["n"]))
        elif lst2[number] == "o":
            number += 1
            lst.append(str(encodeDict["o"]))
        elif lst2[number] == "p":
            number += 1
            lst.append(str(encodeDict["p"]))
        elif lst2[number] == "q":
            number += 1
            lst.append(str(encodeDict["q"]))
        elif lst2[number] == "r":
            number += 1
            lst.append(str(encodeDict["r"]))
        elif lst2[number] == "s":
            number += 1
            lst.append(str(encodeDict["s"]))
        elif lst2[number] == "t":
            number += 1
            lst.append(str(encodeDict["t"]))
        elif lst2[number] == "u":
            number += 1
            lst.append(str(encodeDict["u"]))
        elif lst2[number] == "v":
            number += 1
            lst.append(str(encodeDict["v"]))
        elif lst2[number] == "w":
            number += 1
            lst.append(str(encodeDict["w"]))
        elif lst2[number] == "x":
            number += 1
            lst.append(str(encodeDict["x"]))
        elif lst2[number] == "y":
            number += 1
            lst.append(str(encodeDict["y"]))
        elif lst2[number] == "z":
            number += 1
            lst.append(str(encodeDict["z"]))
        elif lst2[number] == "!":
            number += 1
            lst.append(str(encodeDict["!"]))
        elif lst2[number] == ".":
            number += 1
            lst.append(str(encodeDict["."]))
        elif lst2[number] == ",":
            number += 1
            lst.append(str(encodeDict[","]))
        elif lst2[number] == " ":
            number += 1
            lst.append(str(encodeDict[" "]))
        elif lst2[number] == "(":
            number += 1
            lst.append(str(encodeDict["("]))
        elif lst2[number] == ")":
            number += 1
            lst.append(str(encodeDict[")"]))
        elif lst2[number] == "-":
            number += 1
            lst.append(str(encodeDict["-"]))
        elif lst2[number] == "'":
            number += 1
            lst.append(str(encodeDict["'"]))
        elif lst2[number] == "0":
            number += 1
            lst.append(str(encodeDict["0"]))
        elif lst2[number] == "1":
            number += 1
            lst.append(str(encodeDict["1"]))
        elif lst2[number] == "2":
            number += 1
            lst.append(str(encodeDict["2"]))
        elif lst2[number] == "3":
            number += 1
            lst.append(str(encodeDict["3"]))
        elif lst2[number] == "4":
            number += 1
            lst.append(str(encodeDict["4"]))
        elif lst2[number] == "5":
            number += 1
            lst.append(str(encodeDict["5"]))
        elif lst2[number] == "6":
            number += 1
            lst.append(str(encodeDict["6"]))
        elif lst2[number] == "7":
            number += 1
            lst.append(str(encodeDict["7"]))
        elif lst2[number] == "8":
            number += 1
            lst.append(str(encodeDict["8"]))
        elif lst2[number] == "9":
            number += 1
            lst.append(str(encodeDict["9"]))
        elif lst2[number] == ":":
            number += 1
            lst.append(str(encodeDict[":"]))
        elif lst2[number] == ";":
            number += 1
            lst.append(str(encodeDict[";"]))
    code = str(lst)
    code2 = code.replace("'", "")
    code3 = code2.replace(",", "")
    code4 = code3.replace("[", "")
    code5 = code4.replace("]", "")
    code6 = code5.replace(" ", "")
    print(code6)
    q = input("Would you like to document this? ")
    if q == "yes" or q == "Yes":
        f = open("decodeMe" + ".txt", "a")
        f.write("\n\n" + code6)
        f.close()
    else:
        print("Ok")
def function2():
    message = input("Enter your message here: ")
    messageLower = message.lower()
    length = len(messageLower)
    number = 0
    lst = []
    lst2 = []
    lst2.extend(messageLower)
    for i in range(0, length):
        if lst2[number] == "^":
            number += 1
            lst.append(str(encodeDict2["^"]))
        elif lst2[number] == "@":
            number += 1
            lst.append(str(encodeDict2["@"]))
        elif lst2[number] == "$":
            number += 1
            lst.append(str(encodeDict2["$"]))
        elif lst2[number] == "#":
            number += 1
            lst.append(str(encodeDict2["#"]))
        elif lst2[number] == "*":
            number += 1
            lst.append(str(encodeDict2["*"]))
        elif lst2[number] == "%":
            number += 1
            lst.append(str(encodeDict2["%"]))
        elif lst2[number] == ">":
            number += 1
            lst.append(str(encodeDict2[">"]))
        elif lst2[number] == "`":
            number += 1
            lst.append(str(encodeDict2["`"]))
        elif lst2[number] == "+":
            number += 1
            lst.append(str(encodeDict2["+"]))
        elif lst2[number] == "/":
            number += 1
            lst.append(str(encodeDict2["/"]))
        elif lst2[number] == "!":
            number += 1
            lst.append(str(encodeDict2["!"]))
        elif lst2[number] == "-":
            number += 1
            lst.append(str(encodeDict2["-"]))
        elif lst2[number] == "~":
            number += 1
            lst.append(str(encodeDict2["~"]))
        elif lst2[number] == "|":
            number += 1
            lst.append(str(encodeDict2["|"]))
        elif lst2[number] == "?":
            number += 1
            lst.append(str(encodeDict2["?"]))
        elif lst2[number] == "<":
            number += 1
            lst.append(str(encodeDict2["<"]))
        elif lst2[number] == ".":
            number += 1
            lst.append(str(encodeDict2["."]))
        elif lst2[number] == ";":
            number += 1
            lst.append(str(encodeDict2[";"]))
        elif lst2[number] == "&":
            number += 1
            lst.append(str(encodeDict2["&"]))
        elif lst2[number] == "{":
            number += 1
            lst.append(str(encodeDict2["{"]))
        elif lst2[number] == "=":
            number += 1
            lst.append(str(encodeDict2["="]))
        elif lst2[number] == "_":
            number += 1
            lst.append(str(encodeDict2["_"]))
        elif lst2[number] == "(":
            number += 1
            lst.append(str(encodeDict2["("]))
        elif lst2[number] == "]":
            number += 1
            lst.append(str(encodeDict2["]"]))
        elif lst2[number] == "}":
            number += 1
            lst.append(str(encodeDict2["}"]))
        elif lst2[number] == ")":
            number += 1
            lst.append(str(encodeDict2[")"]))
        elif lst2[number] == "q":
            number += 1
            lst.append(str(encodeDict2["q"]))
        elif lst2[number] == "w":
            number += 1
            lst.append(str(encodeDict2["w"]))
        elif lst2[number] == "e":
            number += 1
            lst.append(str(encodeDict2["e"]))
        elif lst2[number] == "r":
            number += 1
            lst.append(str(encodeDict2["r"]))
        elif lst2[number] == "t":
            number += 1
            lst.append(str(encodeDict2["t"]))
        elif lst2[number] == "y":
            number += 1
            lst.append(str(encodeDict2["y"]))
        elif lst2[number] == "o":
            number += 1
            lst.append(str(encodeDict2["o"]))
        elif lst2[number] == "l":
            number += 1
            lst.append(str(encodeDict2["l"]))
        elif lst2[number] == "a":
            number += 1
            lst.append(str(encodeDict2["a"]))
        elif lst2[number] == "k":
            number += 1
            lst.append(str(encodeDict2["k"]))
        elif lst2[number] == "s":
            number += 1
            lst.append(str(encodeDict2["s"]))
        elif lst2[number] == "j":
            number += 1
            lst.append(str(encodeDict2["j"]))
        elif lst2[number] == "d":
            number += 1
            lst.append(str(encodeDict2["d"]))
        elif lst2[number] == "h":
            number += 1
            lst.append(str(encodeDict2["h"]))
        elif lst2[number] == "f":
            number += 1
            lst.append(str(encodeDict2["f"]))
        elif lst2[number] == "g":
            number += 1
            lst.append(str(encodeDict2["g"]))
        elif lst2[number] == "x":
            number += 1
            lst.append(str(encodeDict2["x"]))
        elif lst2[number] == "p":
            number += 1
            lst.append(str(encodeDict2["p"]))
        elif lst2[number] == "c":
            number += 1
            lst.append(str(encodeDict2["c"]))
        elif lst2[number] == "v":
            number += 1
            lst.append(str(encodeDict2["v"]))
        elif lst2[number] == "b":
            number += 1
            lst.append(str(encodeDict2["b"]))
        elif lst2[number] == "z":
            number += 1
            lst.append(str(encodeDict2["z"]))
    code = str(lst)
    code2 = code.replace("'", "")
    code3 = code2.replace(", ", "")
    code4 = code3.replace("[", "")
    code5 = code4.replace("]", "")
    print(code5)
while 1 == 1:
    question = input("Encode or Decode? ")
    if question == "Encode" or question == "encode":
        function()
    if question == "Decode" or question == "decode":
        function2()
    if question == "finish" or question == "Finish":
        print("CYA!")
        break
        
        
    
