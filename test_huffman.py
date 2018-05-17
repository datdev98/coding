from coding import *


text = "khong co gi quy hon doc lap tu do"
code = Huffman(Coding.source_units_from_text("khong co gi quy hon doc lap tu do"))

print("Text:", text)

print("Encode:")
encode = code.encode(text)
print(code.encode_table())
print(encode)

print("Decode:")
decode = code.decode(encode)
print(code.decode_table())
print(decode)