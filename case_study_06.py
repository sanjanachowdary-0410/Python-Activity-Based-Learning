texts = ["aaabbbbbcc", "abcd", "aabbcc", ""]

for text in texts:
    if len(text) == 0:
        encoded = ""
    else:
        encoded = ""
        run_len = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                run_len += 1
            else:
                encoded = encoded + text[i - 1] + str(run_len)
                run_len = 1
        encoded = encoded + text[-1] + str(run_len)

    beneficial = len(encoded) < len(text) and len(text) > 0
    print(
        f"Orig: '{text}' (len={len(text)}) | "
        f"Enc: '{encoded}' (len={len(encoded)}) | "
        f"Beneficial: {beneficial}"
    )
