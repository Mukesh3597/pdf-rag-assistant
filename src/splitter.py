import re


def split_text(text):
    lines = text.splitlines()

    chunks = []
    current_chunk = []

    expected_question = 1

    for line in lines:
        line = line.strip()

        if not line:
            continue

        match = re.match(r"^(\d+)\.\s+", line)

        if match:
            number = int(match.group(1))

            if number == expected_question:
                if current_chunk:
                    chunks.append("\n".join(current_chunk).strip())

                current_chunk = [line]
                expected_question += 1
                continue

        current_chunk.append(line)

    if current_chunk:
        chunks.append("\n".join(current_chunk).strip())

    # PDF ka title remove karo
    chunks = [
        chunk for chunk in chunks
        if re.match(r"^1\.\s+", chunk)
        or re.match(r"^\d+\.\s+", chunk)
    ]

    return chunks