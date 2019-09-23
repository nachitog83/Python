hours = input("Enter hours:")
rate = input("Enter rate:")
try:
    h = float(hours)
    r = float(rate)
except:
    print("Enter numeric input")
    quit()

if h > 40:
    p = 40 * r + (h - 40) * r * 1.5
else:
    p = h * r

print("Pay:", p)
