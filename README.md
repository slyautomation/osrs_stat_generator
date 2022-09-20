# osrs_stat_generator

Creates a stat card of your the desired stats inputted into the userform:

Starts with a blank card:

![image](https://user-images.githubusercontent.com/81003470/191150799-5ac85877-0e17-4f76-bfae-afaf0c13d726.png)

Add in numbers for each skill:

![image](https://user-images.githubusercontent.com/81003470/191150904-cf8a2410-17c1-4cd5-a878-c6f8160aac11.png)

The result is saved to a png file 'Result.png' located in the same location as the exe file.

![image](https://user-images.githubusercontent.com/81003470/191150984-e1a38e4e-0e50-4277-8150-5adeeb1f9f93.png)


This project incorporates pyinstaller to package the project into a executable file. this is a good example of a project that is dependant on images and creating files which can be difficult to work as intended in a exe file. 

The main part of the code that helps ensure images and created files are referenced when running the exe file is the resourcepath function.

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

This will save relevent files in you user profile temp folder on your operating system and allows the exe file to run in any location.
  
Run in the terminal: 
```
pyinstaller --noconsole --onefile main.spec
```
--noconsole is a command to ensure the command terminal is hidden and only the app is displayed.

--onefile packages the python project into a single exe file

main.spec is a specification config file which details how the pyinstaller will setup the project as an executable file.

```
a = Analysis(['main.py'],
             pathex=['C:\\Users\\i7 8700\\PycharmProjects\\osrs_xp_stat_generator'],
             binaries=[],
             datas=[('C:\\Users\\i7 8700\\PycharmProjects\\osrs_xp_stat_generator\\*.png','.'),('C:\\Users\\i7 8700\\PycharmProjects\\osrs_xp_stat_generator\\images\\','.')],
```

An important component to ensure images are build into the exe file is updating the spec file with the path location of the image files and any other files that are needed. from the above referenced in 'datas=' i want any png file to be included in the packaging in the exe. make sure to change the file path as it is set to my userpath.
