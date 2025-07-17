# +----------------------------------+
# | The Cryptopals Crypto Challenges |
# | Miguel Guimarães                 |
# +----------------------------------+

# Imports
import base64
import cryptography
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Setup
input_file_path = "files/input_challenge7.txt"

def aes_128_ecb_decipher(input: bytes, key: str):
    key_bytes = str.encode(key)
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    



########################################################################################################################
# Main function
if __name__ == "__main__":
    input_file_bytes = open(input_file_path, "rb").read()
    decrypted_file_bytes = base64.b64decode(input_file_bytes)
