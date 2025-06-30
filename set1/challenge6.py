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

def get_keysizes(input: bytes):
    resulting = []

    for keysize in range(2, 40):
        # Extract 4 blocks of 'keysize' size
        b1 = input[0:keysize]
        b2 = input[keysize:2*keysize]
        b3 = input[2*keysize:3*keysize]
        b4 = input[3*keysize:4*keysize]
        
        # If the last block is incomplete we will stop
        if len(b4) < keysize: break

        # Calculate the 6 distances
        d12 = hamming_distance_bytes(b1, b2)
        d13 = hamming_distance_bytes(b1, b3)
        d14 = hamming_distance_bytes(b1, b4)
        d23 = hamming_distance_bytes(b2, b3)
        d24 = hamming_distance_bytes(b2, b4)
        d34 = hamming_distance_bytes(b3, b4)

        # Get the average of the hamming distances
        avg_dist = (d12 + d13 + d14 + d23 + d24 + d34) / 6.0
        norm = avg_dist / keysize

        resulting.append((keysize, norm))

    # Return the keysizes, ordered by the best hamming distances score
    return sorted(resulting, key=lambda x: x[1])

# Break the repeating-key xor cipher
def brute_force_rkx(input: bytes):
    keysizes = get_keysizes(input)
    best_keysize = keysizes[0][0]

    input_array = bytearray(input)
    blocks = []

    # Creating blocks where every byte was applied the same char from the key (see steps 5 and 6)
    for i in range(best_keysize):
        block = bytes(input_array[i::best_keysize]) # Picks in i in key_bytes steps
        blocks.append(block)

    # For each block we will find the 'single byte xor cipher' key
    final_key = bytearray()
    for block in blocks:
        key_byte = single_byte_key(block)
        final_key.append(key_byte)

    return final_key.decode('ascii')
    
# Deciphers using 'repeating key xor cipher'
def rkx_decipher(input: bytes, key: bytes):
    input_array = bytearray(input)
    key_array   = bytearray(key)

    current_key_byte = key_array[0]
    current_pos = 0

    # Apply every byte of the key to the input in repeating order
    for i in range (0, len(input_array)):
        input_array[i] = input_array[i] ^ current_key_byte

        # Update the current key byte
        if current_pos == (len(key_array) - 1):
            current_pos = 0
        else:
            current_pos += 1
        
        current_key_byte = key_array[current_pos]

    return input_array


########################################################################################################################
# Main function
if __name__ == "__main__":
    input_file_bytes = open(input_file_path, "rb").read()
    decrypted_file_bytes = base64.b64decode(input_file_bytes)
    key = brute_force_rkx(decrypted_file_bytes)
    print("Key: " + key)
    deciphered_file = rkx_decipher(decrypted_file_bytes, bytes(key.encode('ascii')))
    print(bytes(deciphered_file).decode('ascii'))