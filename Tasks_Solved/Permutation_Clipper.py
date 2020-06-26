"""

You found your very first laptop in the attic, and decided to give in to nostalgia and turn it on.
The laptop turned out to be password protected, but you know how to crack it: you have always used the same password,
but encrypt it using permutation ciphers with various keys. The key to the cipher used to protect your old laptop
very conveniently happened to be written on the laptop lid.

Here's how permutation cipher works: the key to it consists of all the letters of the alphabet written up in some order.
All occurrences of letter 'a' in the encrypted text are substituted with the first letter of the key, all occurrences
of letter 'b' are replaced with the second letter from the key, and so on, up to letter 'z' replaced with the last
symbol of the key.

Given the password you always use, your task is to encrypt it using the permutation cipher with the given key.

"""

def permutationCipher(password, key):
    table = {i + 97 : ord(key[i]) for i in range(0, 26)}
    return password.translate(table)

print(permutationCipher("iamthebest", "zabcdefghijklmnopqrstuvwxy"))        # hzlsgdadrs
print(permutationCipher("codesignalrocks", "ebtyfkudagizxmvcnojqwlsrhp"))   # tvyfjaumezovtij

