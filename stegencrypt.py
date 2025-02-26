import cv2
import tkinter as tk
from tkinter import messagebox

def encrypt_message():
    msg = entry_msg.get()
    password = entry_pass.get()
    input_image = entry_image.get()  # Get image name from GUI entry
    
    if not msg or not password or not input_image:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    img = cv2.imread(input_image)  # Read image with provided name
    if img is None:
        messagebox.showerror("Error", f"Failed to read image: {input_image}")
        return
    
    height, width, _ = img.shape
    
    # Check if image is large enough
    required_pixels = len(msg) + len(password) + 2
    if required_pixels * 3 > height * width * 3:
        messagebox.showerror("Error", "Image too small to embed data!")
        return
    
    d = {chr(i): i for i in range(256)}
    n, m, z = 0, 0, 0
    
    # Embed message
    for char in msg:
        img[n, m, z] = d[char]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= width:
                m = 0
                n += 1
    
    # Embed delimiter (255)
    img[n, m, z] = 255
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= width:
            m = 0
            n += 1
    
    # Embed password length
    pass_length = len(password)
    img[n, m, z] = pass_length
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= width:
            m = 0
            n += 1
    
    # Embed password
    for char in password:
        img[n, m, z] = d[char]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= width:
                m = 0
                n += 1
    
    # Save encrypted image with fixed name
    cv2.imwrite("encryptedImage.png", img)
    messagebox.showinfo("Success", "Encrypted image saved as: encryptedImage.png")

# GUI setup
root = tk.Tk()
root.title("Steganography Encryptor")

tk.Label(root, text="Input Image Name:").pack()
entry_image = tk.Entry(root, width=50)
entry_image.pack()

tk.Label(root, text="Secret Message:").pack()
entry_msg = tk.Entry(root, width=50)
entry_msg.pack()

tk.Label(root, text="Password:").pack()
entry_pass = tk.Entry(root, show="*", width=50)
entry_pass.pack()

tk.Button(root, text="Encrypt", command=encrypt_message).pack(pady=10)

root.mainloop()