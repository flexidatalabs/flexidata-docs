Parsing Html Files
============

To parse Html files using flexidata, you need to import the necessary modules and classes from the flexidata library. Here's how you can do it:

.. code-block:: python

   from flexidata.parser.html import HtmlParser
   from flexidata.utils.constants import FileReaderSource, ParserMethod

Next, you need to create an instance of the :red:`HtmlParser` class. You can specify the file path, source, and whether to extract images or not in the constructor:

.. code-block:: python

   parser = HtmlParser(
       file_path="index.html",
       source=FileReaderSource.LOCAL,
       extract_image=False,
   )

Finally, you can parse the Html file by calling the :red:`parse` method on the parser object. This method returns a list of elements extracted from the Html file:

.. code-block:: python

   elements = parser.parse()

Each element in the returned list represents a piece of content extracted from the Html file.