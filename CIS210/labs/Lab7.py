import os
os.getcwd()

def uppercase_file(myf):
    with open(myf) as file:
        newf = file.read()
        upper_file = newf.upper()
    print(upper_file)
    return None

def lowercase_file(myf):
    with open(myf) as file:
        newf = file.read()
        lower_file = newf.lower()
    print(lower_file)
    return None

def fcounts(file):
    '''
    (file) -> None

    


