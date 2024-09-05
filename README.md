# Python starter project to create applications (not only but specially) for Scribus.

This starter kit is preconfigured to facilitate fast development. It is based on
my ``python-maya-boilerplate`` ([python-maya-boilerplate](https://github.com/leonardpin-br/python-maya-boilerplate)) 
repository that was made for Autodesk Maya 2020 (Python 2.7.11). This one was 
adapted for Scribus 1.5.8 (Python 3.7.9).



## Before you begin

### Git and Cygwin
Install Git (and Git Bash) for version control.

Cygwin is a good terminal and I suggest you use it. But, you can execute the BASH
scripts with just Git Bash.

### Spaces in file paths
Make sure you clone this repository to a path without spaces in it. Scribus can and do execute without problems, but Sphinx will throw an error if there are any spaces in the path.

### _example files
There are files that have ``_example`` in their names. Those files were created to deal with source control.

It is necessary to copy and rename them, removing the ``_example``. Those files are:

```
<project_root>/.vscode/settings_example.json
<project_root>/docs/sphinx/make_example.bat (the adaptation does not work in Scribus)
<project_root>/resources/qss/Combinear_example.qss
<project_root>/src/activerecord/db_credentials_example.py
```

### Line endings (CRLF and LF) on Windows
The ``<project_root>/docs/sphinx/make.bat`` file should have CRLF line endings.

The BASH script (``.sh``) files should have LF (Unix) line endings even if you are using Windows. They should be executed in Cygwin or Git Bash.

The provided ``.gitattributes`` file has a configuration that should work without problems (Reference: [Configuring Git to handle line endings](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)).



## Inspirations and reference
This kit is heavily influenced by the greate course
[PHP: Object-Oriented Programming with Databases](https://www.linkedin.com/learning/php-object-oriented-programming-with-databases)
taught by Kevin Skoglund. If you are learning about OOP, I highly recommend it
even if PHP is not your primary focus.



## Why is it better than a script in a single file?
This starter kit allows the development of a more powerfull tool. Instead of creating a single script, the user of this kit will be able to create a small application.



## It includes
    1. Easy password hashing and verification (bcrypt). Even though Scribus is not able to load
    the BCrypt package more than once per session, if the user of this kit needs to hash and 
    verify a password, it is already preconfigured.
    2. An abstract class to be inherited by all the others that access
    the database. It is an application of the Active Record design pattern.
    3. Two example subclasses are provided. One for a product and one for
    an admin, both are subclasses of the database one (active record).
    4. The code is heavly documented (using Sphinx and Google style docstrings) and HTML generation
    is preconfigured.
    5. General and validation functions that can be easily reused in other projects.
    6. Unit tests and coverage are preconfigured.
    7. Line endings are preconfigured.
    8. QR Code generation is preconfigured.



## Dependencies

### Node.js
It depends on Node.js, but only for development (documentation and unit tests).

Install Node.js and navigate to the root folder of this project. Install node
dependencies with the command:

```
npm install
```

The provided `package.json` file has many useful scripts.

### MySQL

Having a MySQL database server is only necessary if you need communication with
one. If your scripts do not access a database, you do not need it. 

If you will not use a database, remove te `import` statements.

If you use a Database Management System (DBMS) different from MySQL, editing the
code will be easy.

### Python version and virtual environments

Install Python 3 and them install the `virtualenv` package. Python 3 allows the
installation of tools like Qt Designer later. Another very useful factor is the
installation of lauchers. ~~The configuration os Sphinx will depend on it later.~~ Does not work on Scribus 1.5.8.

`virtualenv` will allow you to create virtual environments.

The command to install the recommended package is:

```
pip install virtualenv
```

Then, create a virtual environment (`py37env` folder)
in the root folder of this project. Run this command from the project's root folder:

```
virtualenv --python="C:/Program Files/Python37/python.exe" "./py37env"
```

Activate the virtual environment with the command:
```
source ./py37env/Scripts/activate   => Cygwin and Git Bash
py37env\Scripts\activate            => Command Prompt
.\py37env\Scripts\activate.ps1      => PowerShell
```

It is important to install the necessary packages using the command below from
the project's root:
```
pip install -r requirements.txt
```
It will install all the packages, including the appropriate version of Sphinx.



## Documentation
By now, you should have installed Sphinx inside the virtual environment (`py37env` folder).

### Terminals on Windows systems
On Windows systems, the terminal you are using makes a big difference. On my tests, I used
- Command Prompt
- Cygwin
- Git Bash
- Powershell

Even after activating the virtual environment in all of them, the results may differ.

### The shebang line

Only the files that are intended to be executed directly should have the shebang line (Reference: [3.7 Shebang Line](https://google.github.io/styleguide/pyguide.html#37-shebang-line)). In this code, there are only two files that should have it:
```
<project_root>/src/main.py
<project_root>/resources/documentation_config/build_sphinx_mayadoc.py (does not work in Scribus)
```

Windows do not support the shebang line (the first line starting with `#! `). But, since Python 3.3 (Reference: [Should I put #! (shebang) in Python scripts, and what form should it take?](https://stackoverflow.com/a/14599026/3768670)), Python installs launchers like

```
"C:\Windows\pyw.exe"
```

The `.py` files should be associated with the above laucher as the default program to execute them.

___________

In my tests, **the shebang line only makes a difference if the main script file is executed directly.** That is what will be discussed below.

___________

#### The tested shebang lines

The laucher **does read** the shebang lines. The commands for each terminal are:
```
full/path/to/src/main.py       => Cygwin and Git Bash
full\path\to\src\main.py       => Command Prompt
.\full\path\to\src\main.py     => PowerShell
```

The result is:

```
#! python.exe                                          => Cygwin only accepts this one.
#! /c/Progra~1/Scribu~1/python/python.exe              => Git Bash accepts the first and the second.
#! "C:\Program Files\Scribus 1.5.8\python\python.exe"  => Only accepted by Command Prompt and PowerShell.
```

The only shebang line that worked in all of the tested terminals was `#! python.exe`. That line depends on the alteration of the system environment variables. The steps are listed below.

### Step-by-step on Windows systems
For the documentation generation to work as expected, it is necessary to do the following:

#### 1. Edit the environment variables
Add the path to the bundled `python.exe` to the system variables. The default path is
```
C:\Program Files\Scribus 1.5.8\python
```
Move it tho the top of the list.

#### 2. ~~Edit the make.bat file~~ Does not work in Scribus 1.5.8
Sphinx does not create the HTML documentation. The error message says that 
Sphinx cannot import its own ``main`` function. It appears to be a known bug (Reference: [ ImportError on building documents #7766](https://github.com/sphinx-doc/sphinx/issues/7766)). Many small successfull tests 
were made, but the entire sequence does not work.

Simply use the ``make.bat`` file generated for the documentation. Int that file, the important line is this one below. Keep it like that.

```
set SPHINXBUILD=sphinx-build
```

Do not use the `<project_root>/scripts/update_make_bat.sh`. The resulting change in the `make.bat` **does not work**:

```
set SPHINXBUILD=scribus -g --python-script "full/path/to/the/build_sphinx_scribusdoc.py" (Do not use it.)
```

The command `scribus -g --python-script` should allow Sphinx to execute the code using the Python interpreter that comes with Scribus. (Reference: [Example of command line script without arguments](https://wiki.scribus.net/canvas/Command_line_scripts#Example_of_command_line_script_without_arguments)).

The file `build_sphinx_scribusdoc.py` **should be** a custom config file that instructs Sphinx to work with the Scribus modules.



## Folder structure
```
<project_root>
|- src                          (the app)
    |- activerecord             (modules that implement the active record design pattern)
    |- appclasses               (classes specific for the application being developed)
    |- shared                   (usefull functions shared by the packages)
    |- userinterface            (example of user interface class and related modules)
|- docs                         (for the generated HTML documentation and coverage reports)
    |- coverage                 (for the generated HTML code coverage reports)
    |- sphinx                   (for the generated HTML documentation)
|- py37env                      (virtual environment folder)
|- resources                    (good to have and needed files)
    |- documentation_config     (configuration for Sphinx)
    |- example_files            (files that can be used as reference)
    |- img                      (images used in the interface creation)
    |- qss                      (for interface customization)
    |- sql                      (for databases)
    |- ui                       (files created in Qt Designer)
|- scripts                      (usefull bash scripts)
|- tests                        (unit tests)

```



## Which file will be executed?
Using this starter kit, the main.py (``<project_root>/src/main.py``) will be
the file being executed from Scribus.