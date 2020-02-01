# Задача.
# Вход: хэш SHA-1
# Условия: максимум 5 символов и используются только строчные буквы (a-z)
# Выход: функция которая принимает на вход хеш и возврашает расшифрованный пароль.
#
# a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
#
# 77be4fc97f77f5f48308942bb6e32aacabed9cef
import hashlib
from string import ascii_lowercase
from itertools import permutations


def get_pwd_combinations(iterable, len_of_pwd):
    lst_of_pwds = list(permutations(iterable, len_of_pwd))
    pwds = []
    for elem in lst_of_pwds:
        pwd = ''.join(elem)
        pwds.append(pwd)
    return pwds


def get_pwd_from_hash(hash, passwords):
    for pwd in passwords:
        pwd_hash = hashlib.sha1(bytes(pwd, encoding='utf-8'))
        if pwd_hash.hexdigest() == hash:
            return pwd
    return


def main():
    passwords = get_pwd_combinations(ascii_lowercase, 4)
    print(get_pwd_from_hash('e6fb06210fafc02fd7479ddbed2d042cc3a5155e', passwords))


if __name__ == '__main__':
    main()