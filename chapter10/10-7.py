"""
10–7. Exceptions. What is the difference between Python
pseudocode snippets (a) and (b)? Answer in the context of
statements A and B, which are part of both pieces of code.
(Thanks to Guido for this teaser!)
(a) try:
        statement_A
    except . . .:
        . . .
    else:
        statement_B
(b) try:
        statement_A
        statement_B
    except . . .:
        . . .
"""

"""
Solution: 两者的statement_B语句都是仅当statement_A不抛出异常时才会执行；而对于(a)，若statement_B执行时遇到
错误抛出异常给上层调用者，程序下一步执行逻辑不可控；而(b)中statement_B若执行遇到错误抛出异常时可以被外层的except语句捕获，
处理异常后程序按预定逻辑继续执行。
"""