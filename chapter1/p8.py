def cipher(tar):
    ans = ""
    for char in tar:
        if char.islower():
            ans += chr(219 - ord(char))
        else:
            ans += char
    return ans

print("文字列を入力してください: ")
result = cipher(input())

print("暗号化: {}".format(result))
print("複合化: {}".format(cipher(result)))
