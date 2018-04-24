'''
Created on Apr 23, 2018

@author: Azhar
'''
from numpy.core.defchararray import rfind
from os.path import isdir
from posix import mkdir

BaseDir = "/Users/Azhar/Desktop/MultiWUW/"
featDir = "feat/"
featFile = BaseDir + featDir+"down/0c40e715_nohash_0.mfc"
outFile = BaseDir +"ReverseFeatTest/down/0c40e715_nohash_0.mfc"


FrameList = []
Header=''
FeatDimension = 39  # 13 with d and dd
with open(featFile,'rb') as fp:
    header = fp.read(1) # This is the header, which is 13xN where N is no of frames for audio
    Header = header
    frame = fp.read(FeatDimension)
    while frame != "":
        # Do stuff with byte.
        #print frame
        FrameList.append(frame)
        frame = fp.read(FeatDimension)

FrameList.reverse()
FrameList.insert(0, Header)
L =len(FrameList)
print("No of frames: " + str(L))

'''
Write reversed frames into ouFile
'''
testDir = outFile.rfind("/")
newDir = outFile[0:testDir]
print newDir
if(isdir(newDir) is not True):
    mkdir(newDir)
with open(outFile, 'wb') as fo:
    for i in range(0,len(FrameList)):
        print i
        fo.write(FrameList[i])

"""
Test list.insert.
@param list.inser(index,value): Check if list.inser(index,value) inserts value before index 
"""

TestList = ["feat1","feat2","feat3"]
TestList.reverse()
TestList.insert(0, "Header")
print TestList