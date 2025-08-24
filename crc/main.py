import argparse
from crc.input_parser import parse_input_file
from crc.optimizer import optimize_cutting

def main():
    """
    Main function to run the aluminum cutting optimizer.
    """
    parser = argparse.ArgumentParser(description='Aluminum Cutting Optimizer')
    parser.add_argument('input_file', help='Path to the input JSON file')
    parser.add_argument('--minimal-waste', type=int, default=50, help='Minimal waste per bar')
    parser.add_argument('--blade-width', type=int, default=5, help='Width of the cutting blade')
    args = parser.parse_args()

    # Parse the input file
    pieces_to_cut, bar_lengths = parse_input_file(args.input_file)

    if not pieces_to_cut:
        print("No pieces to cut.")
        return

    if not bar_lengths:
        print("No bar lengths specified.")
        return

    # For simplicity, we'll use the first available bar length for now.
    bar_length = bar_lengths[0]
    print(f"Using bar length: {bar_length}")
    print(f"Using minimal waste: {args.minimal_waste}")
    print(f"Using blade width: {args.blade_width}")

    # Run the optimizer
    cutting_plan = optimize_cutting(
        pieces_to_cut,
        bar_length,
        blade_width=args.blade_width,
        min_waste=args.minimal_waste
    )

    # Print the results
    print("\n--- Cutting Plan ---")
    total_waste = 0
    total_used_length = 0
    for i, bar in enumerate(cutting_plan):
        bar_pieces_str = ", ".join([f"{p['id']}({p['length']})" for p in bar])
        bar_used_length = sum(p['length'] for p in bar) + (len(bar) - 1) * args.blade_width
        waste = bar_length - bar_used_length
        total_waste += waste
        total_used_length += bar_used_length
        print(f"Bar {i+1}: [{bar_pieces_str}] | Used: {bar_used_length} | Waste: {waste}")

    print(f"\nTotal bars used: {len(cutting_plan)}")
    print(f"Total waste: {total_waste}")
    if len(cutting_plan) > 0:
        overall_efficiency = 100 * total_used_length / (len(cutting_plan) * bar_length)
        print(f"Overall efficiency: {overall_efficiency:.2f}%")


if __name__ == '__main__':
    main()
