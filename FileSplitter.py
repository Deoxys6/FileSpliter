import argparse
import sys
import os

#Function used to split a single file into files each contains CHUNKSIZE bytes 
def splitFile(originalFileName, folderName):
    print(originalFileName, folderName)
    #Create the folder we were given if it does not already exists
    if not (os.path.exists(folderName)):
        os.makedirs(folderName)   
    CHUNKSIZE = 10 * 1024 * 1024
    x = 1
    #open the orignal file, read the chunk of 10MB of data
    with open(originalFileName, 'rb') as originalFile:
        chunk = originalFile.read(CHUNKSIZE)
        #while we have chunks of data, create new files and write the data to them
        while chunk:
            filename = 'file %i'% x
            filePath = os.path.join(folderName, filename)
            with open(filePath, 'wb') as file:
                file.write(chunk)
                x+=1
                chunk = originalFile.read(CHUNKSIZE)
            file.close()  
    originalFile.close()
    return 0
    
#Function to combine the binary files back into the original file
def combineFile(numFiles, originalFileName, folderName):
    #create the path for the files we will be opening
    originalFilePath = os.path.join(folderName, originalFileName)
    #open the file that we will combine all the files back into
    with open(originalFilePath, 'wb') as originalFile:
        #open each binary file, write its contents to the "original file" close the iterating file and repeate until we are done
        for x in range(1, numFiles + 1):
            fileName = 'file %i' % x
            itterativeFilePath = os.path.join(folderName, fileName)
            with open(itterativeFilePath, 'rb') as file:
                chunk = file.read()
                originalFile.write(chunk)
            file.close()
    originalFile.close()

#Main function so this file can be easily called via the command line
if __name__ == '__main__':
    folderName = 'test'
    parser = argparse.ArgumentParser(description='Run some functions')
    # Add a commands the user can call
    parser.add_argument('--splitFile',nargs=1, type=str, help='Split the file provided into 10MB files')
    parser.add_argument('--combineFile', nargs=2, help='Combines number of files provided into file name provided')    
    parser.add_argument('--folderName', nargs=1, help='Name of folder')    

    # Get our arguments from the user
    args = parser.parse_args()
    
    if args.folderName:
        folderName = args.folderName[0]
    if args.splitFile:
        #If the user does not supply a folder name, make the folder name the file name + _Folder
        if args.folderName is None:  
            folderName = os.path.splitext(args.splitFile[0])[0] + "_Folder"
        splitFile(args.splitFile[0], folderName)
    if args.combineFile:
        combineFile(int(args.combineFile[0]), args.combineFile[1], folderName)
