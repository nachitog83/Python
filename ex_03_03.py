score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("Enter numeric value")

if s < 0.6: print("F")
elif s < 0.7: print("D")
elif s < 0.8: print("C")
elif s < 0.9: print("B")
elif s <= 1.0: print("A")
else: print("Grade out of range")
