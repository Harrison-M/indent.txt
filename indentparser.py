import re
import cgi


class IndentTxtParser:
    def parseFile(self, filename):

        #Init
        inputFile = open(filename, "rU")
        output = self.parse(inputFile)
        inputFile.close()
        return output

    def parseText(self, text):
        return self.parse(text.split("\n"))

    def parse(self, iterable):
        indentLevel = 0
        output = "<!doctype html>\n<html>\n<body>\n<ul>\n"

        #Compile our regex for reuse
        indentRE = re.compile("^(\t|    )")
        lineNum = 0

        for line in iterable:
            lineNum += 1
            newIndentLevel = 0
            while(indentRE.match(line)):
                line = indentRE.sub("", line)
                newIndentLevel += 1
            indentDiff = newIndentLevel - indentLevel
            #Indent
            if(indentDiff >= 1):
                output += "\n<ul>\n"
                #Need to go down additional levels
                for i in range(indentDiff - 1):
                    output += "<li>\n<ul>\n"
            #Outdent
            elif(indentDiff <= -1):
                output += "</li>\n"
                for i in range(abs(indentDiff)):
                    output += "</ul>\n</li>\n"
            #Samedent
            else:
                output += "</li>\n"

            #Format line
            prefix = ""
            suffix = ""
            #Emphasis
            if(line.find("*") == 0):
                #strong
                if(line.find("**") == 0):
                    prefix = "<strong>"
                    suffix = "</strong>"
                    line = line[2:]
                #em
                else:
                    prefix = "<em>"
                    suffix = "</em>"
                    line = line[1:]
            output += "<li>" + prefix + cgi.escape(line) + suffix
            indentLevel = newIndentLevel
        #Tie up loose ends
        if(len(iterable) > 0):
            output += "</li>\n"
        for level in range(indentLevel):
            output += "</ul>\n</li>\n"
        output += "</ul>\n</body>\n</html>"
        return output
