#16 3 2 13
#5 10 11 8
#9 6 7 12
#4 15 14 1


a = input("")
b = input("")
c = input("")
d = input("")

w = a.split()
x = b.split()
y = c.split()
z = d.split()

number = int(w[0]) + int(w[1]) + int(w[2]) + int(w[3])

if number == int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) and number == int(y[0]) + int(y[1]) + int(y[2]) + int(y[3]) and number == int(z[0]) + int(z[1]) + int(z[2]) + int(z[3]) and number == int(w[0]) + int(x[0]) + int(y[0]) + int(z[0]) and number == int(w[1]) + int(x[1]) + int(y[1]) + int(z[1]) and number == int(w[2]) + int(x[2]) + int(y[2]) + int(z[2]) and number == int(w[3]) + int(x[3]) + int(y[3]) + int(z[3]):
    print("magic")
else:
    print("not magic")