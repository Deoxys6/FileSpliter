import argparse
import sys

#Function used to split a single file into files each contains CHUNKSIZE bytes 
def splitFile(fileName):
    CHUNKSIZE = 10 * 1024 * 1024
    x = 1
    #open the orignal file, read the chunk of 10MB of data
    with open(fileName, 'rb') as originalFile:
        chunk = originalFile.read(CHUNKSIZE)
        #while we have chunks of data, create new files and write the data to them
        while chunk:
            filename = 'file %i'% x
            with open(filename, 'wb') as file:
                file.write(chunk)
                x+=1
                chunk = originalFile.read(CHUNKSIZE)
            file.close()  
    originalFile.close()
    return 0
    
#Function to combine the binary files back into the original file
def combineFile(numFiles, filename):
    #open the file that we will combine all the files back into
    with open(filename, 'wb') as originalFile:
        #open each binary file, write its contents to the "original file" close the iterating file and repeate until we are done
        for x in range(1, numFiles + 1):
            filename = 'file %i' % x
            with open(filename, 'rb') as file:
                chunk = file.read()
                originalFile.write(chunk)
            file.close()
    originalFile.close()

#Main function so this file can be easily called via the command line
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run some functions')
    # Add a commands the user can call
    parser.add_argument('--splitFile',nargs=1, help='Split the file provided into 10MB files')
    parser.add_argument('--combineFile', nargs=2, help='Combines number of files provided into file name provided')    
    # Get our arguments from the user
    args = parser.parse_args()
    if args.splitFile:
        splitFile(args.splitFile)
    if args.combineFile:
        combineFile(int(args.combineFile[0]), args.combineFile[1])