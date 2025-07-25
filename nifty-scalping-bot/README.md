
# NIFTY Scalping Bot (Render Deployment)

## Setup Instructions

1. Copy `.env.example` to `.env` and fill in your Telegram bot token and chat ID.
2. Deploy this project on Render with the following:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Root Directory:** leave blank

## Test

To test the Telegram webhook:

```bash
curl -X POST https://your-render-url/webhook -H "Content-Type: application/json" -d '{"message":"🚀 Test Alert from Render"}'
```
