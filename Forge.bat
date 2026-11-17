@echo off
rem Atelier Forge : double-clic pour ouvrir la page qui lance les outils Forge (rien à taper).
rem La fenêtre reste ouverte tant que l'atelier tourne ; elle se ferme quand on quitte la page.
chcp 65001 >nul
setlocal
cd /d "%~dp0"

rem Python à utiliser : d'abord l'environnement .venv du projet (uv), sinon uv run, sinon python
set "PY="
if exist "%~dp0.venv\Scripts\python.exe" set "PY=%~dp0.venv\Scripts\python.exe"
if not defined PY (where uv >nul 2>nul && set "PY=uv run python")
if not defined PY set "PY=python"

%PY% "%~dp0scripts\forge\forge.py" %*
if errorlevel 1 (
    echo.
    echo L'atelier s'est arrêté sur une erreur ^(voir ci-dessus^).
    pause
)
