# README
## Windows (x64):
### Setup:
0. Create a venv:  
`python.exe -m venv venv/`
0. Upgrade setuptools in the venv with:  
`.\venv\Scripts\pip.exe install --upgrade setuptools`  
This step is essential to allow distutils to find the toolchain installed by Microsoft Build Tools for Visual Studio 2017.
0. Install the weasyprint requirements as instructed at  
`http://weasyprint.readthedocs.io/en/latest/install.html#windows`  
 1. Install GTK3 with "Set up PATH environment variable to include GTK+" checked from:  
 `https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases`
 2. Restart machine
 3. Install Build Tools for Visual Studio 2017 from:  
 `https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017`
0. `.\venv\Scripts\pip.exe install markdown weasyprint`
0. Download the lxml‑3.8.0‑cp36‑cp36m‑win_amd64.whl from:  
`http://www.lfd.uci.edu/~gohlke/pythonlibs/`
0. Uninstall the *broken* version of lxml from the venv with:  
`.\venv\Scripts\pip.exe uninstall lxml`
0. Install lxml from the wheel with:  
`.\venv\Scripts\pip.exe install .\wheels\lxml-3.8.0-cp36-cp36m-win_amd64.whl`
0. Test the weasyprint install with:  
`.\venv\Scripts\python.exe -m weasyprint http://weasyprint.org weasyprint.pdf`

### Usage:
* Run makepdf using:  
`.\venv\Scripts\python.exe .\makepdf.py`
