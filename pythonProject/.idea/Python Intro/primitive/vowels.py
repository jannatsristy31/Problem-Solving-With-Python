def count_vowels(input, txt):
    txt = txt.lower()
    for x in txt:
        if x in input:
            input[x] += 1
    return input


input = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
txt = "unga bunga"

print(count_vowels(input,txt))
