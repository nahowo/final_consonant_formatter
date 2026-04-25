<!--
SPDX-FileCopyrightText: 2026 Nahyun Park <nahowo@naver.com>

SPDX-License-Identifier: MIT
-->

# Final_Consonant_Formatter
A simple Python package to attach correct case particles based on whether a Korean syllable ends with a final consonant. 

### How to use
1. Install final_consonant_formatter package
    ```
    pip install final_consonant_formatter
    ```
2. Import final_consonant_formatter package in python file or terminal
    ```py
    from fc_formatter import attach_iga, attach_eulreul
    ```
3. Use attach_iga function
    ```py
    print(f'{attach_iga("파이썬")} 재밌다!') # 파이썬이 재밌다!
    print(f'{attach_iga("자바")} 재밌다!') # 자바가 재밌다!
    ```
4. Use attach_eulreul function
    ```py
    print(f'{attach_eulreul("파이썬")} 공부한다!') # 파이썬을 공부한다!
    print(f'{attach_eulreul("자바")} 공부한다!') # 자바를 공부한다!
    ```
