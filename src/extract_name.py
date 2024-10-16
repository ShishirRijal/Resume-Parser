"""
extract_name.py

This script extracts names from text using spaCy's Matcher component.

"""

import spacy
from spacy.matcher import Matcher


#! If you don't have the model downloaded, you can download it using the following command
# python -m spacy download en_core_web_sm


# load pre-trained model
nlp = spacy.load("en_core_web_sm")

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)


def extract_name(resume_text):
    """
    Extracts the name from the given text using spaCy's Matcher component.

    Args:
        resume_text (str): The text to extract the name from.

    Returns:
        str: The extracted name, or None if no name is found.
    """
    nlp_text = nlp(resume_text)

    # Patterns to match names (First name, Last name)
    # The idea is that the name is always a proper noun.
    pattern = [
        {"POS": "PROPN"},
        {"POS": "PROPN"},
    ]  # Most common pattern: First name + Last name
    # We can handle the other name formats by just changing the pattern here...

    # Add the pattern to the matcher
    matcher.add("NAME", [pattern])

    # Find matches in the text
    matches = matcher(nlp_text)

    if matches:
        # Return the first matched name
        match_id, start, end = matches[0]
        span = nlp_text[start:end]
        return span.text

    return None  # If no name is found, return None


if __name__ == "__main__":
    resume_text = "Shishir Rijal is a software engineer. He pursued his undergraduate degree in computer science from the Tribhuwan University."
    print("Names found:", extract_name(resume_text))  # Output: Shishir Rijal
