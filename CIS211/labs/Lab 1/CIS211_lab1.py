class Fraction:
    def __init__(self, num: int, den: int):
        assert num >= 0 and den >0, 'Denominator cannot be 0 and Numberator cannot be negative'
        self.num = num
        self.den = den
        self.simplify()

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction({self.num},{self.den})"

    def __mul__(frac1, frac2) -> str:
        num_result = frac1.num * frac2.num
        den_result = frac1.den * frac2.den
        fractemp = Fraction(num_result,den_result)
        fractemp.simplify()
        return f"{fractemp.num}/{fractemp.den}"

    def __add__(frac1, frac2) -> str:
        num_result = (frac1.num * frac2.den) + (frac2.num * frac1.den)
        den_result = frac1.den * frac2.den
        fractemp = Fraction(num_result,den_result)
        fractemp.simplify()
        return f"{fractemp.num}/{fractemp.den}"

    def gcd(self, a, b) -> int:
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    
    def simplify(self) -> None:
        gcd = self.gcd(self.num, self.den)
        self.num = int(self.num/gcd)
        self.den = int(self.den/gcd)
        return None
    
