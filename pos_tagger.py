import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('stopwords')

# Get English stopwords
stop_words = set(stopwords.words('english'))

def pos_tag_text(input_file, output_file=None):
    # Read the input file and convert to lowercase
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    
    # Tokenize the text into words and remove stopwords
    tokens = [word for word in word_tokenize(text) if word.lower() not in stop_words and word.isalnum()]
    
    # Perform POS tagging
    tagged = pos_tag(tokens)
    
    # Print the results
    print("POS Tagging Results:")
    print("-" * 40)
    print(f"{'Word':<15} | {'POS Tag'}")
    print("-" * 40)
    for word, tag in tagged:
        print(f"{word:<15} | {tag}")
    
    # Save to output file if specified
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Word, POS Tag\n")
            for word, tag in tagged:
                f.write(f"{word}, {tag}\n")
        print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    input_file = "text.txt"  # Change this if your file has a different name
    output_file = "pos_tags.csv"  # Output file name (optional)
    
    print(f"Processing file: {input_file}")
    pos_tag_text(input_file, output_file)
