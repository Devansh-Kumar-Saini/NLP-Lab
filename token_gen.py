import sys
import os

def count_tokens(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        tokens = text.split() 
        print(len(tokens)) 
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python simple_token_counter.py file.txt")
        sys.exit(1)

    count_tokens(sys.argv[1])