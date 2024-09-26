import sys

# Updated expected HTML content for index.html
expected_html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Learning Git</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Learning Git</h1>
    <h2>Excellent Git training!</h2>
  </body>
</html>
"""

# Expected CSS content for style.css
expected_css_content = """
body {
  background-color: #aaa;
}
h2 {
  background-color: red;
  color: white;
}
"""

def normalize_content(content):
    """Remove extra whitespaces and newlines."""
    return ' '.join(content.split())

def check_file_content(file_path, expected_content):
    """Check if the file content matches the expected content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            normalized_file_content = normalize_content(file_content)
            normalized_expected_content = normalize_content(expected_content)
            
            if normalized_file_content == normalized_expected_content:
                print(f"The content in {file_path} matches the expected content.")
            else:
                print(f"The content in {file_path} does not match the expected content.")
                sys.exit(1)  # Exit with a non-zero status code to indicate failure
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        sys.exit(1)

if __name__ == "__main__":
    # Check index.html
    check_file_content("index.html", expected_html_content)

    # Check style.css
    check_file_content("style.css", expected_css_content)