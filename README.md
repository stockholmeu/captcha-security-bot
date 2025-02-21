# Telegram Captcha Bot

This is a Telegram bot built using the Aiogram library. It is designed to verify users by presenting them with a simple captcha challenge before granting access to a private channel.

## Features

- **User Verification**: Uses a simple math captcha to verify users are not bots.
- **Invite Links**: Generates invite links for verified users to join a private channel.
- **Secure Access**: Ensures that only verified users can access the channel.

## Getting Started

### Prerequisites

- Python 3.7+
- A Telegram bot token from [BotFather](https://t.me/botfather)
- Aiogram library

### Installation

1. **Clone the repository**:
```bash
   git clone https://github.com/yourusername/telegram-captcha-bot.git
   cd telegram-captcha-bot

   pip install aiogram, asyncio, aiohttp
