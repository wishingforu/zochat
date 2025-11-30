```text
 ________  ________          ________  ___  ___  ________  _________   
|\_____  \|\   __  \        |\   ____\|\  \|\  \|\   __  \|\___   ___\ 
 \|___/  /\ \  \|\  \       \ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_| 
     /  / /\ \  \\\  \       \ \  \    \ \   __  \ \   __  \   \ \  \  
    /  /_/__\ \  \\\  \       \ \  \____\ \  \ \  \ \  \ \  \   \ \  \ 
   |\________\ \_______\       \ \_______\ \__\ \__\ \__\ \__\   \ \__\
    \|_______|\|_______|        \|_______|\|__|\|__|\|__|\|__|    \|__| 			v1. 
```
> A [https://zo.computer](https://zo.computer) CLI
## Installation
### Quick Install (Recommended)
```bash
curl -fsSL https://raw.githubusercontent.com/wishingforu/zo-chat-cli/main/install.sh | bash
```
### Install with Git
```bash
git clone https://github.com/wishingforu/zo-chat-cli.git
cd zo-chat-cli
chmod +x install.sh
./install.sh
```
### Manual Install
1. **Download the script**
   ```bash
   curl -O https://raw.githubusercontent.com/wishingforu/zo-chat-cli/main/zo-chat
   ```
2. **Make it executable**
   ```bash
   chmod +x zo-chat
   ```
3. **Move to your PATH**
   ```bash
   mv zo-chat ~/.local/bin/chat
   ```
   *Or run directly:*
   ```bash
   ./zo-chat
   ```
## Requirements
- **Bash** 4.0 or higher
- **curl** - For API requests
- **jq** - For JSON parsing
- **Unix-based OS** (Linux, macOS, WSL on Windows)
## Quick Start
Run the tool:
```bash
chat
```
### First-time setup
You'll be prompted for:
1. **Access Token** - Get from Zo Computer:
   - Press `F12` in your browser
   - Go to `Application` > `Cookies` > `.zo.computer`
   - Copy the `access_token` value
2. **Domain** - Your Zo subdomain (e.g., enter `yourname` if your URL is `yourname.zo.computer`).
