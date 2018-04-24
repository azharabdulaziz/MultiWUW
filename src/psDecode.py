'''
Created on Apr 24, 2018

@author: Azhar
'''
#!/usr/bin/python

from os import environ, path
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *



# Create a decoder with certain model
def psDecodeFeat(fileName):
    BASEDIR = "/Users/Azhar/Desktop/MultiWUW/"
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
    
    '''
    Start decoding mfc feature file
    '''
    stream = open(path.join(fileName), 'rb')
    stream.read(4)
    buf = stream.read(13780)
    decoder.start_utt()
    decoder.process_cep(buf, False, True)
    decoder.end_utt()
    hypothesis = decoder.hyp()
    #logmath = decoder.get_logmath()
    
    return(hypothesis)
    #print("Best hypothesis: ", hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", hypothesis.prob)
    #print ("Best hypothesis: ", hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", logmath.exp(hypothesis.prob))