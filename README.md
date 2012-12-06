# Indent.txt
Turn your indented notes into HTML

## How to use

### Sublime Text 2
1. Place this repository's folder in your Sublime Packages folder ([Sublime Package Control](http://wbond.net/sublime_packages/package_control) support coming soon)
2. Run the "Indent.txt: Parse" command from the command palette (Ctrl-Shift-P) on a file or selection from a file
3. The resulting HTML will open in a new tab.

### Command line

    python indenttxt.py inputfile outputfile
    
Parses inputfile using the Indent.txt parser and saves the result to outputfile

## Formatting
Examples of all formatting marks can be found in test.txt with the results in output.html

* Prefixing a line with a single asterisk (*) will wrap the item in an &lt;em&gt; tag
* Prefixing a line with two asterisks (**) will wrap the item in a &lt;strong&gt; tag

## Like Indent.txt?

[![endorse](http://api.coderwall.com/harrisonm/endorsecount.png)](http://coderwall.com/harrisonm)

## License
MIT

## Coming soon:
* More formatting
* Automatic table of contents