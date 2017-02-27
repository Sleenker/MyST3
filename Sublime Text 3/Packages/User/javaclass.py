import sublime, sublime_plugin, os
from datetime import datetime

class JavaclassCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    file = os.path.basename( self.view.file_name() )
    stamp = datetime.now().strftime("Date: %d/%m/%y, Time: %H:%M:%S.")
    heading = """\n\n/**\n* Engineered and developed by Jhonny Trejos Barrios.
* Technology: Java.
* Version: Java Development Kit 1.8.0_31, Standard Edition.
* Development Environment: Sublime Text 3 [build 3126].
* """ + stamp + """\n*
* Additional Info.\n*\n* Source Code Target Or Details:
*
*              []
*
* Licenses: GNU GPL v3.0, Eclipse Public License 1.0, personal not for commercial purposes.
* Developer Contact: jtrejosb@live.com || jtrejosb@gmail.com || jtrejosb@icloud.com
* Mobile: --
*/

public class """ + os.path.splitext( file )[0] + " {\n  \n}"
    for r in self.view.sel():
      if r.empty():
        self.view.insert (edit, r.a, heading)
      else:
        self.view.replace(edit, r, heading)
