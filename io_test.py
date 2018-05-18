from coding import *

with open("./input.txt", 'r') as fin:
    text = fin.read()
    coding = Shannon(Coding.source_units_from_text(text))
    print(coding)
    code = coding.encode(text)
    print("Encode table: ", coding.encode_table())
    print ("K_t: ", coding.k_t())
    print ("K_n: ", coding.k_n())
    with open("./code.txt", 'w') as fout:
        fout.write(code)

    with open("./code.txt", 'r')  as fin:
        code = fin.read()
        text = coding.decode(code)
        with open("./text.txt", 'w') as fout:
            fout.write(text)