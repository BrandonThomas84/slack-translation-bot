# Slack Translation Bot

You will need to add a Google API key that has Google Cloud Translation API enabled. Additionally you will need to create a Slack App and add a bot user to it. You will need the bot token for the Slack App.

It may also be a good idea to setup an Ngrok account that can be used to test against your local development environment.

## Environment Variables

| Variable | Description |
| --- | --- |
| SLACK_BOT_TOKEN | your-slack-bot-token |
| GOOGLE_API_KEY | your-google-api-key |

## Development

The first time you setup the application the order of operations is a bit out of whack. First you will need to setup your Slack app and bot user so that you can get the bot key necessary for the environment. Secondly you will need to setup an API key for the Google Cloud Translation API. Once you have both of these keys you can add them to the environment variables in the `.env` file and run the application after running the setup command.

You can then run the `expose ngrok` command to give you a URL that can be added to the Manifest file for the Slack App (change `https://your-server-url/` to the ngrok URL). This will allow you to test the application in a live environment.

### Setup

Run the following command to setup your application. This will install all the dependencies.

```bash
Make setup
```

### Run

Run the following command to run your application.

```bash
Make run
```

### Expose Locally

To expose your local development environment to the internet you can use Ngrok. Run the following command to expose your local development environment.

```bash
Make expose-ngrok
```
