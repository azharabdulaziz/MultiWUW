'''
Created on Apr 24, 2018

@author: Azhar
'''
from os import environ, path
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import StoreResults as dump

def psDecode(fileName):
    '''
    Start decoding mfc feature file
    '''
    stream = open(path.join(fileName), 'rb')
    stream.read(4)
    buf = stream.read(13780)
    stream.close()
    """
    START DECODER
    """
    decoder.start_utt()
    decoder.process_cep(buf, False, True)
    decoder.end_utt()
    """
    END DECODER
    """
    
    hypothesis = decoder.hyp()
    return(hypothesis.best_score)






BASEDIR = "/Users/Azhar/Desktop/MultiWUW/"
ForwardFeatDir = "feat/"
ReverseFeatDir = "reverseFeat/"
IV_FileIds = BASEDIR + "etc/MultiWUW_trainCore.fileids"
OOV_FileIds = BASEDIR + "etc/MultiWUW_trainAux.fileids"


"""
Defining Decoder

"""


MODELDIR = BASEDIR+ "model_parameters/MultiWUW.cd_cont_200/"

#DATADIR = BASEDIR+featDir
#R_DATADIR = BASEDIR+"reverseFeat/"
config = Decoder.default_config()
config.set_string('-hmm', MODELDIR)
config.set_string('-lm', path.join(BASEDIR, 'etc/MultiWUW.lm'))
config.set_string('-dict', path.join(BASEDIR, 'etc/MultiWUW.dic'))

config.set_string('-logfn', '/dev/null')

# Decode streaming data.
decoder = Decoder(config)
    

"""
For IV get forward
"""
FinalResult = {}
ListOfFinalResult = []
with open(IV_FileIds) as fi:
    line = fi.readline().strip('\n')
    while(line):
        fileNameForward = BASEDIR+ForwardFeatDir+line+'.mfc'
        fileNameBackward = BASEDIR+ReverseFeatDir+line+'.mfc'
        #print fileName
        score1 = psDecode(fileNameForward)
        score2 = psDecode(fileNameBackward)
        #logmath = decoder.get_logmath()
        #print("Best hypothesis: ", hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", hypothesis.prob)
        FinalResult = {"FileName":line, "Score1":score1,"Score2":score2}
        ListOfFinalResult.append(FinalResult)
        """
        CONTINUE
        """
        line = fi.readline().strip('\n')
dump.CSVDictWrite(BASEDIR+"IVResults.csv")
   
