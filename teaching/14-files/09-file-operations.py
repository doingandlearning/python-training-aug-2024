import os

def find_largest_text_file(directory):
    largest_file = None
    largest_size = 0
    
    # List all files in the directory
    for file_name in os.listdir(directory):
        # Check if it is a text file
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory, file_name)
            file_size = os.path.getsize(file_path)
            
            # Check if this file is the largest one we've found
            if file_size > largest_size:
                largest_size = file_size
                largest_file = file_path
    
    return largest_file, largest_size

def open_largest_text_file(directory):
    largest_file, largest_size = find_largest_text_file(directory)
    
    if largest_file:
        with open(largest_file, 'r') as file:
            content = file.read()
            print(f"Opened file: {largest_file} (Size: {largest_size} bytes)")
            return content
    else:
        print("No text files found in the directory.")
        return None

# Specify the directory to search
directory_path = '.'  # Replace with your directory path

# Open and read the largest text file
file_content = open_largest_text_file(directory_path)

# If you want to do something with the content, you can process it here
if file_content:
    print(file_content[:500])  # Print the first 500 characters as a preview
