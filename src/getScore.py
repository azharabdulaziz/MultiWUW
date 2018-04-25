'''
Created on Apr 24, 2018

@author: Azhar
'''
import StoreResults as dump

def getHypotheses(fname):
    ListOfHyps = []
    with open(fname) as fp:
        prev_line = "kkkk"
        for line in fp:  
            if line.find(scoreLine)> -1:
                #print line
                score = line.split(':',3)[3]
                score = score.strip("\n")
            if line.find("done")> -1:
                hyp0 = prev_line
                splitted = hyp0.split('(')
                hyp = splitted[0]
                fNameOnly = splitted[1].split(')',2)[0].split()[0]
                confidence = splitted[1].split(')',2)[0].split()[1]
#                 
                #print("Name: "+fNameOnly+ "   Hyp:" + hyp+ "   Score:"+ score+"   Confidence:"+ confidence)
                #FinalResult = {"Name":fNameOnly, "Hyp": hyp, "Score": score, "Confidence": confidence}
                ListOfHyps.append(hyp)
            prev_line = line
    return(ListOfHyps)

def getFileName(fname):
    ListOfNames = []
    with open(fname) as fp:
        prev_line = "kkkk"
        for line in fp:  
            if line.find(scoreLine)> -1:
                #print line
                score = line.split(':',3)[3]
                score = score.strip("\n")
            if line.find("done")> -1:
                hyp0 = prev_line
                splitted = hyp0.split('(')
                hyp = splitted[0]
                fNameOnly = splitted[1].split(')',2)[0].split()[0]
                confidence = splitted[1].split(')',2)[0].split()[1]
#                 
                #print("Name: "+fNameOnly+ "   Hyp:" + hyp+ "   Score:"+ score+"   Confidence:"+ confidence)
                #FinalResult = {"Name":fNameOnly, "Hyp": hyp, "Score": score, "Confidence": confidence}
                ListOfNames.append(fNameOnly)
            prev_line = line
    return(ListOfNames)

def getScore(fname):
    ListOfScores = []
    with open(fname) as fp:
        prev_line = "kkkk"
        for line in fp:  
            if line.find(scoreLine)> -1:
                #print line
                score = line.split(':',3)[3]
                score = score.strip("\n")
#             if line.find("done")> -1:
#                 hyp0 = prev_line
#                 splitted = hyp0.split('(')
#                 hyp = splitted[0]
#                 fNameOnly = splitted[1].split(')',2)[0].split()[0]
#                 confidence = splitted[1].split(')',2)[0].split()[1]
#                 
                #print("Name: "+fNameOnly+ "   Hyp:" + hyp+ "   Score:"+ score+"   Confidence:"+ confidence)
                #FinalResult = {"Name":fNameOnly, "Hyp": hyp, "Score": score, "Confidence": confidence}
                ListOfScores.append(score)
            prev_line = line
    return(ListOfScores)







'''
MAIN
'''
IVorOOV = "OOV"

scoreLine = "INFO: ps_lattice.c(1380): Bestpath score:"
hypoLine = "INFO: batch.c(763):"  # At scoreLine+7 or before ('done')

BaseDir = "../DecodingLogs/"
                #              Model15: 40-50
 
ForScore1 = BaseDir + "MultiWUW-1-1_"+IVorOOV+"_Score1.log"
ForScore2 = BaseDir + "MultiWUW-1-1_"+IVorOOV+"_Score2.log"
outResult = BaseDir + IVorOOV + "_Scores.csv"
#out_File = BaseDir + "Noisy_" + str(inputSNR) +"db/" + currentModel
#print ("Storing result in: " + out_File)
FinalResults ={}
ListOfFinalResults = []
print("Getting results of input "+ ForScore1)
Score1 = getScore(ForScore1)
Hypothesis = getHypotheses(ForScore1)  # Hypotheses are correct only when extracted from forward decding (i.e. score1)
filesNames = getFileName(ForScore1)

Score2 = getScore(ForScore2)
print("Length of Score1: " + str(len(Score1)))
print("Length of Score2: " + str(len(Score2)))

for i in range(0,len(Score2)):
    #print ("Name",filesNames[i], "Hyp", Hypothesis[i],"Score1", Score1[i]) 
    #print ("Score2", Score2[i])
    FinalResults = {"Name":filesNames[i], "Hyp": Hypothesis[i], "Score1": Score1[i], "Score2": Score2[i]}
    ListOfFinalResults.append(FinalResults)
dump.CSVDictWrite(ListOfFinalResults, outResult)

        