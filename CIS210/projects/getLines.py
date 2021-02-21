def getLines(fileName):
    """ getLines validates the given fileName.
        Returns all lines present in a valid file. """
    lines = ""
    if (fileName != None and len(fileName) > 0 and os.path.exists(fileName)):
        if os.path.isfile(fileName):
            file = open(fileName, 'r')
            lines = file.read()
            if (len(lines) > 0):
                return lines
            else:
                print("<" + fileName + "> is an empty file!", end="\n\n")
        else:
            print("<" + fileName + "> is not a file!", end="\n\n")
    else:
        print("<" + fileName + "> doesn't exists, try again!", end="\n\n")
    return lines
