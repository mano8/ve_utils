# ve-utils
This is a Python utilities library helper. Contain methods shared by multiple repositories.

# Installation

#### Install from PyPi :
You can install the ve_utils helper from PyPI:

``pip install ve_utils``

#### Install from github repository :
To install directly from GitHub:

``$ python3 -m pip install "git+https://github.com/mano8/ve_utils"``

# How to use

First you need import one of the utils package egg :

``from ve_utils.utils import UType as U``

Now, for example if you need to test if variable contain an non empty list you can use :

    > my_var = [ 0, 1 ,2 ,3 ]
    > U.is_list_not_empty(my_var)
    > True
    > my_var = 2
    > U.is_list_not_empty(my_var)
    > False 

The ``is_list_not_empty`` method is the same of using ``isinstance(my_var, list) and len(my_var) > 0``.