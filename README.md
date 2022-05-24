# ve-utils
This is a Python utilities library helper. Contain methods shared by multiple repositories.

# Installation

#### Install from PyPi :
You can install the ve_utils helper from PyPI:

``python -m pip install ve_utils``

#### Install from github repository :
Open Git bash or install it from [here](https://git-scm.com/downloads).

Go to the current directory where you want the cloned directory to be added.

``cd ~/my-repo/``

And clone the ve-utils repository :

``git clone https://github.com/mano8/utils.git``

Open new console and go to the current directory where you clone utils repository

``cd ~/my-repo/utils``

If you use python virtual environment egg anaconda,
``conda activate my_env``

Now you can install the package via python command :

``python setup.py install``

# How to use

First you need import one of the utils package egg :

``from utils.utils import UType as U``

Now, for example if you need to test if variable contain an non empty list you can use :

    > my_var = [ 0, 1 ,2 ,3 ]
    > U.is_list_not_empty(my_var)
    > True
    > my_var = 2
    > U.is_list_not_empty(my_var)
    > False 

The ``is_list_not_empty`` method is the same of using ``isinstance(my_var, list) and len(my_var) > 0``.