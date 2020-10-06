seq1 = "0actcg"
seq2 = "acagtag"
gap = -1
mismatch = 0
match = 1

def BuildTable():
    global gap
    global seq1
    global seq2
    table = []
    for i in range(len(seq1)):
        column = []
        for j in range(len(seq2)+1):
            if j == 0:
                column.append(i * gap)
            elif i == 0:
                column.append(j*gap) 
            else:
                column.append(0)
        table.append(column)
    return table

def BuildTraceTable():
    global seq1
    global seq2
    traceTable = []
    for i in range(len(seq1)):
        column = []
        for j in range(len(seq2)+1):
            column.append(0)
        traceTable.append(column)
    return traceTable 

table = BuildTable()
traceTable = BuildTraceTable()

def FillTable():
    global table
    global traceTable
    global gap
    global match
    global mismatch
    for i in range(1,len(table)):
        for j in range(1,len(table[0])):
            dScore = 0
            if seq1[i] == seq2[j-1]:
                dScore = int(match + table[i-1][j-1])
            else:
                dScore = int(mismatch + table[i-1][j-1])
            topScore = int(table[i-1][j]) + int(gap)
            leftScore = int(table[i][j-1]) + int(gap)
            score = max(dScore,topScore,leftScore)
            table[i][j] = score
            scores = []
            if int(score) == int(topScore):
                scores.append(0)
            if int(score) == int(leftScore):
                scores.append(1)
            if int(score) == int(dScore):
                scores.append(2)
            traceTable[i][j] = scores
FillTable()

for i in table:
    print(i)
for j in traceTable:
    print(j)

def BuildPath():
    global traceTable
    i = len(table)-1
    j = len(table[0])-1

    s1 = ""
    s2 = ""
    path = ""
    # assumes that there is one path and one path only
    while i != 0 and j != 0:
        if traceTable[i][j][0] == 2:
            path += "d"
            i = i-1
            j = j-1
        elif traceTable[i][j][0] == 1:
            path += "l"
            j = j - 1
        elif traceTable[i][j][0] == 0:
            path += "t"
            i = i - 1
    print(path)
    return path

path = BuildPath()



def GetPairwiseAlignment(seq1,seq2):
    seqFinal1 = ""
    seqFinal2 = ""

    seq1 = seq1[::-1]
    seq2 = seq2[::-1]

    seq1Counter = 0
    seq2Counter = 0
    finalScore = 0
    for i in path:
        if i == "d":
            seqFinal1 += seq1[seq1Counter]
            seqFinal2 += seq2[seq2Counter]

            if seq1[seq1Counter] == seq2[seq2Counter]:
                finalScore += match
            else:
                finalScore += mismatch
            seq1Counter += 1
            seq2Counter += 1
        elif i == 'l':
            seqFinal1 += '-'
            seqFinal2 += seq2[seq2Counter]
            seq2Counter += 1
            finalScore += gap
        else:
            seqFinal2 += '-'
            seqFinal1 += seq2[seq1Counter]
            seq1Counter += 1
            finalScore += gap
    print(seqFinal1[::-1])
    print(seqFinal2[::-1])
    print(finalScore)
seq1 = "actcg"
seq2 = "acagtag"
GetPairwiseAlignment(seq1,seq2)