'''
Description: Read and index data.
#----------------------------------------------------------------------------------------------------------------#
Class functions:


#----------------------------------------------------------------------------------------------------------------#
Notes:

'''
import numpy as np

class videoData:

#------------------------------ Constructor ------------------------------#
    def __init__(self, FILE_NAME, HEIGHT, WIDTH, CHANNELS):
        self.__videoFrames = np.fromfile(FILE_NAME, dtype ='uint8')
        self.__width = WIDTH
        self.__height = HEIGHT
        self.__channels = CHANNELS
        self.totalFrames = len(self.__videoFrames)/(WIDTH*HEIGHT*CHANNELS)

    def getFrame(self,frameNumber):
        rgbArray = np.zeros((self.__height,self.__width,self.__channels),'uint8')
        # i,j,k = [(frameNumber-1)*HEIGHT*WIDTH*CHANNELS + i*HEIGHT*WIDTH for i in range(3)]

        for channel in range(self.__channels):
            for row in range(self.__height):
                for col in range(self.__width):
                    i = channel*self.__height*self.__width+row*self.__width+col
                    rgbArray[row][col][channel] = self.__videoFrames[self.__channels*(frameNumber-1)*self.__height*self.__width + i]
        return rgbArray


    def iterator(self,startFrame=0):
        for i in range(self.totalFrames):
            yield(self.getFrame(startFrame+i))


if __name__ =='__main__':
    a = videoData('oneperson_960_540.rgb',540,960,3)
    a.getFrame(0)
    a.getFrame(1)
    a.getFrame(2)

