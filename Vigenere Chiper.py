def vigenere_encrypt(plain_text, key):
  encrypted_text = ''
  key_len = len(key)
  for i in range(len(plain_text)):
    char = plain_text[i]
    if char.isalpha():
      key_char = key[i % key_len]
      shift = ord(key_char.upper()) - 65
      if char.islower():
        encrypted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
      else:
        encrypted_char = chr(((ord(char) - 65 + shift) % 26) + 65)
      encrypted_text += encrypted_char
    else:
      encrypted_text += char
  return encrypted_text


def vigenere_decrypt(encrypted_text, key):
  decrypted_text = ''
  key_len = len(key)
  for i in range(len(encrypted_text)):
    char = encrypted_text[i]
    if char.isalpha():
      key_char = key[i % key_len]
      shift = ord(key_char.upper()) - 65
      if char.islower():
        decrypted_char = chr(((ord(char) - 97 - shift) % 26) + 97)
      else:
        decrypted_char = chr(((ord(char) - 65 - shift) % 26) + 65)
      decrypted_text += decrypted_char
    else:
      decrypted_text += char
  return decrypted_text


# Fungsi untuk registrasi
def register():
  username = input("Masukkan username: ")
  password = input("Masukkan password: ")
  key = input("Masukkan kunci enkripsi Vigenere: ")

  encrypted_password = vigenere_encrypt(password, key)

  # Simpan username, encrypted_password, dan key ke database atau file
  with open("user_database.txt", "a") as file:
    file.write(f"{username} {encrypted_password} {key}\n")
  print("Pendaftaran berhasil!")


# Fungsi untuk login
def login():
  username = input("Masukkan username: ")
  password = input("Masukkan password: ")

  with open("user_database.txt", "r") as file:
    for line in file:
      parts = line.split()
      if len(parts) == 3:
        stored_username, stored_password, stored_key = parts
        if stored_username == username:
          decrypted_password = vigenere_decrypt(stored_password, stored_key)
          if password == decrypted_password:
            print("Login berhasil!")
            return
  print("Login gagal. Periksa kembali username dan password Anda.")


# Program utama
while True:
  print("1. Register")
  print("2. Login")
  print("3. Keluar")
  choice = input("Pilih opsi (1/2/3): ")

  if choice == '1':
    register()
  elif choice == '2':
    login()
  elif choice == '3':
    break
  else:
    print("Opsi tidak valid. Silakan pilih lagi.")
