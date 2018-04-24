'''
Created on Apr 24, 2018

@author: Azhar
'''
#!/usr/bin/python

from os import environ, path
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

BASEDIR = "/Users/Azhar/Desktop/MultiWUW/"
MODELDIR = BASEDIR+ "model_parameters/MultiWUW.cd_cont_200/"
F_DATADIR = BASEDIR+"feat/"
R_DATADIR = BASEDIR+"reverseFeat/"

# Create a decoder with certain model

config = Decoder.default_config()
config.set_string('-hmm', MODELDIR)
config.set_string('-lm', path.join(BASEDIR, 'etc/MultiWUW.lm'))
config.set_string('-dict', path.join(BASEDIR, 'etc/MultiWUW.dic'))

config.set_string('-logfn', '/dev/null')
config.set_float('-beam', 1e-100)
config.set_float('-fwdflatbeam', 1e-130)
config.set_float('-fwdflatlw',10)
config.set_float('-fwdflatwbeam',1e-120)
config.set_float('-lpbeam',1e-60)
config.set_float('-lponlybeam',1e-20)
config.set_float('-lw', 0.5)
# Decode streaming data.
decoder = Decoder(config)

'''
Start decoding mfc feature file
'''
stream = open(path.join(F_DATADIR, 'bed/fa446c16_nohash_2.mfc'), 'rb')
stream.read(4)
buf = stream.read(13780)
decoder.start_utt()
decoder.process_cep(buf, False, True)
decoder.end_utt()
hypothesis = decoder.hyp()
#logmath = decoder.get_logmath()
logmath = decoder.get_logmath()

print("Best hypothesis: ", hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", hypothesis.prob)
#print ("Best hypothesis: ", hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ", logmath.exp(hypothesis.prob))