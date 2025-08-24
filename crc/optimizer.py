def optimize_cutting(pieces, bar_length, blade_width=5, min_waste=50):
    """
    Optimizes the cutting of pieces from stock bars using the first-fit decreasing algorithm.

    Args:
        pieces (list): A list of piece objects to be cut. Each object is a dict
                       with 'id' and 'length'.
        bar_length (int): The length of the stock bars.
        blade_width (int): The width of the cutting blade.
        min_waste (int): The minimum allowable waste length.

    Returns:
        list: A list of lists, where each inner list represents a bar and contains the
              piece objects cut from that bar.
    """
    # Sort pieces in descending order of length
    pieces.sort(key=lambda p: p['length'], reverse=True)

    bars = []
    for piece in pieces:
        placed = False
        # Try to place the piece in an existing bar
        for bar in bars:
            # Calculate the total length of pieces in the bar, including blade width for each cut
            current_bar_length = sum(p['length'] for p in bar) + len(bar) * blade_width
            potential_waste = bar_length - (current_bar_length + piece['length'])
            if current_bar_length + piece['length'] <= bar_length and (potential_waste == 0 or potential_waste >= min_waste):
                bar.append(piece)
                placed = True
                break

        # If the piece could not be placed in any existing bar, start a new bar
        if not placed:
            bars.append([piece])

    return bars
