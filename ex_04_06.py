def computepay(h,r):
    if h > 40:
        p = 40 * r + (h - 40) * r * 1.5
        return p
    else:
        p = h * r
        return p


hours = input("Enter Hours:")
rate = input("Enter hour rate:")
try:
    hrs = float(hours)
    rt = float(rate)
except:
    print("Enter numeric values")
    quit()

p = computepay(hrs, rt)
print(p)
