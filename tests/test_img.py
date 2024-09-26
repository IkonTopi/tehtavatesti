import sys

def normalize_content(content):
    # Remove extra whitespaces and newlines
    return ' '.join(content.split())

def check_readme(file_path):
    with open(file_path) as file:
        
        if (file):
            print(f"{file_path} -tiedosto löytyi!")
        else:
            print(f"{file_path} -tiedostoa  ei löytynyt.")
            sys.exit(1)  # Exit with a non-zero status code to indicate failure

if __name__ == "__main__":
    file_name = "img/gitRemoteRemoval.png"
    check_readme(file_name)