import os
def list_directory_contents(path):
    try:
        contents = os.listdir(path)
        print(f"Contents of {path}:")
        for item in contents:
            print(item)
    except FileNotFoundError: 
        print("Error: The directory {path} does not exist.")
    except PermissionError:
        print("Error: Permission denied to access {path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the path of the directory: ")
    list_directory_contents(directory_path)