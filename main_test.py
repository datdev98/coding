from coding import *

n = int(input("Nhap so nguon tin: "))

sources = []

print("Nhap nguon tin va xac suat: ")
for i in range(n):
    print("Source", i)
    source = input("Name: ")
    prop = float(input("Probability: "))
    sources.append(SourceUnit(source, prop))

print()
code = Shannon(sources)
print(code.encode_table())
print("Average length: ", code.source_units_average_length())
print("K_t: ", code.k_t())
print("K_n: ", code.k_n())

print()
code = ShannonFano(sources)
print(code.encode_table())
print("Average length: ", code.source_units_average_length())
print("K_t: ", code.k_t())
print("K_n: ", code.k_n())

print()
code = Huffman(sources)
print(code.encode_table())
print("Average length: ", code.source_units_average_length())
print("K_t: ", code.k_t())
print("K_n: ", code.k_n())