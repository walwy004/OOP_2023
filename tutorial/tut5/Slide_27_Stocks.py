stocks = {"GOOGL": (1235.20, 1242.54, 1231.06), "MSFT": (110.41, 110.45, 109.84)}
# print(stocks["GOOGL"])
# print(stocks["AAPL"])

# print(stocks.get("AAPL", "Not found..."))

# print(stocks.setdefault("GOOGL", "Invalid"))
# print(stocks.setdefault("NVDA", (995.48, 1084.16, 3091.81)))
# print(stocks["NVDA"])

# for key in stocks.keys():
#     print(key)

# for value in stocks.values():
#     print(value)

# for key, value in stocks.items():
#     print(f"{key} stock values are: {value}")
    # print(key + " stock values are: " + str(value))

stocks["GOOGL"] = (1245.21, 1252.64, 1245.18)
print(stocks["GOOGL"])

keyExamples = {}
keyExamples["String"] = "A String"
keyExamples[5] = "An Integer"
keyExamples[1.5] = "A Float"
keyExamples[("tuple", 100913)] = "A Tuple"
