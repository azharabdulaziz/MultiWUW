"""
PrepareCorpus.py
This method 

The core words are:
"Yes", "No", "Up", "Down", "Left", "Right", "On", "Off", "Stop", "Go", "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", and "Nine".
To help distinguish unrecognized words, there are also ten auxiliary words, which most speakers only said once. These include:
 "Bed", "Bird", "Cat", "Dog", "Happy", "House", "Marvin", "Sheila", "Tree", and "Wow". 

@author: Azhar Abdulaziz
@note: The data are from 
"Warden P. Speech Commands: A public dataset for single-word speech recognition, 2017. Available from http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz".
"""

"""
@bug: 
"""
def getDictionary(CoreOrAux,listingFile):
    """
    Split the original list file "validation_list" and "testing_list" from the train corpus into two lists:
    
    1- Core list.
    2- Auxilary list.
    
    @type CoreOrAux: String 
    @param CoreOrAux: Input either 'Core' or 'Aux' 
    """ 
    if(CoreOrAux == "Core" ):
        whichList = finalCoreList
    elif(CoreOrAux == "Aux"):
        whichList = finalAuxList
    else:
        print(" Invalid input, please input either 'Core' or 'Aux'.... ")  
   
    testingFile = BaseDir+listingFile
    DictFile = BaseDir+"MultiWUW_"+ CoreOrAux +".dic"
    toWrite = open(DictFile,'w')
    with open(testingFile,'r') as testing:
        lines = testing.readlines()
        N = len(lines)
        #print("No of Lines: " + str(N))
        for i in range(0,N):
            line = lines[i]
            specificWord = line.split("/",1)[0]
            #print specificWord
            if(specificWord in whichList):
                #print("Line: " + line +"   Specific Word: " + specificWord)
                toWrite.write(specificWord+"\n")
    toWrite.close()
    print("The file " + DictFile + " was written sucessfully")
    return


def getTranscript(CoreOrAux,listingFile):
    """
    Split the original list file "validation_list" and "testing_list" from the train corpus into two lists:
    
    1- Core list.
    2- Auxilary list.
    
    @type CoreOrAux: String 
    @param CoreOrAux: Input either 'Core' or 'Aux' 
    """ 
    if(CoreOrAux == "Core" ):
        whichList = finalCoreList
    elif(CoreOrAux == "Aux"):
        whichList = finalAuxList
    else:
        print(" Invalid input, please input either 'Core' or 'Aux'.... ")  
    if(listingFile.find("testing")):
        firstFileName = "MultiWUW_test"
    elif(listingFile.find("validation")):
        firstFileName = "MultiWUW_train"
    else:
        print("The input list file name is not correct") 
 
    testingFile = BaseDir+listingFile
    TranscriptionFile = BaseDir+firstFileName+ CoreOrAux +".transcription"
    CleanTranscription = BaseDir+firstFileName+ CoreOrAux +"Transcription.txt"
    TowriteTrans = open(TranscriptionFile,'w')
    TowriteClean = open(CleanTranscription,'w')
    with open(testingFile,'r') as testing:
        lines = testing.readlines()
        N = len(lines)
        #print("No of Lines: " + str(N))
        for i in range(0,N):
            line = lines[i]
            specificWord = line.split("/",1)[0]
            #print specificWord
            if(specificWord in whichList):
                #print("Line: " + line +"   Specific Word: " + specificWord)
                TowriteTrans.write("<s> " + specificWord.upper()+" </s> ("+line.split(".",1)[0]+")\n")
                TowriteClean.write(specificWord + "\n")
    TowriteTrans.close()
    TowriteClean.close()
    print("The file " + TranscriptionFile + " was written sucessfully")
    return

def splitLists(CoreOrAux,listingFile):
    
    """
    Split the original list file "validation_list" and "testing_list" from the train corpus into two lists:
    
    1- Core list.
    2- Auxilary list.
    
    @type CoreOrAux: String 
    @param CoreOrAux: Input either 'Core' or 'Aux' 
    """ 
    if(CoreOrAux == "Core" ):
        whichList = finalCoreList
    elif(CoreOrAux == "Aux"):
        whichList = finalAuxList
    else:
        print(" Invalid input, please input either 'Core' or 'Aux'.... ")  
    if(listingFile.find("testing")):
        firstFileName = "MultiWUW_test"
    elif(listingFile.find("validation")):
        firstFileName = "MultiWUW_train"
    else:
        print("The input list file name is not correct") 
    testingFile = BaseDir+listingFile
    fileIDs = BaseDir + firstFileName+ CoreOrAux +".fileids"
    toWrite = open(fileIDs,'w')
    with open(testingFile,'r') as testing:
        lines = testing.readlines()
        N = len(lines)
        #print("No of Lines: " + str(N))
        for i in range(0,N):
            line = lines[i]
            specificWord = line.split("/",1)[0]
            #print specificWord
            if(specificWord in whichList):
                #print("Line: " + line.split(".",1)[0] )
                toWrite.write(line.split(".",1)[0]+"\n")
    toWrite.close()
    print("The file " + fileIDs + " was written sucessfully")
    return

def Start():
    
    """
    Now, the given list files are for testing and validation (training). The following code will prepare them.
    """
    toSplitFile= "testing_list.txt"
    CoreOrAux = "Core"
    splitLists(CoreOrAux,toSplitFile)
    getTranscript(CoreOrAux, toSplitFile)
    CoreOrAux = "Aux"
    splitLists(CoreOrAux,toSplitFile)
    getTranscript(CoreOrAux, toSplitFile)
    
    toSplitFile= "validation_list.txt"
    CoreOrAux = "Core"
    splitLists(CoreOrAux,toSplitFile)
    getTranscript(CoreOrAux, toSplitFile)
    CoreOrAux = "Aux"
    splitLists(CoreOrAux,toSplitFile)
    getTranscript(CoreOrAux, toSplitFile)
    


"""
The exution of the code start here.
Finally, the CoreValidationList will be used to train the WUW AM.
On the other hand, the testing lists for both core and auxilary will be used to measure the scores.  

"""
"""
Global variables
@type finalCoreList: List of strings 
@param finalCoreList:
@type finalAuxList: List of strings
@param finalAuxList:   
"""
BaseDir = "/Users/Azhar/Documents/Corpora/WUWcommands/train/";
auxWords = [ "Bed", "Bird", "Cat", "Dog", "Happy", "House", "Marvin", "Sheila", "Tree","Wow"]
coreWords = ["Yes", "No", "Up", "Down", "Left", "Right", "On", "Off", "Stop", "Go", "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight","Nine"]
corelength = len(coreWords)
auxlength = len(auxWords)

for i in range(0,corelength):
    coreWords[i] = coreWords[i].lower()
    #print ("Core Word["+str(i)+"]: "+coreWords[i])
for i in range(0,auxlength):
    auxWords[i] = auxWords[i].lower()
    #print("auxilary word[" + str(i) + "]: " + auxWords[i])

"""
Extracting 10 core and auxilary words
For core words, only the first 10 words are considered. The digits will be excluded by doing so. 
As for auxilary words are only 10, all of them are considered. 
"""
finalCoreList = coreWords[0:10]
#print finalCoreList
finalAuxList = auxWords
#print finalAuxList

Start()
# CoreOrAux = "Core"
# listingFile = "testing_list.txt"
# 
# listingFile = "validation_list.txt"
# getTranscript(CoreOrAux, listingFile)