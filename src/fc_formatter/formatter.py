def attach_iga(word: str) -> str:
    if not word:
        return word
    
    last_char = word[-1]
    if not ('가' <= last_char <= '힣'):
        return f"{word}(이)가"
    if (ord(last_char) - 44032) % 28 > 0:
        return f"{word}이"
    else:
        f"{word}가"