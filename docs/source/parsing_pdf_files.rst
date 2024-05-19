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

The `parse` method returns a list of elements, where each element is a dictionary representing a piece of content extracted from the PDF file. Here's an example of what an element might look like:

.. code-block:: json

   {
      "Type":"NarrativeText",
      "Text":"Extending Llama-3’s Context Ten-Fold Overnight",
      "metadata":{
         "file_path":"2404.19553v1.pdf",
         "languages":[
            "eng"
         ],
         "filetype":"application/pdf",
         "page_number":1,
         "bbox":[
            122.95,
            99.42961860000003,
            489.05269640000006,
            116.64501860000007
         ],
         "layout_height":792,
         "layout_width":612,
         "extraction_source":"pdfminer.six"
      }
   }

In this example, the "Type" field indicates the type of content (e.g., "NarrativeText"), the "Text" field contains the actual text content extracted, and the "metadata" field contains additional information about the content, such as the file path, detected languages, file type, page number, bounding box coordinates, layout dimensions, and the extraction source.