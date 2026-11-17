@echo off
rem CapsuleForge
rem  - double-clic : assistant pas à pas (enregistrer, construire, vérifier, reprendre un .approj)
rem  - glisser un dossier de capsule ou un capsule.yaml sur ce fichier : construction du lecteur
rem  - glisser un projet ActivePresenter (.approj) : reprise en capsule.yaml (lecture seule)
chcp 65001 >nul
setlocal

rem Python à utiliser : d'abord l'environnement .venv du projet (uv), sinon uv run, sinon python
set "PY="
if exist "%~dp0.venv\Scripts\python.exe" set "PY=%~dp0.venv\Scripts\python.exe"
if not defined PY if exist "%~dp0..\.venv\Scripts\python.exe" set "PY=%~dp0..\.venv\Scripts\python.exe"
if not defined PY if exist "%~dp0..\..\.venv\Scripts\python.exe" set "PY=%~dp0..\..\.venv\Scripts\python.exe"
if not defined PY (where uv >nul 2>nul && set "PY=uv run python")
if not defined PY set "PY=python"

rem dépendances de l'enregistreur (installées une fois dans .venv)
%PY% -c "import pynput, mss, PIL, yaml" >nul 2>nul
if errorlevel 1 (
    echo Installation des dépendances de CapsuleForge ^(pynput, mss, uiautomation^)...
    where uv >nul 2>nul && (cd /d "%~dp0..\.." & uv pip install -r requirements.txt) || %PY% -m pip install pynput mss uiautomation Pillow PyYAML
)

if "%~1"=="" (
    cd /d "%~dp0..\.."
    %PY% "%~dp0capsuleforge.py" assistant
) else if /i "%~x1"==".approj" (
    cd /d "%~dp0..\.."
    %PY% "%~dp0capsuleforge.py" approj "%~1"
) else (
    cd /d "%~dp0..\.."
    %PY% "%~dp0capsuleforge.py" construire "%~1"
)
echo.
pause
