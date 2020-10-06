
seq1 = "0actcg"
seq2 = "acagtag"
gap = -1
mismatch = 0
match = 1
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
traceTable = []
for i in range(len(seq1)):
    column = []
    for j in range(len(seq2)+1):
        column.append(0)
    traceTable.append(column)
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
for i in table:
    print(i)
for j in traceTable:
    print(j)
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
sequence1 = ""
sequence2 = ""

chars1 = seq1[-1]


