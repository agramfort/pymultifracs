.. -*- mode: rst -*-

|Codecov|_ |Binder|_ |CircleCI|_

.. |Codecov| image:: https://codecov.io/gh/neurospin/pymultifracs/branch/master/graph/badge.svg
.. _Codecov: https://codecov.io/gh/neurospin/pymultifracs

.. |Binder| image:: https://mybinder.org/badge_logo.svg
.. _Binder: https://mybinder.org/v2/gh/neurospin/pymultifracs/master

.. |CircleCI| image:: https://circleci.com/gh/neurospin/pymultifracs.svg?style=svg
.. _CircleCI: https://circleci.com/gh/neurospin/pymultifracs



Introduction
============

This package implements wavelet based multifractal analysis of 1D signals.

Implemented features:

* Computation of (1D) multiresolution quantities: wavelet coefficients, wavelet-leaders and p-leaders
* Computation of structure functions, cumulants and log-cumulants.
* Estimation of the multifractal spectrum.


The code in this package is based on the Wavelet p-Leader and Bootstrap based MultiFractal analysis (PLBMF) Matlab toolbox written by Patrice Abry, Herwig Wendt and colleagues
(http://www.ens-lyon.fr/PHYSIQUE/Equipe3/MultiFracs/software.html). For a thorough introduction to multifractal analysis, you may access H. Wendt's PhD thesis available in his webiste at
https://www.irit.fr/~Herwig.Wendt/data/ThesisWendt.pdf).


For a brief introduction to multifractal analysis, see the file THEORY.ipynb

There are two ways to install this package: either by using a package manager to install the package only, which will make
the code only usable as an import,
or by cloning the repository first, and then installing the package which will make it editable

Installing the package only
===========================

Using conda
-----------

Creating a new environment (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

    wget https://raw.githubusercontent.com/neurospin/pymultifracs/master/env.yml
    conda env create -f env.yml

Installing into a pre-existing environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that this package requires a recent version of python (>=3.7)

.. code:: shell

    wget https://raw.githubusercontent.com/neurospin/pymultifracs/master/env.yml
    conda env update -f env.yml --name $ENVNAME

----

Using pip
---------

.. code:: shell

    pip install git+https://github.com/neurospin/pymultifracs.git@master


Cloning the whole repository (including examples)
=================================================

Using conda
-----------

Using conda, the simplest way to proceed is to use the :code:`meta.yml` file to create or update
an environment, and then install the editable local version of pymultifracs on top.

Creating a new environment (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

    git clone https://github.com/neurospin/pymultifracs.git@master
    conda env create -f pymultifracs/meta.yml
    pip install -e pymultifracs

Installing into a pre-existing environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that this package requires a recent version of python (>=3.7)

.. code:: shell

    git clone https://github.com/neurospin/pymultifracs.git@master
    conda env update -f pymultifracs/meta.yml --name $ENVNAME
    pip install -e pymultifracs

----

Using pip
---------

.. code:: shell

    git clone https://github.com/neurospin/pymultifracs.git@master
    pip install -e pymultifracs

See the examples/ folder, mainly examples/Demo.ipynb and examples/Maquette.ipynb
