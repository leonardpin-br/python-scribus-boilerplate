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

try:
    import scribus
except ImportError:
    print("Unable to import the 'scribus' module. This script will only run within")
    print("the Python interpreter embedded in Scribus. Try Script->Execute Script.")
    sys.exit(1)

# Gets the full path of this script file dinamically.
src_dir = os.path.realpath(os.path.dirname(__file__))

# If the path is not in sys.path:
for path in sys.path:
    if path == src_dir:
        break
else:
    sys.path.insert(0, src_dir)

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


def main():
    """The main function to execute the entire project/application.
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    
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
    
    
    
    # BICYCLE: FIND ALL
    # ==========================================================================
    # bikes = Bicycle.find_all()
    
    # for bike in bikes:
        
        # FOR TESTING IN THE DEVELOPMENT ENVIRONMENT:
        # -------------------------------------------
        # print(bike.brand)
        # print(bike.model)
        # print(bike.year)
        # print(bike.category)
        # print(bike.gender)
        # print(bike.color)
        # print("{weight_kg} / {weight_lbs}".format(weight_kg=bike.get_weight_kg(), weight_lbs=bike.weight_lbs))
        # print(bike.condition_id)
        # print(bike.price)
        # print("====================================================\n\n")
        
        # FOR TESTING INSIDE SCRIBUS:
        # ---------------------------
        # bike_as_text = bike.brand + "\n"
        # bike_as_text += bike.model + "\n"
        # bike_as_text += "{bike_year}".format(bike_year=bike.year) + "\n"
        # bike_as_text += bike.category + "\n"
        # bike_as_text += bike.gender + "\n"
        # bike_as_text += bike.color + "\n"
        # bike_as_text += "{weight_kg} / {weight_lbs}".format(weight_kg=bike.get_weight_kg(), weight_lbs=bike.weight_lbs) + "\n"
        # bike_as_text += "{bike_condition_id}".format(bike_condition_id=bike.condition_id) + "\n"
        # bike_as_text += "{bike_price}".format(bike_price=bike.price) + "\n"
        # bike_as_text +="====================================================\n\n"
        # scribus.messageBox('Console simulation', bike_as_text, scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    # BICYCLE: FIND BY ID
    # ==========================================================================
    # bike = Bicycle.find_by_id(2)
    
    # if bike:
    
    # FOR TESTING IN THE DEVELOPMENT ENVIRONMENT:
    # -------------------------------------------
    #     print(bike.name())
    #     print("-------------------------------------------")
    #     print(bike.id)
    #     print(bike.brand)
    #     print(bike.model)
    #     print(bike.year)
    #     print(bike.category)
    #     print(bike.gender)
    #     print(bike.color)
    #     print("{weight_kg} / {weight_lbs}".format(weight_kg=bike.get_weight_kg(), weight_lbs=bike.weight_lbs))
    #     print(bike.condition())
    #     print("${price}".format(price=bike.price))
    # else:
    #     print("The ID was not found.")
        
    # FOR TESTING INSIDE SCRIBUS:
    # ---------------------------
    #     bike_as_text = bike.name() + "\n"
    #     bike_as_text += "-------------------------------------------" + "\n"
    #     bike_as_text += "{bike_id}".format(bike_id=bike.id) + "\n"
    #     bike_as_text += bike.brand + "\n"
    #     bike_as_text += bike.model + "\n"
    #     bike_as_text += "{bike_year}".format(bike_year=bike.year) + "\n"
    #     bike_as_text += bike.category + "\n"
    #     bike_as_text += bike.gender + "\n"
    #     bike_as_text += bike.color + "\n"
    #     bike_as_text += "{weight_kg} / {weight_lbs}".format(weight_kg=bike.get_weight_kg(), weight_lbs=bike.weight_lbs) + "\n"
    #     bike_as_text += bike.condition() + "\n"
    #     bike_as_text += "${price}".format(price=bike.price) + "\n"
    #     scribus.messageBox('Console simulation', bike_as_text, scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    # else:
    #     message = "The ID was not found."
    #     scribus.messageBox('Console simulation', message, scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    # BICYCLE: CREATING A RECORD
    # ==========================================================================
    # bicycle = Bicycle(brand="Schwinn", model="Cutter", year=2016, category="City", color="white",
    #                   gender="Unisex", price=450, weight_kg=18, condition_id=4, description="")
    # bicycle = Bicycle(brand="Mongoose", model="Switchback Sport", year=2015, category="Mountain", color="blue",
    #                   gender="Mens", price=399, weight_kg=24, condition_id=2, description="")
    # kwargs = {
    #     "brand": "Diamondback",
    #     "model": "Bob's Overdrive",
    #     "year": 2016,
    #     "category": "Mountain",
    #     "color": "dark green",
    #     "gender": "Unisex",
    #     "price": 565,
    #     "weight_kg": 23.7,
    #     "condition_id": 3,
    #     "description": ""
    # }
    # kwargs = {
    #     "brand": "Schwinn",
    #     "model": "Sanctuary 7-Speed",
    #     "year": 2016,
    #     "category": "Cruiser",
    #     "color": "purple",
    #     "gender": "Womens",
    #     "price": 190,
    #     "weight_kg": 19.5,
    #     "condition_id": 3,
    #     "description": ""
    # }
    # kwargs = {
    #     "brand": "Junk Bike",
    #     "model": "Delete me",
    #     "year": 1998,
    #     "category": "Road",
    #     "color": "white",
    #     "gender": "Mens",
    #     "price": 2,
    #     "weight_kg": 1,
    #     "condition_id": 3,
    #     "description": ""
    # }
    
    # bicycle = Bicycle(**kwargs)
    # result = bicycle.save()
    # if result:
    #     print("The new ID is: {id}".format(id=bicycle.id))
    #     print("The bicycle was created successfully.")
    
        # scribus.messageBox('Console simulation', "The new ID is: {id}".format(id=bicycle.id), scribus.ICON_INFORMATION, scribus.BUTTON_OK)
        # scribus.messageBox('Console simulation', "The bicycle was created successfully.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
        
    # else:
    #     print(shared.display_errors(bicycle.errors))
        # scribus.messageBox('Console simulation', shared.display_errors(bicycle.errors), scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    
    # BICYCLE: UPDATING A RECORD
    # ==========================================================================
    # bike = Bicycle.find_by_id(7)
    
    # if bike:
    
    #     kwargs = {
    #         "id": bike.id,
    #         "brand": bike.brand, # bike.brand
    #         "model": "Bob's Overdrive", # Bob's Overdrive
    #         "year": bike.year,
    #         "category": bike.category,
    #         "gender": bike.gender,
    #         "color": bike.color,
    #         "weight_kg": bike.weight_kg,
    #         "condition": bike.condition,
    #         "price": bike.price
    #     }
    
    #     bike.merge_attributes(**kwargs)
    #     result = bike.save()
    #     if result:
    # #         print("The bicycle was updated successfully.")
    #         scribus.messageBox('Console simulation', "The bicycle was updated successfully.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    #     else:
    # #         print(shared.display_errors(bike.errors))
    #         scribus.messageBox('Console simulation', shared.display_errors(bike.errors), scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    # else:
    # #     print("The ID was not found.")
    #     scribus.messageBox('Console simulation', "The ID was not found.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    # BICYCLE: DELETING A RECORD
    # ==========================================================================
    # bike = Bicycle.find_by_id(7)
    
    # if bike:
    
    #     result = bike.delete()
    #     if result:
    #         # print("{name} was deleted successfully.".format(name=bike.name()))
    #         scribus.messageBox('Console simulation', "{name} was deleted successfully.".format(name=bike.name()), scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    #     else:
    #         # print("There was an error deleting the bicycle.")
    #         scribus.messageBox('Console simulation', "There was an error deleting the bicycle.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    # else:
    #     # print("The ID was not found.")
    #     scribus.messageBox('Console simulation', "The ID was not found.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    # ADMIN: CREATING A RECORD
    # ==========================================================================
    # kwargs = {
    #     "first_name": "Kevin",
    #     "last_name": "Skoglund",
    #     "email": "kevin@nowhere.com",
    #     "username": "kskoglund",
    #     "password": "Password#1234",
    #     "confirm_password": "Password#1234"
    # }
    # kwargs = {
    #     "first_name": "Bob",
    #     "last_name": "Smith",
    #     "email": "b@b.com",
    #     "username": "bobsmith",
    #     "password": "Password#1234",
    #     "confirm_password": "Password#1234"
    # }
    
    # admin = Admin(**kwargs)
    # result = admin.save()
    # if result:
    #     # print("The ID of the new admin is: {id}".format(id=admin.id))
    #     # print("The admin was created successfully.")
    #     scribus.messageBox('Console simulation', "The ID of the new admin is: {id}".format(id=admin.id), scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    #     scribus.messageBox('Console simulation', "The admin was created successfully.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    # else:
    #     # print(shared.display_errors(admin.errors))
    #     scribus.messageBox('Console simulation', shared.display_errors(admin.errors), scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    # ADMIN: FIND ALL
    # ==========================================================================
    # admins = Admin.find_all()
    
    # for admin in admins:
    #     # print(admin.first_name)
    #     # print(admin.last_name)
    #     # print(admin.email)
    #     # print(admin.username)
    #     # print("====================================================\n\n")
        
    #     admin_as_text = admin.first_name + "\n"
    #     admin_as_text += admin.last_name + "\n"
    #     admin_as_text += admin.email + "\n"
    #     admin_as_text += admin.username + "\n"
    #     admin_as_text += "====================================================\n\n"
    #     scribus.messageBox('Console simulation', admin_as_text, scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    # ADMIN: FIND BY ID
    # ==========================================================================
    # admin = Admin.find_by_id(2)
    
    # if admin:
    #     admin_as_text = admin.full_name() + "\n"
    #     admin_as_text += "-------------------------------------------" + "\n"
    #     admin_as_text += admin.first_name + "\n"
    #     admin_as_text += admin.last_name + "\n"
    #     admin_as_text += admin.email + "\n"
    #     admin_as_text += admin.username + "\n"
        
    #     scribus.messageBox('Console simulation', admin_as_text, scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    # else:
    #     # print("The ID was not found.")
    #     scribus.messageBox('Console simulation', "The ID was not found.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    # ADMIN: UPDATING A RECORD
    # ==========================================================================
    # admin = Admin.find_by_id(2)
    
    # if admin:
    
    #     kwargs = {
    #         "first_name": admin.first_name,
    #         "last_name": admin.last_name,
    #         "email": admin.email,
    #         "username": "bobsmith",
    #         "password": "",
    #         "confirm_password": ""
    #     }
    
    #     admin.merge_attributes(**kwargs)
    #     result = admin.save()
    #     if result:
    #         # print("The admin was updated successfully.")
    #         scribus.messageBox('Console simulation', "The admin was updated successfully.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    #     else:
    #         # print(shared.display_errors(admin.errors))
    #         scribus.messageBox('Console simulation', shared.display_errors(admin.errors), scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    # else:
    #     # print("The admin ID was not found.")
    #     scribus.messageBox('Console simulation', "The admin ID was not found.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    # ADMIN: PASSWORD VERIFY
    # ==========================================================================
    # username = "bobsmith"
    # password = "Password#1234"
    # admin = Admin.find_by_username(username)
    
    # if admin:
    #     if admin.verify_password(password):
    #         # print("The given password match with the one stored in the database.")
    #         scribus.messageBox('Console simulation', "The given password match with the one stored in the database.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    #     else:
    #         # print("The admin password does not match with the original.")
    #         scribus.messageBox('Console simulation', "The admin password does not match with the original.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    # else:
    #     # print("The admin username was not found.")
    #     scribus.messageBox('Console simulation', "The admin username was not found.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    
    
    # ADMIN: DELETING A RECORD
    # ==========================================================================
    # admin = Admin.find_by_id(2)
    
    # if admin:
    
    #     result = admin.delete()
    #     if result:
    #         # print("The admin {name} was deleted successfully.".format(name=admin.full_name()))
    #         scribus.messageBox('Console simulation', "The admin {name} was deleted successfully.".format(name=admin.full_name()), scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    #     else:
    #         # print("There was an error deleting the admin.")
    #         scribus.messageBox('Console simulation', "There was an error deleting the admin.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)
    
    # else:
    #     # print("The ID of the admin was not found.")
    #     scribus.messageBox('Console simulation', "The ID of the admin was not found.", scribus.ICON_INFORMATION, scribus.BUTTON_OK)



main()
