import argparse

def main():
    parser = argparse.ArgumentParser(description="File Converter")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("output_format", choices=["json", "yaml", "xml"], help="Output format")
    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()
