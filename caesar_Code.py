alphabet = "abcdefghijklmnopqrstuvwxyz"
caesar_Code = input()
shift_Number = int(input())
for i in range(len(caesar_Code)):
    index = int(alphabet.index(caesar_Code[i]))
    caesar_Code=caesar_Code.replace(caesar_Code[i], alphabet[index + shift_Number])
print(caesar_Code)
for i in range(len(caesar_Code)):
    index = int(alphabet.index(caesar_Code[i]))
    caesar_Code=caesar_Code.replace(caesar_Code[i], alphabet[index - shift_Number])
print(caesar_Code)