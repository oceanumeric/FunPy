import re
from collections import defaultdict
from typing import Dict, List, Any, TypeVar, Iterator, TextIO, Tuple


# Sample text data
text_data = """
Natural language processing (NLP) is a sub-field of artificial intelligence (AI) that focuses on the interaction 
between computers and humans through natural language. The ultimate objective of NLP is to read, decipher, understand, 
and make sense of human languages in a manner that is valuable.
"""


def clean_and_tokenize(text: str) -> Iterator[str]:
    """Clean and tokenize text data"""
    for word in re.sub(r"[^a-zA-Z0-9]", " ", text).lower().split():
        yield word
        

def word_pairs(words: List[str]) -> Iterator[Tuple[str, str]]:
    """Generate word pairs from a list of words"""
    prev_word = None
    for word in words:
        if prev_word:
            yield prev_word, word
        prev_word = word
        

if __name__ == "__main__":
    words = list(clean_and_tokenize(text_data))
    for pair in word_pairs(words):
        print(pair)
        
    # Count word pairs
    word_pair_counts = defaultdict(int)
    for pair in word_pairs(words):
        word_pair_counts[pair] += 1
    
    print("\nWord pair counts:")
    for pair, count in word_pair_counts.items():
        print(pair, count)
    
    most_common_pairs = sorted(word_pair_counts.items(), key=lambda x: x[1], reverse=True)
    
    print(most_common_pairs[:5])