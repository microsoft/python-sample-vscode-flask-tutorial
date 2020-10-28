# Python Azure DevOps (Santiago Gonzalez A @locoalien)

<<<<<<< HEAD
* This sample contains the completed program from the tutorial, make sure to visit the link: [Using Flask in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask). Intermediate steps are not included.
* It also contains the Dockerfile and uwsgi.ini files necessary to build a container with a production server. The resulting image works both locally and when deployed to Azure App Service. See [Deploy Python using Docker containers](https://code.visualstudio.com/docs/python/tutorial-deploy-containers).
* To run the app:
  1. Run the command `cd hello_app`, to change into the folder that contains the Flask app.
  1. Run the command `set FLASK_APP=webapp` (Windows cmd) or `FLASK_APP=webapp` (macOS/Linux) to point to the app module.
  1. Start the Flask server with `flask run`.

## The startup.py file

In the root folder, the `startup.py` file is specifically for deploying to Azure App Service on Linux without using a containerized version of the app (that is, deploying the code directly, not as a container).

Because the app code is in its own *module* in the `hello_app` folder (which has an `__init__.py`), trying to start the Gunicorn server within App Service on Linux produces an "Attempted relative import in non-package" error.

The `startup.py` file, therefore, is a shim to import the app object from the `hello_app` module, which then allows you to use startup:app in the Gunicorn command line (see `startup.txt`).
=======


* Derechos de autor  Ver [New Inntech](https://www.newinntech.com).
* Proyecto donde se muestra como realizar un Pipeline d DevOps en Microsoft Azure. Analisis de codigo estatico, pruebas de cobertura, analisis de vulnerabilidadees, SonarQube, integracion con AWS CodeCommit.
>>>>>>> master

