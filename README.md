# ve-utils
[![CircleCI](https://circleci.com/gh/mano8/ve_utils.svg?style=svg)](https://app.circleci.com/pipelines/github/mano8/ve_utils)
[![PyPI package](https://img.shields.io/pypi/v/ve_utils.svg)](https://pypi.org/project/ve_utils/)
[![codecov](https://codecov.io/gh/mano8/ve_utils/branch/master/graph/badge.svg?token=ADZ070QHDR)](https://codecov.io/gh/mano8/ve_utils)   

This is a Python utilities library helper. Contain methods shared by multiple repositories.

# Installation

#### Install from PyPi :
You can install the ve_utils helper from PyPI:

``pip install ve_utils``

#### Install from GitHub repository :
To install directly from GitHub:

``$ python3 -m pip install "git+https://github.com/mano8/ve_utils"``

# How to use

### UType :
import package :

``from ve_utils.utype import UType as Ut``

#### Test format :
Example for is_list method:

    $> my_var = [ 0, 1 ,2 ,3 ]
    $> Ut.is_list(my_var, not_null=True)
    $> True
    $> Ut.is_list(my_var, min_items=5)
    $> False
    $> Ut.is_list(my_var, max_items=2)
    $> False 
    $> Ut.is_list([], not_null=True)
    $> False 
    $> Ut.is_list([])
    $> True 
    $> Ut.is_list(dict())
    $> False 

The methods ```is_list, is_dict and is_tuple ``` takes the sames arguments.

Example for is_int method:

    $> my_var = 10
    $> Ut.is_int(my_var, not_null=True)
    $> True
    $> Ut.is_int(my_var, mini=15)
    $> False
    $> Ut.is_int(my_var, maxi=2)
    $> False 
    $> Ut.is_int(0, not_null=True)
    $> False 
    $> Ut.is_int(-10, not_null=True)
    $> True 
    $> Ut.is_int("hello")
    $> False 

The methods ```is_int, is_float and is_numeric ``` takes the sames arguments.
``is_numeric`` method allow to work with float and int instances.
