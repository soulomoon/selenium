
import sys, os, time
from pywinauto import Desktop, Application
script_dir = os.path.join(os.getcwd(), os.path.dirname(sys.argv[0]))
os.chdir(script_dir)

Application().start(r'explorer.exe "' + script_dir + '"')

# connect to another process spawned by explorer.exe
app = Application(backend="uia").connect(path="explorer.exe", title="pywinauto_fork")

app.pywinauto_fork.set_focus()
appveyor = app.pywinauto.ItemsView.get_item('appveyor.yml')
appveyor.click_input()
appveyor.right_click_input()

app.ContextMenu.Properties.invoke()

# this dialog is open in another process (Desktop object doesn't rely on any process id)
Properties = Desktop(backend='uia').appveyor_yml_Properties
Properties.print_control_identifiers(depth=5)
Properties.Cancel.click()
Properties.wait_not('visible') # make sure the dialog is closed