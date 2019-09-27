# Python/Flask remote debuggin sample for Visual Studio Code

* This sample contains the completed program from the tutorial, make sure to visit the link: [Using Flask in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask). Intermediate steps are not included.
* It also contains the Dockerfile with `ptvsd` package necessary to run remote debugging in the Docker scenario.

## Navigation

The flask application `hello_app` is simple web application we are going to debug remotely with VSCode.

There 2 scenarios:
1. Invasive: we can init debug from the application (see commented section in the `hello_app/webapp`)
2. Transparrent: Run the application through the `ptvsd`
   1. Using `ptvsd` module
   2. Using the `launcher.py` in case some preparation work should be done.

## Steps

### Install VSCode with extensions

1. Follow the link [MS VSCode setup guide](https://code.visualstudio.com/docs/setup/setup-overview)
2. Install the python extension `ms-python.python`
3. Optional: Install the Docker extension `ms-azuretools.vscode-docker`
4. Advanced: VScode in Docker scenario extension (Code Insiders version of VSCode): `ms-vscode-remote.remote-containers`

### Build the image:

* Use `Terminal->Run Task->Build docker` task to create the image.
* Start image with `Terminal->Run Task->Start docker` task.
* Ensure it is started: it uses tcp ports mapped to the 5000 (webapp) and 3000 (debugger)

The output should be:
```
 * Serving Flask app "hello_app.webapp"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 ```

### Start debugging

* Set the breakpoint on some API controller in the `hello_app/views.py`
* Run the `Attach` launch configuration.
* Open the web app in the browser `http://localhost:5000` and hit the breakpoint.

## Additional details

* This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
* For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
* Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
