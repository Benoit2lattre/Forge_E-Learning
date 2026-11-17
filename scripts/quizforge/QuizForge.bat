@echo off
rem QuizForge
rem  - double-clic : assistant pas à pas (menus numérotés)
rem  - glisser un ou plusieurs classeurs sur ce fichier : conversion avec le profil par défaut
chcp 65001 >nul
setlocal

rem Python à utiliser : d'abord l'environnement .venv du projet (uv), sinon uv run, sinon python
set "PY="
if exist "%~dp0.venv\Scripts\python.exe" set "PY=%~dp0.venv\Scripts\python.exe"
if not defined PY if exist "%~dp0..\.venv\Scripts\python.exe" set "PY=%~dp0..\.venv\Scripts\python.exe"
if not defined PY if exist "%~dp0..\..\.venv\Scripts\python.exe" set "PY=%~dp0..\..\.venv\Scripts\python.exe"
if not defined PY (where uv >nul 2>nul && set "PY=uv run python")
if not defined PY set "PY=python"

if "%~1"=="" (
    cd /d "%~dp0..\.."
    %PY% "%~dp0quizforge.py" assistant
) else (
    cd /d "%~dp1"
    %PY% "%~dp0quizforge.py" %*
)
echo.
pause
