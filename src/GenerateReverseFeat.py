'''
Created on Apr 24, 2018

@author: Azhar
'''
from reverseFeature import reverseFeat
BaseDir = "/Users/Azhar/Desktop/MultiWUW/"
InfeatDir = "feat/"
outFeatDir = "reverseFeat/"
fileIds = BaseDir + "etc/MultiWUW_trainAux.fileids"
with open(fileIds,'r') as listIn:
    line = listIn.readline()
    while(line):
        inputFeat = BaseDir + InfeatDir + line.strip("\n")+".mfc"
        outputFeat = BaseDir + outFeatDir + line.strip("\n")+".mfc"
        reverseFeat(inputFeat, outputFeat)
        print("Converting: "+ inputFeat + " ====> " + outputFeat)
        line = listIn.readline()