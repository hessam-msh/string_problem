"""
    First Solution
"""
import re

text = input()
if re.search(r"AB.*BA|BA.*AB", text):
    print("Yes")

"""
    Second Solution
"""
# word = input()
# ab_pos = word.find('AB')
# ba_pos = word.find('BA')
# if ab_pos != -1 and ba_pos != -1:
#     if word.find('BA', ab_pos + 2) != -1:
#         print("YES")
#     elif word.find('AB', ba_pos + 2) != -1:
#         print('YES')
#     else:
#         print("NO")
# else:
#     print('NO')
