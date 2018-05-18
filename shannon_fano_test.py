from coding import *

a = SourceUnit('a', 0.36)
b = SourceUnit('b', 0.18)
c = SourceUnit('c', 0.18)
d = SourceUnit('d', 0.12)
e = SourceUnit('e', 0.09)
f = SourceUnit('f', 0.07)

code = ShannonFano([a, c, b, d, f, e])
print(code)

text = "abcaac"
print("Text:", text)

print("Encode:")
encode = code.encode(text)
print(code.encode_table())
print(encode)

print("Average length: ", code.source_units_average_length())
print("K_t: ", code.k_t())
print("K_n: ", code.k_n())

print("Decode:")
decode = code.decode(encode)
print(code.decode_table())
print(decode)