@echo off

Rem if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

start cmd /k python ./testing/unit_test/test0.py



