# +----------------------------------+
# | The Cryptopals Crypto Challenges |
# | Miguel Guimarães                 |
# +----------------------------------+

# Applies xor of each byte of the key
def repeating_key_xor(input: bytes, key: bytes):
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
# Inputs
input = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"

# To bytes
input_bytes = input.encode()
key_bytes = key.encode()

# Apply the repeating key xor
output = repeating_key_xor(input_bytes, key_bytes)

# Format the output to hex
output_str = output.hex()
print(output_str)

assert output_str == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
