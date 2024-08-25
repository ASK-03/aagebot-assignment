# AageBot Assignment

Submission By - [Abhishek Singh Kushwaha](https://github.com/ASK-03)

### Live Links

- Telegram Bot Link: https://web.telegram.org/a/#7535287425

- Telegram Bot Id: [aagebot_assignment_bot](https://web.telegram.org/a/#7535287425)

- Webserver Link: https://aagebot-assignment.onrender.com/

(This bot and web server are deployed using the **Free Tier** from Render. The server may go into a sleep mode when inactive for an long period. There may be a slight delay when accessing the bot or server for the first time after a period of inactivity. Once the server is active, subsequent requests should be processed without significant delay.)

## Dependencies

- **Python3**: Ensure that you have Python 3 installed on your system. You can download and install Python 3 from the official Python website: https://www.python.org.
- **pip**: pip is the package installer for Python. It is usually installed by default when you install Python. However, make sure you have pip installed and it is up to date. You can check the version of pip by running the following command:
  ```
  pip --version
  ```

## Installation

To install and use Telegram bot, follow the steps given below:

- Clone the forked repository to your local machine:
  ```
  git clone https://github.com/ASK-03/aagebot-assignment
  ```
- Navigate to the project directory:
  ```
  cd aagebot-assignment
  ```
- Install the necessary Python packages by running the following command:
  ```
  pip install -r requirements.txt
  ```
  (NOTE: It is recommended to install these requirements in a new python environment, you can use [venv](https://docs.python.org/3/library/venv.html))

## How to use?

Follow the steps given below:

- After installing requirements using the `requirements.txt` file. Create a new file named `.env` which will contain the `BOT_TOKEN` which can be generated using [`@BotFather`](https://web.telegram.org/a/#93372553). Example can be seen in `example.env` file. (Make sure to name the file as `.env`)

- When running on local server, use `SERVER_URL` variable as `http://localhost:5000`

## Purpose

This repository is created as a submission for intern assignment at [`AageBot`](https://aagebot.com/).

## Author

[Abhishek Singh Kushwaha](https://github.com/ASK-03)
