import os
def create_file(filename):
    try:
        with open(filename,'w') as file:
            print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of '{filename}' :\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def write_to_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text + '\n')
            print(f"Text appended to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
while True:
    print("\nFile Management System Menu:")
    print("1. Create a new File with <filename>")
    print("2. Read a file")
    print("3. Write to a file")
    print("4. Exit")

    choice = input("Enter Operator (1/2/3/4): ")

    if choice == '1':
        filename = input("Enter a name for your new file: ")
        create_file(filename)
    elif choice == '2':
        filename = input("Enter the name of the file to read: ")
        read_file(filename)
    elif choice == '3':
        filename = input("Enter the name of the file to write to: ")
        text = input("Enter new text: ")
        write_to_file(filename, text)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose a valid option.")