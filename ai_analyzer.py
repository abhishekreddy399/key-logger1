from collections import Counter
import re

def analyze_keystrokes(log_path='logs/keystrokes.txt'):
    try:
        with open(log_path, 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return {
            'total_keystrokes': 0,
            'most_common_words': [],
            'total_words': 0,
            'raw_text': ''
        }

    chars = []

    for line in lines:
        part = line.split('-')[-1].strip()

        if part == 'SPACE':
            chars.append(' ')
        elif part == 'ENTER':
            chars.append('\n')
        elif len(part) == 1 and part.isprintable():
            chars.append(part)
        else:
            continue  # this ignores shift, ctrl.

    typed_text = ''.join(chars)

     # removes extra spaces and newlines
    cleaned_text = re.sub(r'\s+', ' ', typed_text).strip()

    words = cleaned_text.split()
    word_freq = Counter(words)

    return {
        'total_keystrokes': len(chars),
        'most_common_words': [word for word, _ in word_freq.most_common(5)],
        'total_words': len(words),
        'raw_text': cleaned_text
    }
