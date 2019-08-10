import os
from os.path import isfile, join

directory = 'Books_directory_path'

onlyfiles = [f for f in os.listdir(directory) if isfile(join(directory, f))]

for filename in onlyfiles:
    removeExtension = filename.find('.')
    nameOnly, extensionOnly = filename[:removeExtension], filename[removeExtension:]
    if extensionOnly == ".zip":
        pass
    else:
        destination = directory + nameOnly
        if os.path.isdir(destination) == False:
            os.mkdir(destination)
            os.rename(directory + filename, destination + '\\' + filename)
        else:
            os.rename(directory + filename, destination + '\\' + filename)