import re


# Extracting SGM files - reut2-021.sgm

counter = 1;
fileName = "/home/ubuntu/server/Assign2dw/articles/myfile" + str(counter) + ".txt"

isFound = False

with open('reut2-021.sgm') as fp:
    
    for line in fp:
        if isFound:         
            if not re.search('</TEXT>', line):
                fp1.write(line)
            else:
                isFound = False
                fp1.close()
                counter += 1
                fileName = "/home/ubuntu/server/Assign2dw/articles/myfile" + str(counter) + ".txt"
                
        else:            
            if re.search('<TEXT.*', line):
                isFound = True
                fp1 = open(fileName, "a")                
    
fp.close()

# Extracting SGM files - reut2-020.sgm

counter = 1;
fileName = "/home/ubuntu/server/Assign2dw/articles/myfile_second_" + str(counter) + ".txt"

isFound = False

with open('reut2-020.sgm') as fp:
    
    for line in fp:
        if isFound:           
            if not re.search('</TEXT>', line):
                fp1.write(line)
            else:
                isFound = False
                fp1.close()
                counter += 1
                fileName = "/home/ubuntu/server/Assign2dw/articles/myfile_second_" + str(counter) + ".txt"
                
        else:            
            if re.search('<TEXT.*', line):
                isFound = True
                fp1 = open(fileName, "a")                
    
fp.close()




