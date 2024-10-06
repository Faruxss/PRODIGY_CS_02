from PIL import Image
import os

def encrypt_image(image_path, output_path, key):
    try:
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size
        key = key % 256
        
        for i in range(width):
            for j in range(height):
                r, g, b, *optional_alpha = pixels[i, j]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                if optional_alpha:  # Handle alpha channel
                    a = optional_alpha[0]
                    pixels[i, j] = (r, g, b, a)
                else:
                    pixels[i, j] = (r, g, b)
        
        image.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(image_path, output_path, key):
    try:
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size
        key = key % 256

        for i in range(width):
            for j in range(height):
                r, g, b, *optional_alpha = pixels[i, j]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                if optional_alpha:  # Handle alpha channel
                    a = optional_alpha[0]
                    pixels[i, j] = (r, g, b, a)
                else:
                    pixels[i, j] = (r, g, b)
        
        image.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def get_valid_key():
    while True:
        try:
            key = int(input("Enter the encryption key (a number between 0 and 255): ").strip())
            if 0 <= key <= 255:
                return key
            else:
                print("Please enter a key between 0 and 255.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        try:
            choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").lower()
            if choice not in ['e', 'd']:
                print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
                continue
            
            image_path = input("Enter the path of the image: ").strip().strip('"')
            output_path = input("Enter the output path for the new image: ").strip().strip('"')
            
            if not os.path.isfile(image_path):
                print(f"The file {image_path} does not exist. Please provide a valid file.")
                continue
            
            key = get_valid_key()

            if choice == 'e':
                encrypt_image(image_path, output_path, key)
            elif choice == 'd':
                decrypt_image(image_path, output_path, key)
            
            another_operation = input("Do you want to perform another operation? (yes/no): ").lower()
            if another_operation != 'yes':
                print("Goodbye!")
                break

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
