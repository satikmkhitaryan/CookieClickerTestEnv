# text = input("Please enter text consiting less than 20 symbols: ")
# symbol1 = input("Enter a symbol: ")
# if len(text) <= 20:
#     if symbol1 in text:
#      print(text.split(symbol1, 1)[1])
#     else:
#         print("This symbol is not in text. ")
# else:
#     print("Text length must be less then 20. Please  again")
#

word = input("input text")
count = 0
for i in range(count + 1):
    letter = word[:1]
    word = word[count:]
    print(word)
    count += 1


print(count)


