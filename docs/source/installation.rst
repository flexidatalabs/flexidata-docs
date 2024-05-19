Installation
------------

To use flexidata, first install it using pip:

.. code-block:: console

   (.venv) $ pip install flexidata

While using the flexidata package, if you encounter an error like `ImportError: libGL.so.1: cannot open shared object file: No such file or directory` from `rapidocr_onnxruntime import RapidOCR`, it indicates that some additional packages are required. You can install these using the following commands:

.. code-block:: console

   $ sudo apt-get update
   $ sudo apt-get install libgl1-mesa-glx

These commands will update your package lists and install the `libgl1-mesa-glx` package, which is required by `rapidocr`.