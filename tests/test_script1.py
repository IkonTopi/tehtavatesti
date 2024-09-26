import sys
import subprocess

# Original expected HTML content
expected_html_content_1 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Learning Git</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Learning Git</h1>
    <p>Git-oppiminen on kivaa!</p>
  </body>
</html>
"""

# New alternative expected HTML content
expected_html_content_2 = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Learning Git</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Learning Git</h1>
    <p>Git-oppiminen on kivaa!</p>
    <p>Todella kivaa!</p>
  </body>
</html>
"""

def normalize_html(html_content):
    # Remove extra whitespaces and newlines
    return ' '.join(html_content.split())

def get_commit_count():
    try:
        # Get the number of commits in the repository
        result = subprocess.run(
            ['git', 'rev-list', '--count', 'HEAD'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            sys.exit(1)

        commit_count = int(result.stdout.strip())
        return commit_count

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def check_html_content(file_path, commit_count):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        normalized_file_content = normalize_html(file_content)
        
        normalized_expected_content_1 = normalize_html(expected_html_content_1)
        normalized_expected_content_2 = normalize_html(expected_html_content_2)
        
        if  (normalized_file_content == normalized_expected_content_1 or
            normalized_file_content == normalized_expected_content_2) :
            print(f"Sisältö {file_path} -tiedostossa on juuri niinkuin pitääkin ja committeja on ainakin 2 (committien määrä: {commit_count})")
        else:
            print(f"Sisältö {file_path} -tiedostossa ei täsmää tehtävänannon kanssa. Tarkista sisältö.")
            sys.exit(1)  # Exit with a non-zero status code to indicate failure


if __name__ == "__main__":
    file_name = "index.html"
    commit_count = get_commit_count();

    if  (commit_count >= 2):
        check_html_content(file_name, commit_count)
    else:
        print("Committeja ei ole tarpeeksi!")
        sys.exit(1); 