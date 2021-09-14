import hashlib

def encrypt_md5(word):
    return hashlib.md5(word.encode('utf-8')).hexdigest()

def encrypt_sha1(word):
    return hashlib.sha1(word.encode('utf-8')).hexdigest()

word = input('Введите слово или фразу для шифрования: ')
print('Каким способом зашифровать?\n1. MD5\n2. SHA1')
choice = input()

print('Вот что получилось: ')
if choice == '1': print(encrypt_md5(word)) 
elif choice == '2': print(encrypt_sha1(word))
else: print('Такого варианта не прредусмотренно.Выберите 1 или 2')
