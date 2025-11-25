import sys
import os
import fitz  # PyMuPDF


def compress_pdf(input_path, output_folder="compressed_output"):
    """
    Compresses a single PDF file and saves it to the output folder.
    """

    # 1. Validation: check the input file exists
    if not os.path.exists(input_path):
        print(f"Error: The file '{input_path}' was not found.")
        return

    # 2. Setup: create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # 3. Naming: build the output filename
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}_compressed{ext}"
    output_path = os.path.join(output_folder, output_filename)

    # 4. Try/Processing start
    try:
        print(f"Processing '{filename}'...")

        # Open PDF
        doc = fitz.open(input_path)

        # 5. Optimization: Save with compression
        doc.save(
            output_path,
            garbage=4,     # remove unused objects
            deflate=True,  # compress streams
            clean=True     # clean and optimize PDF objects
        )
        doc.close()

        # 6. Stats: calculate sizes
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)

        # 7. Compute and print compression result
        ratio = (1 - (compressed_size / original_size)) * 100

        print(f"Done! Saved to: {output_path}")
        print(f"Original:   {original_size / 1024:.2f} KB")
        print(f"Compressed: {compressed_size / 1024:.2f} KB")
        print(f"Reduction:  {ratio:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


# 9. Command-line execution block
if __name__ == "__main__":

    # 10. Check if the user passed a PDF file as argument
    if len(sys.argv) < 2:
        print("Usage: compresspdf.py <pdf_file_path>")
    else:
        # 11. Run compression with the given file path
        input_file = sys.argv[1]
        compress_pdf(input_file)

