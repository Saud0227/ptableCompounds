# Python program to read
# json file


import json
name = []
symbol = []
numb = []
molM = []

# Opening JSON file
with open("Array_Elements_Ptable.csv", "r") as csvF:
    row = [i for i in csvF]
    for i in row:
        raw_row=i.strip().split(",")
        name.append(raw_row[0])
        symbol.append(raw_row[1])
        numb.append(raw_row[2])
        molM.append(raw_row[3])


active = True
cmdStr = ["exit"]
cmd = [cmd_quit]




def cmd_quit():
    active = False



while active:
    ci = input(">")
    try:
        cmdStr.index(ci)
        
    if ci in cmdStr:
        print("!")
        #cmd[]
    print(ci)