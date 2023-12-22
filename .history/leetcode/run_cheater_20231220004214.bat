@echo off
setlocal enabledelayedexpansion

set /A "min=1"
set /A "max=5"

set "python_executable=C:\Python312\python.exe"

set /A "random_executions=!random! %% (%max% - %min% + 1) + %min%"

for /L %%i in (1, 1, %random_executions%) do (
    timeout /t 15 /nobreak >nul
    %python_executable% C:\Users\hamid\OneDrive\Documents\Python-Practice\leetcode\cheater.py
)

endlocal
