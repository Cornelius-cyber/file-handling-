def modify_file_content(content):
    """Function to modify the file content."""
    return content.upper()


def main():
    import os

    try:
        input_filename = input("Enter the name of the file to read: ")

        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")

        with open(input_filename, "r") as file:
            content = file.read()

        modified_content = modify_file_content(content)

        output_filename = input("Enter the name of the file to write the modified content: ")

        with open(output_filename, "w") as file:
            file.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: You don't have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
