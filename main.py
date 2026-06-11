a = 5 // 100
print(a)
price = int(input('Số tiền phát sinh: '))
tax = int(input('Thuế suất: '))
actual = int(price * ( 1 + tax / 100))
classify = ""
if actual < 2000000:
    classify = "Nhỏ"
elif actual > 2000000 and actual < 10000000:
    classify = "Vừa"
elif actual > 10000000 and actual < 50000000:
    classify = "Lớn"
else:
    classify = "Rất lớn"
print(actual)
print(classify)
