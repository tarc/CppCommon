@echo off

@setlocal enabledelayedexpansion

set script_dir=%~dp0
pushd %script_dir%..\

set profile=-pr=default
set build_dir=default

if "%1" neq "" if "%1" neq "default" (
    set profile=-pr=default -pr=../conan/msys2_mingw.txt -pr=../conan/%1.txt
    if "%1" neq "seh-x86_64" if "%1" neq "dwarf2-x86" (
        set profile=-pr=../conan/%1.txt
    )
    set build_dir=%1
)

set _all=%*
call set _tail=%%_all:*%2=%% 2> NUL
set _tail=%2%_tail%
set options=%_tail%

if "%1"=="" (
    set options=
)

rmdir /s/q %build_dir%
mkdir %build_dir%
pushd %build_dir%

:: FOR /F "delims= " %%I IN ('git show --format^=%%ci -s HEAD') DO SET version=%%I

:: set version=cci.%version:-=%

set version=1.0.0.0

set ref=cppcommon/%version%@

echo Reference: %ref% 1>&2
echo Profile: %profile% 1>&2
echo Options: %options% 1>&2


set error_message=conan install ../conan %ref% %profile% %options% --build=missing
call !error_message!
if NOT '!ERRORLEVEL!'=='0' goto fail

set error_message=conan source ../conan
call !error_message!
if NOT '!ERRORLEVEL!'=='0' goto fail

set error_message=conan build ../conan
call !error_message!
if NOT '!ERRORLEVEL!'=='0' goto fail

set error_message=conan export-pkg ../conan %ref% -f
call !error_message!
if NOT '!ERRORLEVEL!'=='0' goto fail

set error_message=conan test ../conan/test_package %ref% %profile% %options%
call !error_message!
if NOT '!ERRORLEVEL!'=='0' goto fail


:success
    exit /b 0

:fail
    echo Something wrong during:
    echo ^> %error_message%
    exit /b 1
