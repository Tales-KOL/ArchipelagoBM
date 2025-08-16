@echo off
:: Batch script to compress "bm" folder into bm.zip, rename to bm.apworld, and copy to Archipelago folder

:: Check if bm folder exists
if not exist "bm" (
    echo Folder "bm" not found!
    pause
    exit /b
)

:: Compress bm folder to bm.zip using PowerShell
powershell -command "Compress-Archive -Path 'bm' -DestinationPath 'bm.zip' -Force"

:: Rename bm.zip to bm.apworld
if exist "bm.zip" (
    if exist "bm.apworld" del "bm.apworld"
    ren "bm.zip" "bm.apworld"
    echo Created bm.apworld
) else (
    echo Compression failed.
    pause
    exit /b
)

:: Copy to Archipelago custom_worlds directory
set DEST=D:\ProgramData\Archipelago\custom_worlds
if not exist "%DEST%" (
    echo Destination folder not found: %DEST%
    pause
    exit /b
)

copy /Y "bm.apworld" "%DEST%"
echo Copied bm.apworld to %DEST%

pause
