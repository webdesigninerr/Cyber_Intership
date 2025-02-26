# Secure Data Hiding in Image Using Steganography

## Overview

This project implements a password-protected steganography tool that embeds encrypted messages into images using pixel-channel manipulation. The approach ensures controlled access and reliable extraction, enhancing traditional steganography techniques with robust security features.

## Features

1. __Password-Protected Steganography:__ Only authorized users with the correct password can decrypt the embedded message.

2. __Dynamic Data Embedding:__ Supports variable-length messages and passwords with precise extraction.

3. __Pixel-Channel Manipulation:__ Utilizes all three RGB channels for efficient data storage.

4. __Lossless Image Format Support:__ Saves encrypted images in PNG format to prevent compression-based data loss.

5. __User-Friendly GUI:__ Simplifies encryption and decryption through an intuitive graphical interface.

6. __Error Handling and Validation:__ Ensures compatibility of image sizes and prevents runtime errors.

7. __Customizable Input Image:__ Users can choose any image file for encryption.

8. Secure Delimiter System: Uses a unique delimiter (ASCII 255) to separate message and password during embedding and extraction.

## Technologies Used

  * __Python:__ Core programming language

  * __OpenCV (cv2):__ Image processing and manipulation

  * __Tkinter:__ GUI toolkit for user interface

  * __NumPy:__ Array-based image data manipulation

  * __File I/O:__ Handling PNG/JPEG image files for data embedding and retrieval

## Installation

* Clone the repository:

git clone https://github.com/yourusername/secure-steganography.git

* Navigate to the project directory:

cd secure-steganography

* Install dependencies:

pip install opencv-python numpy tkinter

* Run the application:

python steganography_gui.py

## Usage

1. __Encrypt Message:__

* Load an image.

* Enter the message and password.

* Click "Encrypt" to generate a steganographic image.

2. __Decrypt Message:__

* Load the steganographic image.

* Enter the correct password.

* Click "Decrypt" to retrieve the message.

## End Users

1. Cybersecurity professionals for covert data transfer.

2. Individuals seeking secure communication channels.

3. Researchers and developers exploring data hiding techniques.

## Results

* Successfully implemented password-protected message embedding and extraction.

* Efficient data concealment within RGB pixel values without visible image distortion.

* User-friendly GUI for secure encryption and decryption.

## Future Scope

1. Advanced Encryption: Integrate AES or RSA encryption for enhanced message security.

2. Multi-Layer Steganography: Implement multi-level embedding for additional obfuscation.

3. Support for Other Formats: Expand compatibility to GIF and BMP formats.

4. Cloud Integration: Enable secure message storage and retrieval via cloud services.

5. Steganalysis Resistance: Enhance the algorithm to resist detection by steganalysis techniques.

6. Mobile Application: Develop an Android/iOS app for on-the-go steganography.

## Conclusion

This project successfully addresses the limitations of traditional steganography methods by integrating password protection and efficient pixel-channel manipulation. The implemented solution ensures secure and reliable data hiding while maintaining image integrity. Future improvements can further enhance security, usability, and adaptability across different platforms.

