import indentparser
import argparse


argHandler = argparse.ArgumentParser(
    description="Convert an indented notes file to HTML.")
argHandler.add_argument('inputfile', metavar='inputfile.txt', type=str,
                        help='File to parse')
argHandler.add_argument('outputfile', metavar='outputfile.html', type=str,
                        help='Output file')

parser = indentparser.IndentTxtParser()
args = argHandler.parse_args()
outFile = open(args.outputfile, "w")
outFile.write(parser.parseFile(args.inputfile))
outFile.close()
