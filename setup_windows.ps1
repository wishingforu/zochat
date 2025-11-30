# Windows WebDAV Setup Script for Zo Computer
# Run this as Administrator

Write-Host "Setting up Windows WebDAV for Zo Computer..." -ForegroundColor Cyan

# 1. Trust the Self-Signed Certificate
$certPath = "$env:USERPROFILE\.config\zo-chat\zoMount.crt"
if (Test-Path $certPath) {
    Write-Host "[*] Trusting SSL Certificate..."
    try {
        Import-Certificate -FilePath $certPath -CertStoreLocation "Cert:\LocalMachine\Root" | Out-Null
        Write-Host "    Success!" -ForegroundColor Green
    } catch {
        Write-Host "    Failed to import certificate. Run as Administrator!" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "[!] Certificate not found at $certPath" -ForegroundColor Yellow
    Write-Host "    Run 'zochat' first to generate it."
    exit 1
}

# 2. Configure WebClient Registry
Write-Host "[*] Configuring WebClient Registry..."
$regPath = "HKLM:\SYSTEM\CurrentControlSet\Services\WebClient\Parameters"

try {
    # Enable Basic Auth (Level 2)
    Set-ItemProperty -Path $regPath -Name "BasicAuthLevel" -Value 2 -Type DWord -Force
    
    # Allow sending credentials to localhost (CRITICAL FIX)
    $hosts = @("https://localhost", "https://127.0.0.1")
    New-ItemProperty -Path $regPath -Name "AuthForwardServerList" -PropertyType MultiString -Value $hosts -Force -ErrorAction SilentlyContinue | Out-Null
    Set-ItemProperty -Path $regPath -Name "AuthForwardServerList" -Value $hosts -Force
    
    # Increase file size limit (optional but good)
    Set-ItemProperty -Path $regPath -Name "FileSizeLimitInBytes" -Value 0xffffffff -Type DWord -Force
    
    Write-Host "    Registry configured!" -ForegroundColor Green
} catch {
    Write-Host "    Failed to write registry. Run as Administrator!" -ForegroundColor Red
    exit 1
}

# 3. Restart WebClient Service
Write-Host "[*] Restarting WebClient Service..."
try {
    Set-Service -Name WebClient -StartupType Automatic
    Restart-Service WebClient -Force
    Write-Host "    Service restarted!" -ForegroundColor Green
} catch {
    Write-Host "    Failed to restart service." -ForegroundColor Red
}

Write-Host "`nSetup Complete! You can now mount using 'zochat'." -ForegroundColor Green
Read-Host "Press Enter to exit"
