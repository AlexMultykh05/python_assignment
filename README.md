# Python Task

This project contains a Python-based task with the following structure:

## Files

- **`main.py`**: The main Python code. It contains the logic for executing the task.
- **`config.ini`**: A configuration file used to store keys and tokens necessary for the task.

## Task Description

This small Python project connects to the Twitter API using Tweepy and OAuth 2.0 to authenticate a user and fetch their recent tweets and retweets. The script reads credentials from a `config.ini` file, authenticates the user, retrieves their Twitter handle and user ID, and prints a list of their latest tweets to the console. The goal is to demonstrate basic access to personal Twitter data via the Twitter API v2.


## What I got

For the given piece of code I got a list of my tweets and times I posted them:

```alexmultykh@MacBook-Air-Alex Desktop % python3 python_task/main.py
Authenticated as @alexmultykh2005 (ID: 1346476645994041344)

Your latest tweets/retweets:
- 2024-10-14 15:43:52+00:00: RT @InfoFortniteUA: 🎁 Розігруємо три скіна чарівної відьмочки «Lexa Hexbringer» 🧙🏻‍♀️

Умови розіграшу дуже прості:
• Підпишіться на @InfoF…
- 2024-10-10 17:36:46+00:00: RT @InfoFortniteUA: 🎁 Розігруємо три скіна чарівної відьмочки «Harbinger Lexa» 🧙🏻‍♀️

Умови розіграшу дуже прості:
• Підпишіться на @InfoFo…
- 2024-01-02 09:01:36+00:00: RT @igorlachenkov: Kyiv now https://t.co/L7SsLp1Nsu
- 2023-10-11 12:06:19+00:00: #RealestPersonOnEarth https://t.co/BLjulFdkbj```


I only have 3 tweets, as I do not use Twitter on daily basis. Fortunately, I obtained the desired result