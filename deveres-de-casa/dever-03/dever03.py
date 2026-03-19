def check_palindrome(word: str, i, l):
    if i == l - 1:
        return True
    if word[i] != word[l - 1]:  # R A C O C A R
        return False

    return check_palindrome(word, i + 1, l - 1)


"""
solução iterativa I

def iterativo(word: str):
    p = word[::-1]
    if word == p:
        print("É um palindromo")
    else:
        print("Não é")



solução iterativa II

def iterativOO(word: str):

    j = len(word)
    print(j)
    for i in range(len(word) // 2):
        if word[i] != word[j - 1]:  # 0 != 3  1 != 2
            return print("Não é um palindromo")
        j = j - 1
        print(f"iterações: {1 + i}")
    return print("É um palindromo")

"""
print(check_palindrome("ovo", 0, 3))

print(check_palindrome("asjdh", 0, 5))

print(check_palindrome("racecar", 0, 7))

print(check_palindrome("raczcar", 0, 7))

print(check_palindrome("raoecar", 0, 7))
