import re

def clean_fen(fen):
    # Remove characters starting from "-"
    fen = re.split(r"[-]", fen, maxsplit=1)[0].strip()
    
    # Replace "\" with "0"
    fen = fen.replace("/", "0")
    
    return fen

# Example usage
example_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
cleaned_fen = clean_fen(example_fen)

print(cleaned_fen)