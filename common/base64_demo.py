import base64

be = base64.b64encode(b'binary\x00string')
print(be)

bd = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(bd)


def safe_base64_decode(s):
    count = len(s) % 4
    print(count)

    while len(s) % 4 != 0:
        s = s + b'='

    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')