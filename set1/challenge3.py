# +----------------------------------+
# | The Cryptopals Crypto Challenges |
# | Miguel Guimarães                 |
# +----------------------------------+

# Imports
import string

# Xor function
def xor (input1: bytes, input2: bytes):
    if len(input1) != len(input2): raise ValueError('The input sizes must be the same for XOR.') 
    
    result = bytearray(input1)
    input2_array= bytearray(input2)
    
    # XOR of each byte in the input1 array and the input2 array
    for i in range(0, len(input1)):
        result[i] = result[i] ^ input2_array[i] 
    
    return result

# Function that creates every single byte xor possible
def combinations(input: bytes):
    size = len(input)
    result = []

    # Iterate all keys (all bytes possible)
    for i in range(0,256):
        temp = bytearray(input)
        
        # XOR every byte with the current key 'i'
        for w in range(0, size):
            temp[w] = temp[w] ^ i          
        
        # Store the xor of the input with the current key
        result.append(bytes(temp))

    return result
    
# Very simple scoring system that checks the frequency of the most used caraters
def scoring(text: str):
    frequent_letters = set('aeiouwy')
    alphabet = set(string.ascii_lowercase)
    extras = {'\''} | {' '} | {'\n'}
    
    result = 0
    
    for letter in text:
        if letter.lower() in frequent_letters:
              result += 1
        
        # If a char thats not used in the english alphabet appears then we will give it a score of 0
        if (letter.lower() not in extras) and (letter.lower() not in alphabet):
            return 0
    
    return result

# Checks every possible key and ranks every result
def brute_force(input: bytes):
    results = []
    combs = combinations(input)

    # Iterate every result from applying every key (single byte xor)
    for comb in combs:
        try:
            comb_str = comb.decode("utf-8")
        except UnicodeDecodeError:
            pass
        else:
            score = scoring(comb_str)
            results.append((score, comb_str)) 
        
    ranked = sorted(results, key=lambda x: x[0], reverse=True)

    return ranked    
    
########################################################################################################################

input_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
input_bytes = bytearray.fromhex(input_hex)

print(brute_force(input_bytes))

# The result is 'Cooking MC's like a pound of bacon'