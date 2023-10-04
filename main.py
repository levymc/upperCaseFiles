import os

def renameFiles(path):
    for actualFolder, _, files in os.walk(path):
        for fileName in files:
            if fileName.endswith('.ts'):
                newName = fileName[0].upper() + fileName[1:]
                
                oldPath = os.path.join(actualFolder, fileName)
                newPath = os.path.join(actualFolder, newName)
                os.rename(oldPath, newPath)
                print(f"Renaming: {fileName} -> {newName}")

path = '/home/levy/git/wehandle-integrations/integrations--wh-intgr-mdias/src'
renameFiles(path)
