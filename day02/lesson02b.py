bill = input("What was your bill?\n")
tip_percent = input("Tip %\n")
payers = input("How are you gonna split it?\n")
# cast str to numbersss
bill = float(bill)
tip_percent = float(tip_percent)
payers = int(payers)

tip = bill * (tip_percent / 100)
total = bill + tip
total_divided = total / payers

print(f"Your total is ${round(total, 2)}")
print(f"Divided {payers} ways it's ${round(total_divided, 2)}")
