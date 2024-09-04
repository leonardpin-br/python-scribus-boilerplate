#! /usr/bin/env python
"""SHOULD serve as a configuration file to Sphinx to work with Scribus 1.5.8 modules.

There are more explanations on how you COULD use it on the README.md file.

Warning:
    The Shebang Line appears to have no practical effect, at least on Windows,
    in the ``<project_root>/resources/documentation_config/build_sphinx_scribusdoc.py``
    file even with the ``.py`` files associated with the launcher
    (``C:\\Windows\\pyw.exe``).

    To make this script a little bit more portable, the shebang line is:

        #! /usr/bin/env python


    The use of the **python** command, inside the ``make.bat`` file, makes all
    the difference in the execution of the documentation generation.

References:
    `Is there possibility how to use scribus module in python outside Scribus?`_
    
    `Getting Sphinx to work with Maya modules`_

    `How Should I Set Default Python Version In Windows?`_

    `unable to run 'aws' from cygwin`_

    `Find full path of the Python interpreter?`_

    `How to force Sphinx to use Python 3.x interpreter`_

    `Standalone Maya Python Interpreter`_

    `Could not import extension sphinxcontrib.napoleon #10378`_

    `3.7 Shebang Line`_

    `Should I put #! (shebang) in Python scripts, and what form should it take?`_

.. _Is there possibility how to use scribus module in python outside Scribus?:
   https://stackoverflow.com/a/33370042
.. _Getting Sphinx to work with Maya modules:
   https://geektalker.wordpress.com/2013/03/26/getting-sphinx-to-work-with-maya-modules/
.. _How Should I Set Default Python Version In Windows?:
   https://stackoverflow.com/a/52913040/3768670
.. _unable to run \'aws\' from cygwin:
   https://stackoverflow.com/a/62093489/3768670
.. _Find full path of the Python interpreter?:
   https://stackoverflow.com/a/2589722/3768670
.. _How to force Sphinx to use Python 3.x interpreter:
   https://stackoverflow.com/a/40638825/3768670
.. _Standalone Maya Python Interpreter:
   https://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/PyMel/standalone.html#standalone-maya-python-interpreter
.. _Could not import extension sphinxcontrib.napoleon #10378:
   https://github.com/sphinx-doc/sphinx/issues/10378#issuecomment-1107455569
.. _3.7 Shebang Line:
   https://google.github.io/styleguide/pyguide.html#37-shebang-line
.. _Should I put #! (shebang) in Python scripts, and what form should it take?:
   https://stackoverflow.com/a/14599026/3768670
"""


import os
import sys

# Gets the full path of this script file dinamically.
THIS_FILE_DIR = os.path.realpath(os.path.dirname(__file__))

# Gets the full path of the project's root folder:
pathList = THIS_FILE_DIR.split("\\")
pathList = pathList[:-2]
project_root = "\\".join(pathList)

# Builds the path to the Sphinx's directory (inside the virtual environment):
sphinx_dir = os.path.join(project_root, "py37env", "Lib", "site-packages")

# If the path is not in sys.path:
for path in sys.path:
    if path == sphinx_dir:
        break
else:
    sys.path.insert(0, sphinx_dir)

import sphinx

import scribus

if __name__ == '__main__':
    
    sys_argv = sys.argv
    """list[str]: sys.argv is a list containing the name of the script being
    executed and all the arguments passed to it. The first item is the script's
    name.
    
    Below are the entire ``sys.argv`` list passed to this file by Sphinx,
    executing the script inside ``package.json`` ("build:html:doc"). That script
    translates to ``make clean && make html``::
    
        ['E:/cloud/Backup/Libraries/scripts/maya/python-maya-boilerplate/resources/documentation_config/build_sphinx_mayadoc.py', '-M', 'clean', 'source', 'build']
        ['E:/cloud/Backup/Libraries/scripts/maya/python-maya-boilerplate/resources/documentation_config/build_sphinx_mayadoc.py', '-M', 'html', 'source', 'build']
    """
    # This script is being called the first time (for each make) with only the
    # name of the script in sys.argv. The if below deals with it.
    if len(sys_argv) == 1:
        quit()
    
    argv = sys_argv[1:]
    """list[str]: argv becomes only the arguments passed to this script file.
    
    The assignment creates a new list removing the first item of the original::
    
        ['-M', 'clean', 'source', 'build']
        ['-M', 'html', 'source', 'build']
    """
    
    sphinx_module = sphinx.__file__.replace("\\", "/")
    """str: As this script file is called twice (``make clean && make html``),
    this variable is assigned twice::
    
        E:/HDD_4TB/cloud/Backup/Libraries/scripts/scribus/python-scribus-boilerplate/py37env/Lib/site-packages/sphinx/__init__.py
        E:/HDD_4TB/cloud/Backup/Libraries/scripts/scribus/python-scribus-boilerplate/py37env/Lib/site-packages/sphinx/__init__.py
    """
    
    # The insert() method inserts the specified value at the specified position.
    argv.insert(0, sphinx_module)
    # ['E:/HDD_4TB/cloud/Backup/Libraries/scripts/scribus/python-scribus-boilerplate/py37env/Lib/site-packages/sphinx/__init__.py', '-M', 'clean', 'source', 'build']
    # ['E:/HDD_4TB/cloud/Backup/Libraries/scripts/scribus/python-scribus-boilerplate/py37env/Lib/site-packages/sphinx/__init__.py', '-M', 'html', 'source', 'build']
    
    sphinx.main(argv)