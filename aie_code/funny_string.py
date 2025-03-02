def funnyString(s):
    reverse_s = s[::-1]
    s_diff = []
    rs_diff = []

    for i in range(len(s) - 1):
        diff = abs(ord(s[i]) - ord(s[i + 1]))
        s_diff.append(diff)

    for j in range(len(reverse_s) - 1):
        diffs = abs(ord(reverse_s[j]) - ord(reverse_s[j + 1]))
        rs_diff.append(diffs)

    if s_diff == rs_diff:
        return "Funny"
    else:
        return "Not Funny"
