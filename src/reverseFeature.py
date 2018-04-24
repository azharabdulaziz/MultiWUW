'''
Created on Apr 23, 2018

@author: Azhar Abdulaziz
'''
from os.path import isdir
from posix import mkdir

def reverseFeat(featFile,outFile):
    FrameList = []
    Header=''
    """
    Only 13 are stored, For IO efficiency we store only static features and dynamic features are computed on the fly. 
    The computation of dynamic features is configured with the -feat option. For example -feat 1s_c_d_dd means to read the vector and compute deltas and delta-deltas and combine them with 1-stream feature vector.
    There are different types like s2_4x which means to compute deltas, delta-deltas, delta-deltas of the second order and combine them in a special 4-stream feature vector.
    If you need a specific feature arrangement you can implement your own feature type in sphinxbase.
    If you want to use features as is use 1s_c feature type which means to read the vector unmodified.
    SEE: https://cmusphinx.github.io/wiki/mfcformat/
    
    
    header (int32 length)
    features of the frame 1 (13 floats or 13 * 4 bytes)
    features of the frame 2 (13 floats or 13 * 4 bytes)
    features of the frame ... (13 floats or 13 * 4 bytes)
    features of the frame N (13 floats or 13 * 4 bytes)
    """
    FeatDimension = 13*4
     
    with open(featFile,'rb') as fp:
        header = fp.read(2) # 2 bytes for the header (int32), which is 13xN where N is no of frames for audio
        Header = header
        frame = fp.read(FeatDimension)
        while frame != "":
            # Do stuff with byte.
            #print frame
            FrameList.append(frame)
            frame = fp.read(FeatDimension)
    
    FrameList.reverse()
    FrameList.insert(0, Header)
    '''
    Write reversed frames into ouFile
    '''
    testDir = outFile.rfind("/")
    newDir = outFile[0:testDir]
    #print newDir
    if(isdir(newDir) is not True):
        mkdir(newDir)
    with open(outFile, 'wb') as fo:
        for i in range(0,len(FrameList)):
            #print i
            fo.write(FrameList[i])
    
    return()

