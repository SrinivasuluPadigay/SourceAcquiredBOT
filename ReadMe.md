# SourceAcquiredBOT

This Python script, `SourceAcquiredBOT.py`, is designed to operate as a Reddit bot within the "SauceSharingCommunity" subreddit. The primary functionality of the bot is to monitor comments in the subreddit, searching for approved hyperlinks or a specific keyword ("!solved"). If such elements are found, the bot automatically updates the post flair to indicate that the source has been acquired.

## Features

- Monitors comments in the specified subreddit for relevant hyperlinks and keywords.
- Automatically updates the post flair to "Source acquired" when criteria are met.
- Utilizes the PRAW (Python Reddit API Wrapper) library for Reddit interaction.

## Prerequisites

Before running the script, ensure that you have the following prerequisites:

- [Python](https://www.python.org/downloads/) installed (script is compatible with Python 3.x).
- PRAW library installed. You can install it using:

  ```bash
  pip install praw
  ```

## Usage

1. Replace the placeholder values in the script with your Reddit bot's credentials:

   - `user_agent`: User-agent for the Reddit bot.
   - `client_id`: Reddit API client ID.
   - `client_secret`: Reddit API client secret.
   - `username`: Reddit bot username.
   - `password`: Reddit bot password.

2. Set the target subreddit by updating the `subreddit` variable:

   ```python
   subreddit = reddit.subreddit('SauceSharingCommunity')
   ```

3. Customize the bot's behavior by modifying the following variables:

   - `saucereqflair`: Flair template ID for the "Source requested" flair.
   - `sauceacqflair`: Flair template ID for the "Source acquired" flair.
   - `keyphrase`: Keyword triggering the bot to mark a post as "Source acquired."
   - `reprocess_keyphrase`: Keyword triggering the bot to reprocess a submission.
   - `sources`: List of approved hyperlink sources.
   - `userBlacklist`: List of users to be excluded from processing.
   - `urlBlacklist`: List of blacklisted URLs.

4. Run the script:

   ```bash
   python SourceAcquiredBOT.py
   ```

The script will continuously monitor comments in the specified subreddit, updating post flairs when appropriate criteria are met.

## Notes

- The script uses exception handling to manage potential errors during execution. If an issue arises, the traceback information will be printed.
- Ensure that the bot account has the necessary permissions to modify post flairs and access the specified subreddit.