import sublime, sublime_plugin, indentparser


class IndentToList(sublime_plugin.TextCommand):
    def run(self, edit):
        parser = indentparser.IndentTxtParser()
        #Get current selection
        sels = self.view.sel()
        selsParsed = 0
        if(len(sels) > 0):
            for sel in sels:
                #Make sure selection isn't just a cursor
                if(abs(sel.b - sel.a) > 0):
                    self.parseRegion(parser, sel, edit)
                    selsParsed += 1
        #All selections just cursor marks?
        if(selsParsed == 0):
            region = sublime.Region(0, self.view.size() - 1)
            self.parseRegion(parser, region, edit)

    def parseRegion(self, parser, region, edit):
        lines = self.view.line(region)
        text = self.view.substr(lines)
        indented = parser.parseText(text)
        newview = self.view.window().new_file()
        newview.insert(edit, 0, indented)
