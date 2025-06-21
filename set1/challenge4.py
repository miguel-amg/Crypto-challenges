# +----------------------------------+
# | The Cryptopals Crypto Challenges |
# | Miguel Guimarães                 |
# +----------------------------------+

# Import
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

# Returns the best result from brute-forcing
def brute_force_best(input: bytes):
    best_result_str = ""
    best_result_score = 0

    combs = combinations(input)

    # Iterate every result from applying every key (single byte xor)
    for comb in combs:
        try:
            comb_str = comb.decode("utf-8")
        except UnicodeDecodeError:
            pass
        else:
            score = scoring(comb_str)
            
            # Store the score if it is the best
            if (score > best_result_score): 
                best_result_score = score
                best_result_str = comb_str 

    # Return tuple with the best score and its corresponding string
    return (best_result_score, best_result_str)

# Gets the best brute-force score/output for each line in a file
def get_all_best_scores(input_file):
    list = []
    for line in input_file:
        line_bytes = bytearray.fromhex(line)
        list.append(brute_force_best(line_bytes))

    sorted_list = sorted(list, key=lambda x: x[0], reverse=True)

    return sorted_list[0]

########################################################################################################################

input_file = open("files/input_challenge4.txt")
score, line = get_all_best_scores(input_file)
print(line)

# The result is 'Now that the party is jumping'