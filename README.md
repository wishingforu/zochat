 ________  ________          ________  ___  ___  ________  _________   
|\_____  \|\   __  \        |\   ____\|\  \|\  \|\   __  \|\___   ___\ 
 \|___/  /\ \  \|\  \       \ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_| 
     /  / /\ \  \\\  \       \ \  \    \ \   __  \ \   __  \   \ \  \  
    /  /_/__\ \  \\\  \       \ \  \____\ \  \ \  \ \  \ \  \   \ \  \ 
   |\________\ \_______\       \ \_______\ \__\ \__\ \__\ \__\   \ \__\
    \|_______|\|_______|        \|_______|\|__|\|__|\|__|\|__|    \|__| 
                                                                    v2.0

A powerful CLI for [Zo Computer](https://zo.computer) - Chat, Billing, Events, and Services.

## Installation

### Option 1: Quick Install (Git)
```bash
git clone https://github.com/wishingforu/zochat.git
cd zochat
chmod +x zochat
./zochat
```

### Option 2: Manual Install (Single Script)
Download the script directly and run it:

```bash
# Download
curl -o zochat https://raw.githubusercontent.com/wishingforu/zochat/main/zochat

# Make executable
chmod +x zochat

# Run
./zochat
```

### Optional: Add to PATH
To run it from anywhere by just typing `zochat`:

```bash
mkdir -p ~/.local/bin
mv zochat ~/.local/bin/
# Ensure ~/.local/bin is in your PATH
```

## Requirements
- **Bash** 4.0+
- **curl** (for API requests)
- **jq** (for JSON parsing & charts)
- **Unix-like OS** (Linux, macOS, WSL)

## Features
- ** All ZO AI services**: GPT-5.1, Claude 3.5, Grok, Gemini, and more
- **Billing Dashboard**: View credits, invoices, and ASCII usage charts
- **Event Scheduler**: Manage recurring tasks and reminders
- **User Services**: Deploy and monitor your services (HTTP/TCP)
- ** Advanced Config**: Reasoning levels, token budgets, and verbosity control

## First-Time Setup
When you first run `./zochat`, you'll be prompted for:

1. **Access Token**: 
   - Press `F12` on zo.computer
   - Go to **Application** > **Cookies** > **.zo.computer**
   - Copy the value of `access_token`
2. **Domain**: 
   - Your subdomain (e.g., `daniel` if your URL is `daniel.zo.computer`)

## Usage
The main menu gives you quick access to all features:

```
  [1] Chat with AI      - Start a conversation
  [2] View Events       - List scheduled tasks
  [3] Schedule Event    - Create new task
  [4] View Billing      - Credits and usage
  [5] User Services     - Manage services
  [6] Exit              - Close application
```
