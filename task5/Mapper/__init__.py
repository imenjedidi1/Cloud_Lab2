import azure.functions as func

def main(mapperinput: tuple):
    """
    Mapper function to process a line of text.
    :param input_data: A tuple (line_number, line_content).
    """
    line_number, line_content = mapperinput

    if not isinstance(line_content, str):
        raise ValueError(f"Expected a string for line_content but got {type(line_content)}")

    # Split line into words and return word-count pairs
    words = line_content.split()
    return [(word, 1) for word in words]
