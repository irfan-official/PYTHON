import os
import pandas as pd

def list_images_to_excel(folder_path, output_excel):
    # Get list of image files
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}
    image_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in image_extensions]
    
    # Prepare data for Excel
    data = [[i+1, file] for i, file in enumerate(image_files)]
    df = pd.DataFrame(data, columns=["S.No", "Image File"])
    
    # Save to Excel
    df.to_excel(output_excel, index=False, engine='openpyxl')
    print(f"Excel file '{output_excel}' created successfully!")

# Example usage
folder_path = "path/to/your/images"  # Replace with the actual path
output_excel = "image_list.xlsx"
list_images_to_excel(folder_path, output_excel)
