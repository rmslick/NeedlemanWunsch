class NeedWunsch():
    def __init__(self, seq1, seq2, gap, mismatch, match):
        self.seq1 = seq1.lower()
        self.seq2 = seq2.lower()
        self.gap = gap
        self.mismatch = mismatch
        self.match = match
        self.table = []
        self.traceTable = []
        self.path = ""
    def BuildTable(self):
        table = []
        seq1 = '0'+self.seq1 #0 inserted for top right
        for i in range(len(seq1)):
            column = []
            for j in range(len(self.seq2)+1):
                if j == 0:
                    column.append(i * self.gap)
                elif i == 0:
                    column.append(j*self.gap) 
                else:
                    column.append(0)
            table.append(column)
        return table
    def BuildTraceTable(self):
        seq1 = '0'+self.seq1
        traceTable = []
        for i in range(len(seq1)):
            column = []
            for j in range(len(self.seq2)+1):
                column.append(0)
            traceTable.append(column)
        return traceTable 
    def FillTable(self):
        seq1 = '0'+self.seq1
        for i in range(1,len(self.table)):
            for j in range(1,len(self.table[0])):
                dScore = 0
                if seq1[i] == self.seq2[j-1]:
                    dScore = int(self.match + self.table[i-1][j-1])
                else:
                    dScore = int(self.mismatch + self.table[i-1][j-1])
                topScore = int(self.table[i-1][j]) + int(self.gap)
                leftScore = int(self.table[i][j-1]) + int(self.gap)
                score = max(dScore,topScore,leftScore)
                self.table[i][j] = score
                scores = []
                if int(score) == int(topScore):
                    scores.append(0)
                if int(score) == int(leftScore):
                    scores.append(1)
                if int(score) == int(dScore):
                    scores.append(2)
                self.traceTable[i][j] = scores
    def BuildPath(self):
        i = len(self.table)-1
        j = len(self.table[0])-1
        s1 = ""
        s2 = ""
        path = ""
        # assumes that there is one path and one path only
        while i != 0 and j != 0:
            if self.traceTable[i][j][0] == 2:
                path += "d"
                i = i-1
                j = j-1
            elif self.traceTable[i][j][0] == 1:
                path += "l"
                j = j - 1
            elif self.traceTable[i][j][0] == 0:
                path += "t"
                i = i - 1
        return path
    def GetPairwiseAlignment(self):
        seqFinal1 = ""
        seqFinal2 = ""

        seq1 = self.seq1[::-1]
        seq2 = self.seq2[::-1]

        seq1Counter = 0
        seq2Counter = 0
        finalScore = 0
        for i in self.path:
            if i == "d":
                seqFinal1 += seq1[seq1Counter]
                seqFinal2 += seq2[seq2Counter]

                if seq1[seq1Counter] == seq2[seq2Counter]:
                    finalScore += self.match
                else:
                    finalScore += self.mismatch
                seq1Counter += 1
                seq2Counter += 1
            elif i == 'l':
                seqFinal1 += '-'
                seqFinal2 += seq2[seq2Counter]
                seq2Counter += 1
                finalScore += self.gap
            else:
                seqFinal2 += '-'
                seqFinal1 += seq2[seq1Counter]
                seq1Counter += 1
                finalScore += self.gap
        print(seqFinal1[::-1])
        print(seqFinal2[::-1])
        print("Score is: " + str(finalScore))
    def ExecuteAlignment(self):
        self.table = self.BuildTable()
        self.traceTable = self.BuildTraceTable()
        self.FillTable()
        self.path = self.BuildPath()
        self.GetPairwiseAlignment()

def main():
    gapPenalty = -1
    mismatchPenalty = 0
    match = 1
    needleWunsch = NeedWunsch("actcg","acagtag",gapPenalty, mismatchPenalty, match)
    needleWunsch.ExecuteAlignment()

if __name__ == "__main__":
    main()
