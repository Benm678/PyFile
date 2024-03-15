# PyFile
A simple app to aid in managing backups of files. 
Over the past (many) few years each time I have upgraded computers, or added new drives I have ended up with a number of compounded file structures - with many files having multiple levels of duplication. 
I wanted a simple way to get a list of all files and all duplicates on a given file path. 
Once opened, select the Generate File Listing option, then select the folder you are interested in. Then Generate Lists. 
Two lists are created, one is Duplicates.csv, the other is UniqueFiles.csv. 
Duplicates are any files in the folder structure that have both the same filename and the same size
UniqueFiles are any files in the folder structure that do not apply to the Duplicates category. 
Two files with the same filename and different file size are regarded as unique. It is therefore possible that two (say a readme.text) file for different applications that just happen to have the same filesize will be treated as duplicates.
If there is a lot of files and folders it can take quite a bit of time, terminal gives a running count of the number of files that have been read in. 
Once finished, click Open and the two csv files will open in the default program. 
In the duplicates.csv file, delete any file entries that you don't want to keep. Usually my process is to keep the top level or first reported version of the file, so will delete the contents of any column with a header of path2 or greater. 
This may or may not work for you. 
Check the uniquefiles.csv to make sure the files seem correct for your path. 
Next, click the Copy Files menu option. 
Select the csv - duplicates or unique - that you want to copy, and then a destination folder. The destination folder is where the files will be copied to. 
Note that file structure is retained. 
Note that files will be overwritten by filename if that file already exists in the new path.
Delete Files is not yet active in this version
