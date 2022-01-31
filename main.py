# Python program to read
# json file


import json

dat = [[],[],[],[]]

# Opening JSON file
def listSetUp():
    global dat
    with open("Array_Elements_Ptable.csv", "r") as csvF:
        row = [i for i in csvF]
        for i,itm in enumerate(row):
            if i != 0:
                raw_row=itm.strip().split(",")
                dat[0].append(raw_row[0])
                dat[1].append(raw_row[1])
                dat[2].append(int(raw_row[2]))
                dat[3].append(float(raw_row[3]))


def getDat(iChem):
    tmpIt = [i[iChem] for i in dat]
    return(tmpIt)

def cmd_quit():
    global active
    print("Program Exit")
    active = False

def cmd_grepNmr(n):
    if n < 119 and n >= 0:
        return getDat(n-1)




listSetUp()
active = True
cmdStr = ["exit","grepNmr", "grepChem"]
cmd = [cmd_quit]





while active:
    cin = input(">")
    cin = cin.split()
    try:
        ci = cmdStr.index(cin[0])
        # print(ci)
        cmd[ci]()
    except ValueError:
        print("Unknown cmd")
          