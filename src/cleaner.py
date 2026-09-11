import re


def clean_text(text):
    # Extra spaces remove
    text = re.sub(r"[ \t]+", " ", text)

    # Extra blank lines remove
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Starting and ending spaces remove
    text = text.strip()

    return text