@echo off
echo Pip instalatuta dagoen egiaztatzen

python -m pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Pip ez da aurkitu. Instalatzen...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    del get-pip.py
) ELSE (
    echo Pip instalatuta dago.
)

echo Instalatzen dependentziak (requirements.txt) ...
python -m pip install -r requirements.txt

echo ---
echo Instalazioa osatua.
pause
