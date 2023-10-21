def IsPalindrome(word):
    count = 0
    for let in set(word):
        count += word.count(let) // 2
    if count == (len(word) - len(word) % 2) // 2:
        return
    return False

