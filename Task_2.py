from itertools import count

filename_in = 'dz6_book.txt'
filename_out = 'dz6_encodebook.txt'
filename_or = 'dz6_decodebook.txt'

def orig_text(file):
    with open(file,'r') as f:
       for i in f:
            txt = ''.join(str(i))
    return (txt)


def encode_text(file_in,file_out):
    with open(file_in, 'r') as f:
        for i in f:
            txt = ''.join(str(i))
    enc_str = ""
    i = 0
    while (i<= len(txt)-1):
        count = 1
        ch = txt[i]
        j = i
        while (j < len(txt) - 1):
            if (txt[j] == txt[j + 1]):
                count +=1
                j += 1
            else:
                break
        enc_str += str(count) + ch
        i = j + 1
    with open(file_out, 'w') as f:
        f.write(enc_str)
    return enc_str

def decode_text(file_out, file_r):
    with open(file_out, 'r') as f:
        for i in f:
            txt = "".join(str(i))
    dec_str = ""
    i = 0
    j = 0
    while(i <= len(txt) - 1):
        count = int(txt[i])
        word = txt[i + 1]
        for j in range(count):
            dec_str += word
            j = j+1
        i = i+2
    with open(file_r, 'w') as f:
        f.write(dec_str)
    return dec_str
print(f'Оригинальный текст: \n {filename_in}')
print('')
print(f'Сжатый текст: \n {filename_in,filename_out}')
print('')
print(f'Вернули текст: \n {filename_in, filename_or}')





