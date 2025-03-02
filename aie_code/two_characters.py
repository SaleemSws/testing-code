# # 1.ต้องลบตัวอักษรออกจากสตริงจนกว่าจะเหลือตัวอักษรที่แตกต่างกันเพียงสองตัว
# # 2.ตัวอักษรสองตัวนี้ต้องสลับกัน(ไม่มีตัวอักษรเดียวกันติดกัน)
# # 3.ต้องหาความยาวสูงสุดที่เป็นไปได้ของสตริงดังกล่าว


def alternate(s):
    unique_chars = list(set(s))
    max_length = 0

    if len(unique_chars) < 2:
        return 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1 = unique_chars[i]
            c2 = unique_chars[j]
            filtered = ""
            for char in s:
                if char == c1 or char == c2:
                    filtered += char
            # Check if the filtered string alternates
            is_alternating = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k - 1]:
                    is_alternating = False
                    break

            # Update max length if this is valid and longer
            if is_alternating and len(filtered) > 0:
                max_length = max(max_length, len(filtered))

    return max_length
