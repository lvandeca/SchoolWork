"""
CIS 313: Intrem Data Structurs

Author: Luke Vandecasteele

Credits: Course textbook, Lab0 Project Overview

Program run to terminal that prompts user to input a digit (or step).
This digit is used to calculate the nth number in the Fibonacci
sequence. Acceptable inputs include any integer greater than 0, or
'q' to quit the program. Creates a class FibSequence and uses the
golden ratio and formula to generate the nth Fibonacci number.
"""


class FibSequence:
    def __init__(self) -> None:
        """Initializing function for the Fibonacci Sequence.
        Establishes F0 and F1 as the initial values for the
        sequence. Also initializes the golden ratio for later
        use.
        """
        self.F0 = 0
        self.F1 = 1
        self.goldenRatio = 1.61803399

    def compute(self, n) -> int:
        """Caluclates the nth Fibonacci Number. Uses the golden
        ratio and the formula:

        (1.618...^n) - (1 - 1.618...)^n / 5^(1/2)

        to calulate. Input n is for a 1-indexed sequence whereas
        the formula is for a 0-indexed sequence so the necessary
        conversion is made. Calls self.display() to print to
        standard output.
        """
        Fn = int(((self.goldenRatio ** (n-1)) - ((1 - self.goldenRatio) ** (n-1))) / ((5)** 0.5))
        self.display(n, Fn)

        return Fn

    def display(self, step: int, num: int) -> None:
        """Prints the nth Fibonacci Number as input by the user.
        to standard output. Called by self.compute. Calls
        self.genSuffix() for correct printing output.
        """

        suffix = self.genSuffix(step)
        print(f"The {step}{suffix} Fibonacci number is: {num}\n")
        return None

    def genSuffix(self, step: int) -> str:
        """Helper function for display. Generates correct suffix
        for a number. Example: 1st, 2nd, 3rd, 4th, etc. Called by
        self.display().
        """

        #isolates one and tens digits
        ones = step % 10
        tens = (step % 100) - ones

        st = [1, 2, 3]
        suf = ["st", "nd", "rd"]

        #outlier case when ones digit is 1, 2, or 3, and the tens
        #digit is not 1
        if(ones in st and tens != 10):
            for num in range(3):
                if ones == st[num]:
                    suffix = suf[num]

        #standard suffix for a majority of numbers
        else:
            suffix = "th"

        return suffix


def main():
    """Main driver function for program. Creates instance of FibSequence"""

    Fx = FibSequence()
    calculateFib = True

    while calculateFib:

        #Loop constantly asking for user input. Loop breaks if 'q' is input
        userInput = input("Enter a digit or 'q' to quit: ")

        #Try and except to catch invalid inputs such as floats, negative
        #integers, or characters other than 'q'.
        try:
            step = int(userInput)
            if(step > 0):
                Fx.compute(step)

            #Catches case when int(userInput) doesn't fail, but integer is
            #not greater than 0.
            else:
                print(f"Invalid input: '{userInput}' Usage: integer > 0 or 'q' to exit program\n")

        #ValueError generated when int(userInput) fails.
        except ValueError:
            if(userInput == 'q'):
                calculateFib = False
            else:
                print(f"Invalid input: '{userInput}' Usage: integer > 0 or 'q' to exit program\n")
    print()

    return None

if __name__ == '__main__':
    main()
