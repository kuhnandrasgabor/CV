# Docs

The CVs are stitched together from multiple Markdown files, each containing a section of the CV. 

You define the structure of it in the [cv_config.json](scripts/cv_config.json) file by defining the following:
* **language support:** the languages you want to support and their suffixes
* **profile name:** the name of the main body of a generated CV, such as "Programming-Oriented" or "Graphics-Oriented"
* **main profile body's content:** the sections of the CV where you can define content elements

A content-element has the following properties:
* `"file": "demo/included-file1"`
* **files:** relative path to the file that contains the content block we wish to use 
    * a path to the file that will be copied into the body of the CV if no content array is defined
* `"generate": "demo/linked-file-with-linked-content",`
* **generate:** instructs the code to generate a sub-document in the specified path
  * the contents will be content array elements
  * linked into the body of the CV and the content array will be used to generate a sub-document
* `"link": {
  "_en": "### [Link to linked-file1]",
  "_hu": "### [linked-file1 -re mutató link]"
  }`
* **links:** a dictionary, holding the text of the link button for each supported language, that is pointing to
    * either the file 
    * or the generated sub-document
    * the link is the first part of the Markdown text, so it can be used with Markdown formatting like hashtags, but needs to be in square brackets for the syntax to work properly 
      * (the link its*elf is calculated by the [combine.py](scripts/combine.py) script)
* `"content":[{"file": "demo/included-file3"},{"file": "demo/included-file4"}`
* **content:** an array of the content for the section used to
    * include multiple files
    * or build a subpage*

You can check out the [interactive demo md file](generated/demo_output_en.md) and it's [pdf version](generated/demo_output_en.pdf) to see how the content is structured.