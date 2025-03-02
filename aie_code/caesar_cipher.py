def caesarCipher(s, k):
    k = k % 26
    result = ""
    for char in s:
        if "a" <= char <= "z":
            result += chr(ord("a") + (ord(char) - ord("a") + k) % 26)
        elif "A" <= char <= "Z":
            result += chr(ord("A") + (ord(char) - ord("A") + k) % 26)
        else:
            result += char

    return result
