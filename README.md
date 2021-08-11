# ***mouse axis inverter***
<p align="center">
  <img src="/icons/iconX.png" />
  <img src="/icons/iconY.png" />
</p>

# Purpose
A bit clunky scripts that inverts one of the 2 axis. 
Update: Rewritten for performance reasons see [Common patterns and mistakes](https://github.com/boppreh/keyboard#common-patterns-and-mistakes)

# Usage 
## Python
Dependencies:
```shell
pip install -r requirements.txt
```
Finally click on it. 
**If you don't want them to show windows cmd, rename their extension from .py to .pyw**

## Windows Executables 
Windows executables are provided for commodity. 
You can make them yourself by using [Nuitka's lib](https://nuitka.net/doc/user-manual.html):
```shell 
python -m pip install nuitka
```
```shell
python -m nuitka --windows-disable-console --follow-imports MouseX.py
```