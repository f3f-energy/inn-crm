@echo off
title INN Deploy

set PASTA_INN=C:\Users\ferna\F3F-Core\inn
set TOKEN=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
set GITHUB_RAW=https://raw.githubusercontent.com/f3f-energy/inn-crm/main/index.html
set LINK_VERCEL=https://inn-crm-f3f-energy.vercel.app
set ARQUIVO_VERSAO=%PASTA_INN%\versao.txt

if not exist "%ARQUIVO_VERSAO%" echo 0 > "%ARQUIVO_VERSAO%"
set /p VERSAO_ATUAL=<"%ARQUIVO_VERSAO%"
set /a VERSAO_NOVA=%VERSAO_ATUAL%+1

cls
echo.
echo =======================================
echo  INN - Innovatis CRM Solar
echo  Versao atual: v%VERSAO_ATUAL%
echo  Nova versao : v%VERSAO_NOVA%
echo =======================================
echo.

cd /d "%PASTA_INN%"

echo [1/3] Sincronizando com GitHub...
git pull origin main

if %errorlevel% equ 0 (
    echo [OK] Atualizado para versao mais recente!
) else (
    echo [ERRO] Falha ao sincronizar.
    pause
    exit /b 1
)

echo %VERSAO_NOVA%> "%ARQUIVO_VERSAO%"

echo.
echo [2/3] Salvando versao v%VERSAO_NOVA%...
git add versao.txt
git commit -m "INN v%VERSAO_NOVA% - %date%"

echo.
echo [3/3] Publicando no Vercel...
git push origin main

if %errorlevel% equ 0 (
    echo.
    echo =======================================
    echo  INN v%VERSAO_NOVA% publicado!
    echo  Aguarde 30s e acesse:
    echo  %LINK_VERCEL%
    echo =======================================
) else (
    echo [ERRO] Falha no push.
)

echo.
set /p ABRIR=Abrir o INN no navegador? S ou N: 
if /i "%ABRIR%"=="S" start %LINK_VERCEL%

echo.
echo Versao instalada: v%VERSAO_NOVA%
echo.
pause
