from PIL import Image

def rescale_png(input_path, output_path, target_size):
    """
    Rescales a PNG file to the desired size.

    Parameters:
    - input_path: Path to the input PNG file.
    - output_path: Path to save the rescaled PNG file.
    - target_size: Tuple (width, height) representing the desired size.

    Example:
    rescale_png("input.png", "output.png", (300, 200))
    """
    try:
        # Open the original image
        original_image = Image.open(input_path)

        # Rescale the image to the target size
        resized_image = original_image.resize(target_size)

        # Save the rescaled image
        resized_image.save(output_path)

        print(f"Rescaling successful. Saved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_file_path = r"C:\Users\zhiji\Documents\company\CompanyI\Images\Invoice_000000000664731.jpg"
output_file_path = r"C:\Users\zhiji\Documents\company\CompanyI\Images\output.jpg"
target_size = (1700//2, 2200//2)

rescale_png(input_file_path, output_file_path, target_size)
