from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size

    # Encrypting image pixels
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            encrypted_pixel = [(p + key) % 256 for p in pixel]  # Shift each color component by the key
            encrypted_pixels.append(tuple(encrypted_pixel))

    # Creating a new image with encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)

    # Save encrypted image
    encrypted_image_path = "encrypted_image.png"
    encrypted_img.save(encrypted_image_path)
    print("Image encrypted and saved as:", encrypted_image_path)

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size

    # Decrypting image pixels
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            decrypted_pixel = [(p - key) % 256 for p in pixel]  # Reverse the encryption process
            decrypted_pixels.append(tuple(decrypted_pixel))

    # Creating a new image with decrypted pixels
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)

    # Save decrypted image
    decrypted_image_path = "decrypted_image.png"
    decrypted_img.save(decrypted_image_path)
    print("Image decrypted and saved as:", decrypted_image_path)

def main():
    choice = input("Enter 'E' to encrypt an image or 'D' to decrypt an image: ").upper()
    if choice == 'E':
        image_path = input("Enter the path to the image file: ")
        while True:
            try:
                key = int(input("Enter the encryption key: "))
                break
            except ValueError:
                print("Invalid key. Please enter an integer value.")

        encrypt_image(image_path, key)
    elif choice == 'D':
        image_path = input("Enter the path to the encrypted image file: ")
        while True:
            try:
                key = int(input("Enter the decryption key: "))
                break
            except ValueError:
                print("Invalid key. Please enter an integer value.")

        decrypt_image(image_path, key)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")


if __name__ == "__main__":
    main()
