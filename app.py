from sys import *

def saveFile(code):
    try:
        file = open(argv[1],"w")
        for line in code:
            file.write(line+"\n")
        print("end")
    except:
        fileName = input("file?> ")
        file = open(fileName,"w")
        for line in code:
            file.write(line+"\n")
        print("end")

def viewFile(code):
    for line in code:
        print(line)

posLine = 1

def updateLine(line):
    global posLine
    posLine = line

code = []
CopyList = []

def main():
    global code
    global posLine
    line = posLine
    while True:
        try:
            line = len(code)+1
            lineC = input(f'{line}> ')
            if lineC == "":
                inp = input(">> ")
                if inp == "save":
                    saveFile(code)
                elif inp == "save&":
                    saveFile(code)
                    break
                elif inp == "quit" or inp == "exit":
                    break
                elif inp == "load":
                    fn = input("FILE> ")
                    f = open(fn,"r").read()
                    code = f.split("\n")
                    line = len(code)+1
                    posLine = 1
                    main()
                    break
                elif inp == "view":
                    print("-"*45)
                    viewFile(code)
                    print("-"*45)
                else:
                    print("input error")
            elif lineC == "[A":
                lineC = input(f"{line-1}> ")
                code[line-2] = lineC
                updateLine(line-2)
                main()
                break
            elif lineC == "[B":
                lineC = input(f"{line-1}> ")
                code[line+1] = lineC
                updateLine(line+1)
                main()
                break
            elif lineC == "[C":
                lineC = input(f"{line}: COPY> ")
                CopyList.append(lineC)
                code.append(lineC)
            elif lineC == "[D":
                lineC = CopyList[-1]
                code.append(lineC)
            else:
                code.append(lineC)
        except KeyboardInterrupt:
            print("> key error")
            break
main()
