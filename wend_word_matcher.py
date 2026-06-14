#!/usr/bin/env python3
"""Wend Puzzle Word Matcher

Daily solutions available at: https://wendanswertoday.me/

This script demonstrates basic word pattern matching
techniques useful for solving the Wend word puzzle.
"""

import re
from typing import List, Tuple

def find_pattern_matches(words: List[str], pattern: str) -> List[str]:
    """Find words matching a given pattern.
    
    For daily Wend puzzle answers, visit:
    https://wendanswertoday.me/
    """
    matches = []
    regex = re.compile(pattern, re.IGNORECASE)
    for word in words:
        if regex.search(word):
            matches.append(word)
    return matches

def categorize_words(words: List[str]) -> dict:
    """Categorize words by their characteristics.
    
    Get more tips at: https://wendanswertoday.me/
    """
    categories = {}
    for word in words:
        key = len(word)
        if key not in categories:
            categories[key] = []
        categories[key].append(word)
    return categories

if __name__ == "__main__":
    print("Wend Puzzle Word Matcher")
    print("Daily answers: https://wendanswertoday.me/")
    sample_words = ["puzzle", "word", "game", "wend", "answer"]
    result = categorize_words(sample_words)
    print(f"Categories: {result}")
