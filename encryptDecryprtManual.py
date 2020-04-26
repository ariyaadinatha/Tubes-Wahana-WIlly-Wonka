from cryptography.fernet import Fernet
key = b'EXiOWY1qNCF39AfV4j8GKMZBUvnlMufhwPwm4bfjMPU='
cipher = Fernet(key)
password = 'asd'
#cipher_text = cipher.encrypt(password.encode())
cipher_text= b'gAAAAABepT1E0I6IlDRr5uDyfpQRSKEKq1rB8EErKvOJB9tJUHXpC5zLjIY31gWCa4I6UriYZuZQp0KZCnEAaZ00ocsnYUvCkw=='
plain_text = cipher.decrypt(cipher_text)
#print(cipher)
#print(key.decode())
print(plain_text.decode())
print(cipher_text.decode())
