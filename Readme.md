# GitHub User CLI

A simple Python command-line tool that uses the GitHub REST API to fetch and display public information about a GitHub user.

## Features

* Search for a GitHub user by username
* Fetch user data using the GitHub API
* Display username, name, bio, followers, following, and public repositories
* Handle API and network errors
* Use a GitHub token securely with `.env`

## Tech Stack

* Python
* Requests
* GitHub REST API
* python-dotenv

## Installation

```bash
git clone <your-repository-url>
cd github-user-cli
pip install -r requirements.txt
```

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
```

## Usage

```bash
python github_cli.py octocat
```

The tool will fetch the user's information and display it in the terminal.

## What I Learned

* How APIs work
* HTTP GET requests
* JSON parsing
* API authentication
* Error handling
* Command-line arguments
* Environment variables and `.env`
