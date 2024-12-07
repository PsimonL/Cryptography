import numpy as np

sbox = {
    0x0: 0xE,
    0x1: 0x4,
    0x2: 0xD,
    0x3: 0x1,
    0x4: 0x2,
    0x5: 0xF,
    0x6: 0xB,
    0x7: 0x8,
    0x8: 0x3,
    0x9: 0xA,
    0xA: 0x6,
    0xB: 0xC,
    0xC: 0x5,
    0xD: 0x9,
    0xE: 0x0,
    0xF: 0x7
}

def int_to_bit_array(number, bits=4):
    return [(number >> i) & 1 for i in range(bits-1, -1, -1)]

def linear_approximation_table(sbox):
    LAT = np.zeros((16, 16), dtype=int)
    
    for a in range(16): 
        A_bits = int_to_bit_array(a)
        for b in range(16):  
            B_bits = int_to_bit_array(b)
            count = 0 
            
            for input_val in range(16):  
                output_val = sbox[input_val]
                
                input_bits = int_to_bit_array(input_val)
                output_bits = int_to_bit_array(output_val)
                
                x_val = sum(A_bits[i] * input_bits[i] for i in range(4)) % 2
                y_val = sum(B_bits[i] * output_bits[i] for i in range(4)) % 2
                
                if x_val == y_val:
                    count += 1
            
            LAT[a][b] = count
    
    return LAT

LAT = linear_approximation_table(sbox)

print("Linear Approximation Table:")
for row in LAT:
    print(" ".join(f"{val:2d}" for val in row))

SDT = (LAT - 8) / 16.0
print("\nStandard Deviation Table:")
for row in SDT:
    print(" ".join(f"{val:+.3f}" for val in row))
