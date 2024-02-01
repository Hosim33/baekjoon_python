word=input()
result = ''

for i in word:
    if i.islower():
            if 97 <= ord(i) <= 109:
                result += chr(ord(i) + 13)
            else:
                result += chr(ord(i) - 13)
    elif i.isupper():
        if 65 <= ord(i) <= 77:
            result += chr(ord(i) + 13)
        else:
            result += chr(ord(i) - 13)
    else:
        result += i

print(result)
