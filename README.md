# FileSplitter.py

Project to get around the 10MB upload limit for files on discord. Allows the user to separate a file into several 10MB chunk files to upload to another user who can then user the code to re-assemble the file into it's original configuration. 

## Commands

***--splitFile*** requires the relative filename of the file that you wish to split. It will split the File into X files in folder specified by --folderName. If the folder does not exist, it will create a new folder given the name provided. 

***--combineFile*** requires the total number of files that are in the working directory that you wish to combine into the new file name provided. 

***--folderName*** This is the name of the folder that you are wanting to save / read files from. If no folder name is provided, the default will be filename_Folder. 
