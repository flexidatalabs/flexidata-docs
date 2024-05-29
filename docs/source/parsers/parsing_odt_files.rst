Parsing odt Files
============

To parse odt files using flexidata, you need to import the necessary modules and classes from the flexidata library. Here's how you can do it:

.. code-block:: python

   from flexidata.parser.odt import OdtParser
   from flexidata.utils.constants import FileReaderSource, ParserMethod

Next, you need to create an instance of the :red:`OdtParser` class. You can specify the file path, source, and whether to extract images or not in the constructor:

.. code-block:: python

   parser = OdtParser(
       file_path="example.odt",
       source=FileReaderSource.LOCAL,
       extract_image=False,
   )

Finally, you can parse the odt file by calling the :red:`parse` method on the parser object. This method returns a list of elements extracted from the odt file:

.. code-block:: python

   elements = parser.parse()

Each element in the returned list represents a piece of content extracted from the odt file.