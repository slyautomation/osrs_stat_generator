# osrs_stat_generator

This project incorporates pyinstaller to package the project into a executable file. this is a good example of a project that is dependant on images and creating files which can be difficult to work as intended in a exe file. 

the main part of the code that helps ensure images and created files are referenced when running the exe file is the resourcepath function.

```
def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)
```

This will save relevent files in you user profile temp folder on you operating system and allows the exe file to run in any location.
  
run in the terminal: 
```
pyinstaller --noconsole --onefile main.spec
```
--noconsole is a command to ensure the command terminal is hidden and only the app is displayed.

--onefile packages the python project into a single exe file

main.spec is a specification config file which details how the pyinstaller will setup the project as an executable file.
