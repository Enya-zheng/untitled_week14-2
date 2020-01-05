from flask import escape

escape('This is a Request')

print(escape('This is a <Request>'))