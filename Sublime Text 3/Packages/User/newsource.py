import sublime, sublime_plugin, os
from datetime import datetime

class NewsourceCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    extension = os.path.splitext( self.view.file_name() )[1]
    head = "/**"
    foot = "*/\n\n"
    phone = "--"
    body = ""

    if extension == ".js":
      tech = "Javascript."
      version = "Javascript 1.7"
    elif extension == ".css":
      tech = "Web (CSS)."
      version = "CSS3."
    else:
      tech = "Web (HTML5)."
      version = "Standard Markup."
      head = "<!--"
      foot = "-->\n"
      phone = "- -"
      body = """\n<html>
  <head>
    <meta name="viewport" content="width=device-width initial-scale=1" charset="UTF-8">
    <title>New Web Page</title>
  </head>
  <body>
    
  </body>
</html>"""

    stamp = datetime.now().strftime("Date: %d/%m/%y, Time: %H:%M:%S.")
    heading = head + """\n* Engineered and developed by Jhonny Trejos Barrios.
* Technology: """ + tech + """
* Version: """ + version + """
* Development Environment: Sublime Text 3 [build 3126].
* """ + stamp + """\n*
* Additional Info.\n*\n* Source Code Target Or Details:
*
*              []
*
* Licenses: GNU GPL v3.0, Eclipse Public License 1.0, personal not for commercial purposes.
* Developer Contact: jtrejosb@live.com || jtrejosb@gmail.com || jtrejosb@icloud.com
* Mobile: """ + phone + """\n""" + foot + body

    

    self.view.insert( edit, 0, heading )















    # file = os.path.basename( self.view.file_name() )
# public class """ + os.path.splitext( file )[0] + " {\n  \n}"
#     for r in self.view.sel():
#       if r.empty():
#         self.view.insert (edit, r.a, heading)
#       else:
#         self.view.replace(edit, r, heading)
