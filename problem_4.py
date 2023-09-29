def duplicates(s: str) -> int:
    letters = {}
    seen = set()
    for letter in s:
        letter = letter.lower()
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
        if letters[letter] > 1 and letter not in seen:
            seen.add(letter)

    return len(seen)

print(duplicates('abcde'))
print(duplicates('aabbcde'))
print(duplicates('aabBcde'))
print(duplicates('indivisibility'))
print(duplicates('Indivisibilities'))
print(duplicates('aA11'))
print(duplicates('ABBA'))