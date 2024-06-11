from PIL import Image

def encrypt_image(image_path, key, output_path):
  """Encrypts an image using pixel value XOR with a key."""
  image = Image.open(image_path)
  pixels = image.load()
  width, height = image.size

  # Convert key to a list of integers (assuming single char key for simplicity)
  key_int = ord(key)

  for y in range(height):
    for x in range(width):
      r, g, b = pixels[x, y]
      new_red = r ^ key_int
      new_green = g ^ key_int
      new_blue = b ^ key_int
      pixels[x, y] = (new_red, new_green, new_blue)

  image.save(output_path)

def decrypt_image(image_path, key, output_path):
  """Decrypts an encrypted image using the same key."""
  image = Image.open(image_path)
  pixels = image.load()
  width, height = image.size

  # Convert key to integer again
  key_int = ord(key)

  for y in range(height):
    for x in range(width):
      r, g, b = pixels[x, y]
      new_red = r ^ key_int
      new_green = g ^ key_int
      new_blue = b ^ key_int
      pixels[x, y] = (new_red, new_green, new_blue)

  image.save(output_path)

# Example usage
image_path = r"C:\Users\vickyy\Downloads\ThinkstockPhotos-72967326.jpg"
key = "S"  # Replace with your desired key (single character for simplicity)
encrypted_path = r"C:\Users\vickyy\Downloads\encrypted_image.jpg"
decrypted_path = r"C:\Users\vickyy\Downloads\decrypted_image.jpg"

encrypt_image(image_path, key, encrypted_path)
decrypt_image(encrypted_path, key, decrypted_path)

print(f"Image encrypted and saved to: {encrypted_path}")
print(f"Image decrypted and saved to: {decrypted_path}")