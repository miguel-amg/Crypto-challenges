# +----------------------------------+
# | The Cryptopals Crypto Challenges |
# | Miguel Guimarães                 |
# +----------------------------------+

# Imports
import base64

# Setup
input_file_path = "files/input_challenge6.txt"

########################################################################################################################
# Frequency of the letters in the english alphabet
freq = {
    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 'e': .12702,
    'f': .02228, 'g': .02015, 'h': .06094, 'i': .06966, 'j': .00153,
    'k': .00772, 'l': .04025, 'm': .02406, 'n': .06749, 'o': .07507,
    'p': .01929, 'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
    'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150, 'y': .01974,
    'z': .00074, ' ': .13000
}

# Breaks the single byte cipher
def single_byte_key(block: bytes) -> int:
    best_score = float('-inf')
    best_key = 0

    # Lets check every possible single byte key
    for k in range(256):
        xord = bytes(b ^ k for b in block)

        score = sum(freq.get(chr(c).lower(), 0) for c in xord) # Sum the score of the frequency of each char 

        # Save the best key
        if score > best_score:
            best_score = score
            best_key = k

    return best_key

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
    best_keysize_1 = keysizes[0][0]
    best_keysize_2 = keysizes[1][0]
    best_keysize_3 = keysizes[2][0]

    print(brute_force_rkx_specific(input, best_keysize_1))
    print(brute_force_rkx_specific(input, best_keysize_2))
    print(brute_force_rkx_specific(input, best_keysize_3))


# Breaks the repeating-key xor for a specific key size
def brute_force_rkx_specific(input: bytes, keysize: int):
    input_array = bytearray(input)
    blocks = []

    # Creating blocks where every byte was applied the same char from the key (see steps 5 and 6)
    for i in range(keysize):
        block = bytes(input_array[i::keysize]) # Picks in i in key_bytes steps
        blocks.append(block)

    # For each block we will find the 'single byte xor cipher' key
    final_key = bytearray()
    for block in blocks:
        key_byte = single_byte_key(block)
        final_key.append(key_byte)

    return final_key.decode('ascii')
    
########################################################################################################################

input_file_bytes = open(input_file_path, "rb").read()
decrypted_file_bytes = base64.b64decode(input_file_bytes)
print(brute_force_rkx(decrypted_file_bytes))