import random
import nltk
from nltk import bigrams, FreqDist, ConditionalFreqDist
import os
import string
import heapq

# Download the necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

# Directory where training documents are stored
DATA_DIRECTORY = "data"

# String of punctuation excluding the full stop
PUNCTUATION = string.punctuation.replace('.', '')

def is_hidden_file(filepath):
    """Check if the file is hidden based on its filename."""
    return os.path.basename(filepath).startswith('.')

def clean_text(text):
    """Remove all punctuation from text except full stops."""
    for char in PUNCTUATION:
        text = text.replace(char, '')
    return text

def load_and_clean_data(directory):
    """Load and clean text data from files in the given directory."""
    combined_text = ""
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if not is_hidden_file(filepath):
            with open(filepath) as file:
                for line in file:
                    if line.strip():  # Ignore lines with only whitespace
                        combined_text += clean_text(line)
    return combined_text

def extract_bigrams(text):
    """Tokenize text and generate bigrams."""
    words = nltk.word_tokenize(text.lower())
    return list(bigrams(words))

def get_top_bigrams(bigram_freq_dist, top_k=3):
    """Get the top 'top_k' bigrams for each first word."""
    top_bigrams_per_first_word = {}

    for (first_word, second_word), freq in bigram_freq_dist.items():
        if first_word not in top_bigrams_per_first_word:
            top_bigrams_per_first_word[first_word] = []

        heapq.heappush(top_bigrams_per_first_word[first_word], (freq, second_word))
        if len(top_bigrams_per_first_word[first_word]) > top_k:
            heapq.heappop(top_bigrams_per_first_word[first_word])

    for first_word in top_bigrams_per_first_word:
        sorted_bigrams = sorted(top_bigrams_per_first_word[first_word], reverse=True)
        top_bigrams_per_first_word[first_word] = [second_word for freq, second_word in sorted_bigrams]

    return top_bigrams_per_first_word

def filter_bigrams(top_bigrams_per_first_word):
    """Filter bigrams to only include the top bigrams per first word."""
    filtered_bi_grams = []
    for first_word, second_words in top_bigrams_per_first_word.items():
        for second_word in second_words:
            filtered_bi_grams.append((first_word, second_word))
    return filtered_bi_grams

def generate_sentence(start_word, num_words, bi_gram_freq):
    """Generate a sentence starting from the given word."""
    current_word = start_word.lower()
    for _ in range(num_words):
        print(current_word, end=' ')
        next_words = list(bi_gram_freq[current_word].keys())
        if next_words:
            current_word = random.choice(next_words)
        else:
            break  # Stop if no following words are found
    print()

# Load and process the text data
text_data = load_and_clean_data(DATA_DIRECTORY)

# Extract bigrams from the text data
bi_grams = extract_bigrams(text_data)

# Calculate frequency distribution of bigrams
bi_gram_freq_dist = FreqDist(bi_grams)

# Get top bigrams for each first word
top_bigrams_per_first_word = get_top_bigrams(bi_gram_freq_dist, top_k=3)

# Filter bigrams to only include the top ones
filtered_bi_grams = filter_bigrams(top_bigrams_per_first_word)

# Create a ConditionalFreqDist using filtered bigrams
bi_gram_freq = ConditionalFreqDist(filtered_bi_grams)

# Example of generating a sentence
print("======= Examples =======")
generate_sentence("Incentivo", 15, bi_gram_freq)
generate_sentence("Incentivo", 15, bi_gram_freq)
generate_sentence("Incentivo", 15, bi_gram_freq)
