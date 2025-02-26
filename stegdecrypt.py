import cv2

def decrypt_message():
    img = cv2.imread("encryptedImage.png")  # Must match the saved format (e.g., PNG)
    if img is None:
        print("Error: Encrypted image not found!")
        return
    
    height, width, _ = img.shape
    d = {i: chr(i) for i in range(256)}
    n, m, z = 0, 0, 0  # Start at first pixel, first channel
    msg = []
    
    # Extract message until delimiter (255)
    while True:
        val = img[n, m, z]
        if val == 255:
            break
        msg.append(d[val])
        z = (z + 1) % 3
        if z == 0:  # Move to next pixel after reading all 3 channels
            m += 1
            if m >= width:
                m = 0
                n += 1
    
    # Move past the delimiter
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= width:
            m = 0
            n += 1
    
    # Extract password length
    pass_length = img[n, m, z]
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= width:
            m = 0
            n += 1
    
    # Extract password using the stored length
    password = []
    for _ in range(pass_length):
        password.append(d[img[n, m, z]])
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= width:
                m = 0
                n += 1
    
    stored_pass = ''.join(password)
    entered_pass = input("Enter decryption passcode: ")
    
    if entered_pass == stored_pass:
        print("Decrypted message:", ''.join(msg))
    else:
        print("Invalid password!")

if __name__ == "__main__":
    decrypt_message()