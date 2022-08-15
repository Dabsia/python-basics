myfile = open('text.txt')
print(myfile.read())

with open('text.txt') as my_NewFile:
    contents = my_NewFile.read()

# st = 'Print only the words that start with s in the sentence'

# stArr = st.split()
# for word in stArr:
#     if word.startswith('s'):
#         print(word)
#         continue

# divisibleBy3 = [n for n in range(0, 51) if n % 3 == 0]
# print(divisibleBy3)

words = 'Print every word in this sentence that has an even number of letters'
newWords = words.split()

for word in newWords:
    if len(word) % 2 == 0:
        print('even')
        continue
    print(word)
