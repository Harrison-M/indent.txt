# Indent.txt
Turn your indented notes into HTML

## How to use

### Sublime Text 2

See [indent.txt-sublime](http://github.com/Harrison-M/indent.txt-sublime)

### Command line

    python indenttxt.py inputfile outputfile
    
Parses inputfile using the Indent.txt parser and saves the result to outputfile

## Formatting
Examples of all formatting marks can be found in test.txt with the results in output.html

* Prefixing a line with a single asterisk (*) will wrap the item in an &lt;em&gt; tag
* Prefixing a line with two asterisks (**) will wrap the item in a &lt;strong&gt; tag
* Prefixing a line with two forward slashes (//) indicates a comment, excluding the line from the results.  This will eventually be used for metadata and parser instructions.

## Like Indent.txt?

[![endorse](http://api.coderwall.com/harrisonm/endorsecount.png)](http://coderwall.com/harrisonm)

## License
MIT

## Coming soon:
* More formatting
* Automatic table of contents
* Mark lines as Todo.txt items
