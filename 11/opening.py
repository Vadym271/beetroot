with open('myfile.txt') as f:
    line = f.read()
print(line)

#Note 1: the file does show up in a directory where i ran scripts
#Note 2: since different directory does not contain our file python won't find the file
# if we add a different directory to path of the file

