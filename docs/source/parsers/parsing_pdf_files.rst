Parsing PDF Files
============

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

Content Types
-------------

The parsing process identifies several types of content in the PDF file. Here's a brief explanation of each type:

- `Email`: This type is used to identify email addresses in the text.
- `Title`: This type is used to identify titles or headings in the text.
- `ListItem`: This type is used to identify list items in the text.
- `NarrativeText`: This type is used to identify general body text or paragraphs.
- `Unknown`: This type is used when the content type cannot be determined.

The `parse` method will return one of these types for each piece of text content extracted from the PDF file.

FileReaderSource
----------------

The `FileReaderSource` class defines several constants that represent the different sources from which a PDF file can be read:

- `WEB_URL`: This source type is used when the PDF file is to be read from a web URL.
- `LOCAL`: This source type is used when the PDF file is to be read from a local file system.
- `S3`: This source type is used when the PDF file is to be read from an Amazon S3 bucket.
- `GOOGLE_DRIVE`: This source type is used when the PDF file is to be read from Google Drive.

The user can specify the source type when creating an instance of the `PdfParser` class. This is done by setting the `source` variable to one of the constants defined in the `FileReaderSource` class. For example, if the PDF file is to be read from a local file system, you would do the following:

.. code-block:: python

   source = FileReaderSource.LOCAL

This tells the `PdfParser` class to read the PDF file from a local file system. Similarly, you can set `source` to `FileReaderSource.WEB_URL`, `FileReaderSource.S3`, or `FileReaderSource.GOOGLE_DRIVE` to read the PDF file from a web URL, an Amazon S3 bucket, or Google Drive, respectively.

ParserMethod
------------

There are three types of ParserMethods supported:

1. **ParserMethod.FAST**: This method is the quickest way to parse PDF files. It directly reads the text embedded in the PDF.

2. **ParserMethod.OCR**: This method uses Optical Character Recognition to read the text from the PDF. It is slower than the FAST method but can read text from images and scanned documents.

3. **ParserMethod.MODEL**: This method uses a trained model to parse the PDF. It is the most accurate but also the slowest method.