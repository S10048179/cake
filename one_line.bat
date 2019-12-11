@echo off
cd "%USERPROFILE%/Documents"
mkdir "cake"
curl https://raw.githubusercontent.com/S10048179/cake/master/cake.bat --output cake.bat
curl https://raw.githubusercontent.com/S10048179/cake/master/portal-radio.wav --output portal-radio.mp3
cake.bat
