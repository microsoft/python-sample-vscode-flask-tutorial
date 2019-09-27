# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
from . import views  # For import side-effects of setting up routes.

## SCENARIO 1 (invasive):
## Uncomment this in case process started without ptvsd runner:
## Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
#print('Started debug version http://localhost:5000/')
#import ptvsd
## Allow other computers to attach to ptvsd at this IP address and port.
#ptvsd.enable_attach(address=('0.0.0.0', 3000), redirect_output=True)
## Pause the program until a remote debugger is attached
#ptvsd.wait_for_attach()
