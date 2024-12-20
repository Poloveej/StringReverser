def reverse_string(input_string: str) -> str:
    """Інвертує рядок"""
    return input_string[::-1]

if __name__ == "__main__":
    user_input = input("Введіть рядок для інвертації: ")
    print("Інвертований рядок:", reverse_string(user_input))