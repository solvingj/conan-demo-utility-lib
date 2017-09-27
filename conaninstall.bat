if "%3"=="Win32" (
    set "ARCH=x86"
) else (
    set "ARCH=%3"
)
echo %ARCH%
call conan install %1 --build=outdated --cwd %2 -s arch=%ARCH% -s build_type=%4

