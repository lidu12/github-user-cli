import os
import sys

import requests
from dotenv import load_dotenv


def get_github_user(username, token):
    """Fetch GitHub user information from the API."""
    url = f"https://api.github.com/users/{username}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 404:
            print(f"Error: GitHub user '{username}' was not found.")
            return None

        if response.status_code == 401:
            print("Error: Authentication failed. Check your GitHub token.")
            return None

        if response.status_code == 403:
            print("Error: Access forbidden or API rate limit exceeded.")
            return None

        print(f"Error: GitHub API returned status code {response.status_code}.")
        return None

    except requests.exceptions.RequestException:
        print("Error: Could not connect to GitHub. Check your internet connection.")
        return None


def display_user(data):
    """Display GitHub user information in a readable format."""
    bio = data.get("bio") or "No bio available"

    print()
    print("=" * 50)
    print("              GITHUB USER INFO")
    print("=" * 50)
    print()
    print(f"Username:             {data['login']}")
    print(f"Name:                 {data.get('name') or 'No name available'}")
    print(f"Bio:                  {bio}")
    print(f"Followers:            {data['followers']}")
    print(f"Following:            {data['following']}")
    print(f"Public repositories:  {data['public_repos']}")
    print(f"Profile:              {data['html_url']}")
    print()
    print("=" * 50)


def main():
    """Run the GitHub CLI application."""
    load_dotenv()

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("Error: GITHUB_TOKEN was not found.")
        print("Make sure your token is stored in the .env file.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python github_cli.py <username>")
        sys.exit(1)

    username = sys.argv[1].strip()

    if not username:
        print("Error: Username cannot be empty.")
        sys.exit(1)

    data = get_github_user(username, token)

    if data:
        display_user(data)


if __name__ == "__main__":
    main()