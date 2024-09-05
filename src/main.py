#! python.exe
"""Entry point of this script/app.

Last modified in 2024-09-03

Python version 3.7.9 (Scribus 1.5.8)

This is the file to run from Scribus.

Note:
    If **unit tests** are in place, this is how they can be run::

        python -m unittest discover

    If coverage is being used too, this is how it can be run::

        coverage erase
        coverage run -m unittest discover
        coverage html

    In this starter kit, it is not necessary to run those commands manually,
    though. They are preconfigure in the ``package.json`` file as scripts.

Important:
    Sphinx (and its packages) **MUST** be installed in the virtual environment
    in order to avoid import errors.

    Having multiple Python versions on the machine and Sphinx installed in one
    of them, leads to confusion and hard to track bugs.

Note:
    How to generate the requirements.txt::

        pip freeze > requirements.txt

    How to install packages from requirements.txt::

        pip install -r requirements.txt

Note:
    To exclude certain modules from being documented, it is necessary to pass
    them as arguments to ``sphinx-apidoc``::

        sphinx-apidoc --force -o ./docs/sphinx/source ./src ./src/activerecord/db_credentials.py

    The example above is in the **package.json** file as the ``build:source:doc`` script.

References:
    `Add Scribus reference to Visual Studio 2019 Python project`_

    `Getting started with Python scripting in Scribus`_

    `sphinx-apidoc ignoring some modules/packages`_

    `Coverage.py`_

    `Configuration reference`_

    `Test Code Coverage`_

    `Python Sphinx exclude patterns`_

    `sphinx-apidoc`_

    `Unpacking kwargs`_

    `PEP 484`_

    `Python docstring rendering\: reStructuredText markup inside directives not recognized`_

    `Creating the package files`_

    `Maintain a Reference to your Widget`_

    `How can I check if a module has been imported?`_


.. _Add Scribus reference to Visual Studio 2019 Python project:
   https://stackoverflow.com/a/72646893
.. _Getting started with Python scripting in Scribus:
   https://opensource.com/life/16/10/python-scripting-scribus
.. _sphinx-apidoc ignoring some modules/packages:
   https://chadrick-kwag.net/sphinx-apidoc-ignoring-some-modules-packages/
.. _Coverage.py:
   https://coverage.readthedocs.io/en/6.3.2/#coverage-py
.. _Configuration reference:
   https://coverage.readthedocs.io/en/6.3.2/config.html#configuration-reference
.. _Test Code Coverage:
   https://cpske.github.io/ISP/testing/code-coverage
.. _Python Sphinx exclude patterns:
   https://stackoverflow.com/a/43868129
.. _sphinx-apidoc:
   https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
.. _Unpacking kwargs:
   https://stackoverflow.com/a/28771348
.. _PEP 484:
   https://www.python.org/dev/peps/pep-0484/
.. _Python docstring rendering\: reStructuredText markup inside directives not recognized:
   https://youtrack.jetbrains.com/issue/PY-40010
.. _Creating the package files:
   https://packaging.python.org/en/latest/tutorials/packaging-projects/creating-the-package-files
.. _Maintain a Reference to your Widget:
   https://help.autodesk.com/cloudhelp/2018/ENU/Maya-SDK/files-to-wrap/GUID-66ADA1FF-3E0F-469C-84C7-74CEB36D42EC.htm
.. _How can I check if a module has been imported?:
   https://stackoverflow.com/a/30483269/3768670

"""

import os
import sys

# Gets the full paths dinamically.
src_dir = os.path.realpath(os.path.dirname(__file__))
project_root_dir = os.path.realpath(os.path.dirname(src_dir))
site_packages_from_venv = os.path.join(project_root_dir, "py37env", "Lib", "site-packages")

# If the path is not in sys.path:
for path in sys.path:
    if path == src_dir:
        break
else:
    sys.path.insert(0, src_dir)
    
# If the path is not in sys.path:
for path in sys.path:
    if path == site_packages_from_venv:
        break
else:
    sys.path.insert(1, site_packages_from_venv)

import segno

# try:
#     import scribus
# except ImportError:
#     print("Unable to import the 'scribus' module. This script will only run within")
#     print("the Python interpreter embedded in Scribus. Try Script->Execute Script.")

from appclasses import Admin, Bicycle
import shared


def untested_function():
    """The only reason this function exists is to not be tested.

    This function will appear, in the coverage HTML report, as an untested
    line of code.

    Returns:
        bool: The value is only an example and will not be used.
    """
    return False


def create_qr_code(target, filename):
    """Creates the QR Code in SVG format and stores it in the 
    `<project_root>/resources/svg` folder.

    Args:
        target (str): The target of the QR Code (link address).
        filename (str): The name without the SVG extension of the file that will
            be created.

    Returns:
        str: Full path to file.

    References:
        `Generate Beautiful QR Codes With Python`_

    .. _Generate Beautiful QR Codes With Python:
       https://realpython.com/python-generate-qr-code/

    """
    qrcode = segno.make_qr(target)
    full_path_to_file = os.path.join(project_root_dir, "resources", "svg", filename + ".svg")
    qrcode.save(
        full_path_to_file,
        kind="svg",
        scale=5,
        border=4,
        light="#ffffff",
        dark="#000000",
        quiet_zone="#ffffff"
    )
    return full_path_to_file


def main():
    """The main function to execute the entire project/application.
    """
    # if not scribus.haveDoc():
    #     # scribus.newDocument(PAPER_A4, (10, 10, 10, 10), PORTRAIT, 1, UNIT_MILLIMETERS, PAGE_1, 0, 2)
    #     scribus.messageBox('Scribus - Script Error', "No document open",
    #                        scribus.ICON_WARNING, scribus.BUTTON_OK)
    #     sys.exit(1)
    
    # if scribus.selectionCount() == 0:
    #     scribus.messageBox('Scribus - Script Error', "There is no object selected.\nPlease select a text frame and try again.",
    #                        scribus.ICON_WARNING, scribus.BUTTON_OK)
    #     sys.exit(2)
    
    # if scribus.selectionCount() > 1:
    #     scribus.messageBox('Scribus - Script Error', "You have more than one object selected.\nPlease select one text frame and try again.",
    #                        scribus.ICON_WARNING, scribus.BUTTON_OK)
    #     sys.exit(2)
    
    # textbox = scribus.getSelectedObject()
    # ftype = scribus.getObjectType(textbox)
    
    # if (ftype != "TextFrame"):
    #     scribus.messageBox('Scribus - Script Error', "This is not a textframe. Try again.", 
    #                        scribus.ICON_WARNING, scribus.BUTTON_OK)
    #     sys.exit(2)
    
    # today = date.today()
    # d = today.strftime("%A, %B %d, %Y")
    # length = scribus.getTextLength()
    # scribus.selectText(19, length-19, textbox)
    # scribus.deleteText(textbox)
    # scribus.insertText(d, -1, textbox)
    
    # length = scribus.getTextLength()
    # scribus.selectText(19, length-19, textbox)
    # scribus.setFontSize(14.0, textbox)
    
    # message = "Hello"
    # print(message)
    
    #     scribus.messageBox('Console simulation', "The ID of the admin was not found.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    create_qr_code("https://www.leonardopinheiro.net", "basic_qrcode")
    



main()
