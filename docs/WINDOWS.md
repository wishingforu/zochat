# Windows Installation Guide

## One-Click Setup

1. **Clone or download** this repository
2. **Double-click** `windows-setup.bat`
3. **Done!** A desktop shortcut will be created

## Manual Setup (if needed)

### Prerequisites
- **Git Bash** (comes with Git): https://git-scm.com/download/win
- **Python 3.12+**: https://www.python.org/downloads/

### Install
```bash
# Clone the repo
git clone https://github.com/wishingforu/zochat.git
cd zochat

# Run setup
windows-setup.bat
```

### Run
- Double-click the **ZoChat** desktop shortcut
- OR run `zochat.bat` from the folder

## First Time Setup

When you first run ZoChat, you'll need:

1. **Access Token**:
   - **Method 1**: Browser → F12 → Application → Cookies → `.zo.computer` → Copy `access_token`
   - **Method 2**: Zo Computer → Settings → Developer → Copy `ZO_CLIENT_IDENTITY_TOKEN`

2. **Domain**: Your subdomain (e.g., `daniel` if your URL is `daniel.zo.computer`)

## Features

- **[1] AI Models** - Chat with AI
- **[2] Chats** - View conversation history  
- **[3] Files** - Browse workspace files
- **[4] Events** - Scheduled tasks
- **[5] Services** - Manage services
- **[6] Billing** - Usage and credits
- **[7] System** - Server stats
- **[8] Mount** - Mount workspace as drive (requires Python)
- **[9] Exit**

## Troubleshooting

### "Git not found"
Install Git from: https://git-scm.com/download/win

### "Python not found"  
Install Python from: https://www.python.org/downloads/
Make sure to check "Add Python to PATH" during installation!

### Mount feature not working
The mount feature is advanced and may not work on all Windows systems. Use the **Files** browser instead (`[3]` in menu).

## Updates

```bash
cd zochat
git pull
```

Or just delete and re-clone for a fresh start!
