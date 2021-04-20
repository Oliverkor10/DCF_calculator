import math

# DCF calculator for python
#by Oliver Korchnoy
def DCF(FCF, r, growth1, growth2, t, p_growth,shares_outstanding, margin_of_safety):
    r= r/100
    growth1= growth1/100
    growth2 = growth2/100
    p_growth= p_growth/100
    FCF_current = FCF
    FCF_sum = 0
    FCF_last = 0
    for i in range(1, math.ceil(t / 2) + 1):
        FCF_current = (FCF_current * (1 + growth1))
        FCF_sum += FCF_current/((1+r)**i)
    for j in range(math.ceil(t / 2) + 1, t + 1):
        FCF_current = (FCF_current * (1 + growth2))
        if (j == t):
            FCF_last = FCF_current
        FCF_sum += FCF_current/((1+r)**j)

    terminal = (FCF_last * (1 + p_growth)) / (r - p_growth)
    d_terminal = terminal / ((1 + r) ** t)
    Intrinsic = d_terminal + FCF_sum
    print("The Intrinsic Value of the comapny is : " + str(Intrinsic))
    Intrinsic_value = Intrinsic/shares_outstanding
    roundedI = round(Intrinsic_value,2)
    print("The Intrinsic Value per share is: " + str(roundedI))
    Buy_Price = Intrinsic_value * (1-margin_of_safety/100)
    roundedB = round(Buy_Price,2)
    print("The Buy Price per Share is: " + str(roundedB))




FCF = float(input("What is the starting Free Cash Flow: "))
r = float(input("What is the expected rate of return: "))
t = int(input("How many years is this DCF: "))
growth1 = float(input("What is the expected growth rate for the first half of the time period: "))
growth2 = float(input("What is the expected growth for the second half of the time period: "))
p_growth = float(input("What is the perpetual growth rate: "))
shares_outstanding = float(input("How many shares outstanding(in millions): "))
margin_of_safety = float(input("What is your margin of safety (%): "))

DCF(FCF, r, growth1, growth2, t, p_growth, shares_outstanding, margin_of_safety)
