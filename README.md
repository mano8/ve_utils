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

First you need import one of the utils package egg :

``from ve_utils.utils import UType as Ut``

Now, for example you can use is_list method as fallow:

    $> my_var = [ 0, 1 ,2 ,3 ]
    $> Ut.is_list(my_var, not_null=True)
    $> True
    $> Ut.is_list(my_var, min_items=5)
    $> False
    $> Ut.is_list(my_var, max_items=2)
    $> False 
    $> Ut.is_list([], not_null=True)
    $> False 
