from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b, inverse as inv, getPrime as getP  # pip install pycrypto

def generate():
    p, q = getP(1024), getP(1024)
    e = 65537
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inv(e, phi)
    return n, e, d

def encrypt(n, e, pt):
    pt = b2l(pt.encode())
    ct = l2b(pow(pt, e, n)).hex()
    return ct

def decrypt(ct, n, d):
    pt = pow(ct, d, n)
    try:
        return l2b(pt).decode()
    except:
        return False

def menu():
    print('''Hello, it's an encryptor/decrytor with RSA algoritm of your messages
Before encrypting the data, you can get the keys necessary for the RSA algorithm to work''')
    print('''menu:
1. generate keys
2. encrypt message
3. decrypt message
4. exit''')
    return

def main():
    menu()
    choice = int(input())
    if choice in [1, 2, 3, 4]:
        if choice == 1:
            n, e, d = generate()
            print('n:', n, 'e:', e, 'd:', d, '(e,n) - publick key, (d,n) - private key', sep='\n')
        elif choice == 2:
            pt = input('input your message\n')
            n, e = int(input('input your modular exponentiation in decimal (n)\n')), int(input('input your coprime exponentiation in decimal (e)\n'))
            print('ciphertext(ct): ', encrypt(n, e, pt), sep='\n')
            return
        elif choice == 3:
            try:
                ct = int(input('input your ciphertext in hex (ct)\n'), 16)
                d = int(input('input yout private key exponent in decimal (d)\n'))
                n = int(input('input your modular exponentiation in decimal (n)\n'))
                print('decrypted text:\n', decrypt(ct, n, d))
                return
            except:
                print('some of your input was wrong, try again')
                return
        else:
            exit(0)

if __name__ == '__main__':
    while True:
        main()
