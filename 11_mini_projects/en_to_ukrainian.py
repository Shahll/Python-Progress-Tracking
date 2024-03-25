def translate_to_ukrainian(input_text):
    keyboard_mapping = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е',
        'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
        '[': 'х', ']': 'ї', 'a': 'ф', 's': 'і', 'd': 'в',
        'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л',
        'l': 'д', ';': 'ж', "'": 'є', 'z': 'я', 'x': 'ч',
        'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',
        ',': 'б', '.': 'ю', '/': '.'
    }
    translated_text = ""
    for char in input_text:
        if char.lower() in keyboard_mapping:
            translated_text += keyboard_mapping[char.lower()]
        else:
            translated_text += char
    return translated_text

input_text = input("Enter English text: ")
output_text = translate_to_ukrainian(input_text)
print(output_text)
