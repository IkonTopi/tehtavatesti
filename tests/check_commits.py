import sys
import subprocess

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

def main():
    commit_count = get_commit_count()

    if commit_count >= 3:
        print(f"Success: The repository has {commit_count} commits.")
    else:
        print(f"Failure: The repository has only {commit_count} commits. At least 3 commits are required.")
        sys.exit(1)

if __name__ == "__main__":
    main()
