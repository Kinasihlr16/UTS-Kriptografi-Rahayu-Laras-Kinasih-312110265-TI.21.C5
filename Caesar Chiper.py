import string


def create_cipher_map(shift):
  alphabet = string.ascii_uppercase
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  cipher_map = str.maketrans(alphabet, shifted_alphabet)
  return cipher_map


def encrypt_substitution(plaintext, shift):
  cipher_map = create_cipher_map(shift)
  return plaintext.upper().translate(cipher_map)


def decrypt_substitution(ciphertext, shift):
  cipher_map = create_cipher_map(-shift)
  return ciphertext.upper().translate(cipher_map)


# Fungsi untuk menampilkan menu
def display_menu():
  print("=== Menu ===")
  print("1. Enkripsi")
  print("2. Dekripsi")
  print("3. Keluar")


# Contoh penggunaan
while True:
  display_menu()
  choice = input("Pilih tindakan (1/2/3): ")

  if choice == '1':
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")
    shift_amount = int(input("Masukkan jumlah geseran: "))
    encrypted_text = encrypt_substitution(plaintext, shift_amount)
    print("Teks terenkripsi:", encrypted_text)
  elif choice == '2':
    ciphertext = input("Masukkan teks yang ingin didekripsi: ")
    shift_amount = int(input("Masukkan jumlah geseran: "))
    decrypted_text = decrypt_substitution(ciphertext, shift_amount)
    print("Teks terdekripsi:", decrypted_text)
  elif choice == '3':
    break
  else:
    print("Pilihan tidak valid. Silakan coba lagi.")
