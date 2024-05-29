Parsing image Files
============

To parse image files using flexidata, you need to import the necessary modules and classes from the flexidata library. Here's how you can do it:

.. code-block:: python

   from flexidata.parser.image import ImageParser
   from flexidata.utils.constants import FileReaderSource, ParserMethod

Next, you need to create an instance of the :red:`ImageParser` class. You can specify the file path, source, parsing method and whether to extract images or not in the constructor:

.. code-block:: python

   parser = ImageParser(
       file_path="Tutorial-HolePunch-02.jpg",
       source=FileReaderSource.LOCAL,
       extract_image=False,
       method=ParserMethod.OCR
   )

Finally, you can parse the image file by calling the :red:`parse` method on the parser object. This method returns a list of elements extracted from the image file:

.. code-block:: python

   elements = parser.parse()

Each element in the returned list represents a piece of content extracted from the image file.