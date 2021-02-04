def fibgen(step: int) -> int:
    Fn = 0
    Fn1 = 1
    step -= 1
    for Fx in range(step - 1):
        tmp = Fn1 + Fn
        Fn = Fn1
        Fn1 = tmp
    return Fn

#def fibgen2(step: int) -> int:
    #initial = [0, 1, 1, 2, 3, 5, 8]
    #if(step < 8):
        #Fx = initial[step-1]
    #else:
        #Fx = (8 * (1.61803399 ** (step - 7))) / 1

    #return Fx

def fibgen3(step: int) -> int:
    goldenRatio = 1.61803399
    Fx = int(((goldenRatio ** step) - ((1 - goldenRatio) ** step)) / ((5)** 0.5))
    return Fx

if __name__ == '__main__':
    for step in range(14):
        correct = fibgen(step)
        #wrong = fibgen2(step)
        maybe = fibgen3(step)
        print(f"Correct: {correct}")
        #print(f"Wrong:   {wrong}")
        print(f"Maybe:   {maybe}\n")
