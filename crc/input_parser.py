import json

def parse_input_file(file_path):
    """
    Parses the input JSON file and returns the pieces and bar lengths.

    The input JSON file should have the following format:
    {
      "pieces": [
        {"id": "P1", "length": 250, "quantity": 10},
        ...
      ],
      "bar_lengths": [1000, 6000]
    }

    Returns:
        tuple: A tuple containing:
            - list: A list of all piece objects, where each object is a dict
                    with 'id' and 'length'.
            - list: A list of available bar lengths.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    pieces_to_cut = []
    for piece_data in data.get('pieces', []):
        piece_id = piece_data.get('id')
        length = piece_data.get('length')
        quantity = piece_data.get('quantity')
        if piece_id is not None and length is not None and quantity is not None:
            for _ in range(quantity):
                pieces_to_cut.append({'id': piece_id, 'length': length})

    bar_lengths = data.get('bar_lengths', [])

    return pieces_to_cut, bar_lengths
