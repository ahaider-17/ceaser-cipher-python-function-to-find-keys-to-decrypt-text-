def decrypt(text):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"

    for shift in range(1, 36):
        shifted_chars = chars[-shift:] + chars[:-shift]

        table = str.maketrans(
            chars + chars.upper(),
            shifted_chars + shifted_chars.upper()
        )

        print(f"Key {shift}: {text.translate(table)}")


encrypted_text = input("Enter encrypted text: ")

decrypt(encrypted_text)
