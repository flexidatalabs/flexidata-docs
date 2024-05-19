Usage
=====

.. _installation:

Installation
------------

To use flexidata, first install it using pip:

.. code-block:: console

   (.venv) $ pip install flexidata

Parsing PDF Files
-----------------

To parse PDF files using flexidata, you need to import the necessary modules and classes from the flexidata library. Here's how you can do it:

.. code-block:: python

   from flexidata.parser.pdf import PDFParser
   from flexidata.utils.constants import FileReaderSource, ParserMethod

Next, you need to create an instance of the `PDFParser` class. You can specify the file path, source, parsing method, and whether to extract images or not in the constructor:

.. code-block:: python

   parser = PDFParser(
       file_path="2404.19553v1.pdf",
       source=FileReaderSource.LOCAL,
       method=ParserMethod.FAST,
       extract_image=False,
   )

Finally, you can parse the PDF file by calling the `parse` method on the parser object. This method returns a list of elements extracted from the PDF file:

.. code-block:: python

   elements = parser.parse()

Each element in the returned list represents a piece of content extracted from the PDF file.



