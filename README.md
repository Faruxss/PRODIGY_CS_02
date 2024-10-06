

---

# Image Encryption and Decryption Tool

This Python tool allows you to encrypt and decrypt images using a simple XOR-based algorithm. It supports images with or without transparency and operates by shifting the RGB values of each pixel by a specified key.

## Features

- Encrypts images by shifting RGB values using a user-specified key.
- Decrypts images using the same key that was used for encryption.
- Supports images with transparency (e.g., PNG with alpha channel).
- Validates the key to be within the range of 0-255.
- Handles file path validation and provides error handling for smoother usage.

## How It Works

The encryption and decryption processes are based on shifting the RGB (red, green, blue) values of each pixel in the image. The shift amount (or key) is entered by the user and is applied to each pixel. For decryption, the same key is used to reverse the shift.

### Workflow:

1. User chooses whether to encrypt or decrypt an image.
2. The tool accepts the input image path, output path, and a key between 0 and 255.
3. The tool shifts each pixel's RGB values by the key and saves the new image.
4. Images with transparency are also supported, where the alpha channel remains unchanged during encryption/decryption.

## Prerequisites

To run this tool, you'll need:

- **Python 3.x** installed on your system.
- The **Pillow** library installed. You can install it using the following command:

```bash
pip install pillow
```

## How to Use

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Faruxss/image-encryption-tool.git
cd image-encryption-tool
```

### 2. Running the Program

To run the program, simply execute the Python script:

```bash
python image_encryption_tool.py
```

### 3. Encrypting an Image

When prompted, choose to encrypt the image and provide the necessary inputs:

```bash
Do you want to (E)ncrypt or (D)ecrypt an image? e
Enter the path of the image: path/to/input_image.png
Enter the output path for the new image: path/to/output_image.png
Enter the encryption key (a number between 0 and 255): 123
Image encrypted and saved as path/to/output_image.png
```

### 4. Decrypting an Image

To decrypt an image, follow similar steps and use the same key that was used during encryption:

```bash
Do you want to (E)ncrypt or (D)ecrypt an image? d
Enter the path of the image: path/to/encrypted_image.png
Enter the output path for the new image: path/to/decrypted_image.png
Enter the encryption key (a number between 0 and 255): 123
Image decrypted and saved as path/to/decrypted_image.png
```

## Code Structure

- **`encrypt_image(image_path, output_path, key)`**: Encrypts the image by shifting the RGB values of each pixel by the provided key.
- **`decrypt_image(image_path, output_path, key)`**: Decrypts the image by reversing the RGB shift using the provided key.
- **`get_valid_key()`**: Ensures that the user provides a valid key between 0 and 255.
- **`main()`**: Main loop that prompts the user for encryption or decryption options and handles the execution.


## Error Handling

The tool includes error handling to manage cases such as:

- Invalid file paths
- Unsupported image formats
- Incorrect key input (non-integer values or values outside the valid range)

## Contributing

Contributions are welcome! If you encounter any bugs or have suggestions for improvements, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

