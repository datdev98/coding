from coding import *

a = SourceUnit('a', 0.36)
b = SourceUnit('b', 0.18)
c = SourceUnit('c', 0.18)
d = SourceUnit('d', 0.12)
e = SourceUnit('e', 0.09)
f = SourceUnit('f', 0.07)

code = Shannon([a, c, b, d, f, e])

text = 'afca'
encode = code.encode(text)

print(encode)
print(code.encode_table())
print(code.decode(encode))
print(code.source_units_average_length())
print(a.entropy())
print(code.entropy())
print(code.k_n())
print(code.k_t())