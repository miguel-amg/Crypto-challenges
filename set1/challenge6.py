# +----------------------------------+
# | The Cryptopals Crypto Challenges |
# | Miguel Guimarães                 |
# +----------------------------------+

# Imports
import base64
from challenge4 import brute_force_sbx

# Setup
input_file_path = "files/input_challenge6.txt"

########################################################################################################################
# Calculates the hamming distance between two strings
def hamming_distance_bytes(input1: bytes, input2: bytes) -> int:
    if len(input1) != len(input2):
        raise ValueError("Hamming distance needs strings of equal size")
    
    result = 0

    for i in range(0, len(input1)):
        xor = input1[i] ^ input2[i]  # XOR will turn differences into 1
        result += xor.bit_count()    # We will count the different bits in this byte  

    return result

# Ranks the possbile keysizes using hamming distance
def get_keysizes(input: bytes):
    resulting_keysize = 0
    resulting_distances = {}

    for keysize in range(2,40):
        value1 = input[0:keysize]            # Get the first keysize number of bytes
        value2 = input[keysize:(keysize*2)]  # Get the second keysize number of bytes

        distance = hamming_distance_bytes(value1, value2)

        resulting_distances[keysize] = distance / keysize  # Normalizing the result by diving by keysize

    return sorted(resulting_distances.items(), key=lambda x: x[1]) 

# Break the repeating-key xor cipher
def brute_force_rkx(input: bytes):
    keysizes = get_keysizes(input)
    best_keysize = keysizes[0][0]


    return best_keysize
    


########################################################################################################################

input_file_bytes = open(input_file_path, "rb").read()
decrypted_file_bytes = base64.b64decode(input_file_bytes)
print(brute_force_rkx(decrypted_file_bytes))