```text
 ________  ________          ________  ___  ___  ________  _________   
|\_____  \|\   __  \        |\   ____\|\  \|\  \|\   __  \|\___   ___\ 
 \|___/  /\ \  \|\  \       \ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_| 
     /  / /\ \  \\\  \       \ \  \    \ \   __  \ \   __  \   \ \  \  
    /  /_/__\ \  \\\  \       \ \  \____\ \  \ \  \ \  \ \  \   \ \  \ 
   |\________\ \_______\       \ \_______\ \__\ \__\ \__\ \__\   \ \__\
    \|_______|\|_______|        \|_______|\|__|\|__|\|__|\|__|    \|__| 
                                                                    v1.0
```

The most ultimate best fucking CLI for [Zo Computer](https://zo.computer) 


## Installation
*You don't need to be SSH'd into your Zo Chat for this to work*

### Requirements
- **Bash** 4.0+
- **curl** (for API requests)
- **jq** (for JSON parsing & charts)
- **Unix-like OS** (Linux, macOS, WSL)


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
     
------------------------------or-----------------------------------
   - Go to your Zo Computer
   - Go to **Settings** > **Developer** > **Edit ZO_CLIENT_IDENTITY_TOKEN**
   - Copy and Paste the `access_token/ ZO_CLIENT_IDENTITY_TOKEN`

   
2. **Domain**: 
   - Your subdomain (e.g., `johnappleseed` if your URL is `johnappleseed.zo.computer`)

## Usage
The main menu gives you quick access to all features:

```
  [1] AI Models         - Start a conversation
  [2] Chats             - History and logs
  [3] Events            - View and schedule tasks
  [4] Services          - Manage services
  [5] Billing           - Credits and usage
  [6] System            - View machine stats
  [7] Exit              - Close application
```
