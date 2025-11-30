# Fix Windows WebDAV Mount Issue

## Current Status

✅ **Good News:** Your WebDAV server is working perfectly!
- Server starts successfully on port 9999
- Python 3.14 and wsgidav 4.3.3 installed correctly
- Port detection logic is working

❌ **Problem:** Windows Registry blocks HTTP WebDAV mounts

## What's Happening

When you try to mount:
```
net use Z: http://127.0.0.1:9999
```

You get:
```
System error 67 - The network name cannot be found.
```

**Root Cause:** Windows security policy restricts WebDAV over HTTP by default.

## Test Results

✅ Server running: `netstat` shows port 9999 LISTENING  
❌ Registry value: `BasicAuthLevel = 0x1` (currently set to 1)  
❌ Required value: `BasicAuthLevel = 0x2` (needs to be 2)

## The Fix

### Option 1: Run as Administrator (PowerShell)

**Open PowerShell as Administrator** and run:

```powershell
# Set registry value to allow HTTP WebDAV
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Services\WebClient\Parameters' -Name 'BasicAuthLevel' -Value 2

# Restart WebClient service
Restart-Service WebClient
```

### Option 2: Manual Registry Edit

1. Press `Win + R`, type `regedit`, press Enter
2. Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters`
3. Double-click `BasicAuthLevel`
4. Change value from `1` to `2`
5. Click OK
6. Restart WebClient service:
   - Press `Win + R`, type `services.msc`
   - Find "WebClient"
   - Right-click → Restart

## After Fixing Registry

Once the registry is fixed, the mount script should work:

```bash
bash mount_zo mount
```

Or mount manually:
```bash
net use Z: http://127.0.0.1:9999 /user:dummy dummy
```

## Verify It Works

```bash
# Check the mount
net use

# List files
dir Z:
```

## Why This Happens

Windows security policy considers HTTP (non-HTTPS) WebDAV connections insecure and blocks them by default. The `BasicAuthLevel` setting controls this:
- `0` = Basic authentication disabled  
- `1` = Basic authentication for HTTPS only (default)
- `2` = Basic authentication for HTTP and HTTPS

Since we're using `http://127.0.0.1` (localhost over HTTP), we need level 2.

## Security Note

This change allows HTTP WebDAV connections system-wide. Since we're only connecting to localhost (127.0.0.1), this is safe. The WebDAV server itself handles authentication via your Zo Computer access token.
