@setlocal enabledelayedexpansion

set script_dir=%~dp0

set profile=-pr=default

if NOT "%1"=="" (
    set profile=-pr=../../%1.txt
)

conan export %script_dir% examples/testing@

pushd %script_dir%test_package

conan test %profile% . examples/testing@
