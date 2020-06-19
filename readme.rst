pysfmov
=======

SFMOV File Reader
-----------------
This module allows to get raw data and meta data from .sfmov image sequences.
We developed this module while working on images recorded from FLIR thermal camera.

Installing this package
-----------------------

.. code-block:: console
    $ pip install pyNNST


Simple examples
---------------
.. code-block:: python

      # Import packages 
      import pysfmov 

      filename = './data/rec.sfmov' #set the path and the filename

      data = pysfmov.get_data(filename) # get data from sfmov file
      meta_data = pysfmov.get_meta_data(filename) # get meta data from sfmov file



Reference:
<https://www.sciencedirect.com/science/article/pii/S0142112320301924>
