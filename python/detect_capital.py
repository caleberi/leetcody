def detect_capital(string):
    return string.isupper() or string.istitle() or string.islower()


print(detect_capital("USA"))
print(detect_capital("lower"))
print(detect_capital("flaG"))
