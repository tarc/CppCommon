@setlocal enabledelayedexpansion

set script_dir=%~dp0
pushd %script_dir%..\..

set profile=-pr=default
set build_dir=benchmarks_default

if NOT "%1"=="" (
    set profile=-pr=../conan/%1.txt
    set build_dir=benchmarks_%1
)

rmdir /s/q %build_dir%
mkdir %build_dir%
pushd %build_dir%

conan install ../conan/benchmarks %profile% --build=missing
conan source ../conan/benchmarks
conan build -sf . ../conan/benchmarks
