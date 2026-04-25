# SPDX-FileCopyrightText: 2026 Nahyun Park <nahowo@naver.com>
#
# SPDX-License-Identifier: MIT

def attach_iga(word: str) -> str:
    if not word:
        return word
    
    last_char = word[-1]
    if not ('가' <= last_char <= '힣'):
        return f"{word}(이)가"
    if (ord(last_char) - 44032) % 28 > 0:
        return f"{word}이"
    else:
        return f"{word}가"
    
def attach_eulreul(word: str) -> str:
    if not word:
        return word
    
    last_char = word[-1]
    if not ('가' <= last_char <= '힣'):
        return f"{word}(을)를"
    if (ord(last_char) - 44032) % 28 > 0:
        return f"{word}을"
    else:
        return f"{word}를"