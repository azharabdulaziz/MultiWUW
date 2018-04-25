'''
Created on Apr 24, 2018

@author: Azhar
'''
scoreLine = "INFO: ps_lattice.c(1380): Bestpath score:"
hypoLine = "INFO: batch.c(763):"  # At scoreLine+7 or before ('done')

BaseDir = "../DecodingLogs/"
                #              Model15: 40-50
logFile = "MultiWUW-1-1_IV_Score1.log"
fname = BaseDir + logFile

#out_File = BaseDir + "Noisy_" + str(inputSNR) +"db/" + currentModel
#print ("Storing result in: " + out_File)
print("Getting results of input "+ fname)

ListOfFinalResults = []
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
            
            print("Name: "+fNameOnly+ "   Hyp:" + hyp+ "   Score:"+ score+"   Confidence:"+ confidence)
            FinalResult = {"Name":fNameOnly, "Hyp": hyp, "Score": score, "Confidence": confidence}
            ListOfFinalResults.append(FinalResult)
        prev_line = line
        