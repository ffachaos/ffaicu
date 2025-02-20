@echo off
REM 使用法チェック: 新しいシバンのパスが引数として必要
if "%~1"=="" (
    echo Usage: %~nx0 ^<new_shebang_path^>
    exit /b 1
)

REM 変数の設定
set "NEW_SHEBANG=#!%~1"
set "TARGET_DIR=ffaicu"
set "OLD_SHEBANG=#!/usr/local/bin/perl --"

REM 対象フォルダ内のすべてのファイルを再帰的に処理
for /R "%TARGET_DIR%" %%F in (*) do (
    powershell -NoProfile -Command "$file = '%%F'; $lines = Get-Content -Path $file -Raw -Encoding UTF8; if($lines -match '^%OLD_SHEBANG%'){ $lines = $lines -replace '^%OLD_SHEBANG%', '%NEW_SHEBANG%'; [System.Text.Encoding]::UTF8.GetBytes($lines) | Set-Content -Path $file -Encoding Byte -NoNewline; Write-Host 'Updating shebang in: %%F' }"
)

echo Shebang update complete.
