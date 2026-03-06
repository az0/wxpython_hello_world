"""Random word generation for tree items."""

import random

ADJECTIVES = [
    "Red", "Blue", "Green", "Fast", "Slow", "Big", "Small", "Bright",
    "Dark", "Happy", "Sad", "Lucky", "Wild", "Calm", "Bold",
]
NOUNS = [
    "Fox", "Tree", "River", "Mountain", "Cloud", "Star", "Moon",
    "Eagle", "Wolf", "Bear", "Stone", "Flame", "Wind", "Wave", "Leaf",
]


def random_label():
    """Return a random two-word label."""
    return "{} {}".format(random.choice(ADJECTIVES), random.choice(NOUNS))
