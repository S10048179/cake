@echo off
cd "%USERPROFILE%/Documents/cake"
powershell "Import-Module BitsTransfer; Start-BitsTransfer 'https://raw.githubusercontent.com/S10048179/cake/master/cake.bat' 'cake.bat'; Start-BitsTransfer 'https://raw.githubusercontent.com/S10048179/cake/master/portal-radio.mp3' 'portal-radio.mp3'"
cake.bat
sleep 3
exit
