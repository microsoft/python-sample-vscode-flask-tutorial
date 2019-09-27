# Pull a pre-built alpine docker image with nginx and python3 installed
#FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
#ARG USERNAME=alex
# On Linux, replace with your actual UID, GID if not the default 1000
#ARG USER_UID=1000
#ARG USER_GID=$USER_UID
# Create the user
# RUN addgroup -g "$USER_GID" "$USERNAME" \
#     && adduser \
#     -D \
#     -g "" \
#     -h "/home/$USERNAME" \
#     -G "$USERNAME" \
#     -u "$USER_UID" \
#     "$USERNAME" && \
#     mkdir -p /home/$USERNAME/.vscode-server /home/$USERNAME/.vscode-server-insiders \
#     && chown ${USER_UID}:${USER_GID} /home/$USERNAME/.vscode-server* \
#     && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
#     && chmod 0440 /etc/sudoers.d/$USERNAME

RUN apk add --no-cache --update sudo python3-dev  gcc build-base
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -U pylint

# Set the default user
#USER $USERNAME
#ENV HOME="/home/${USERNAME}"
# Set the port on which the app runs; make both values the same.
#
# IMPORTANT: When deploying to Azure App Service, go to the App Service on the Azure
# portal, navigate to the Applications Settings blade, and create a setting named
# WEBSITES_PORT with a value that matches the port here (the Azure default is 80).
# You can also create a setting through the App Service Extension in VS Code.
ENV LISTEN_PORT=5000
EXPOSE ${LISTEN_PORT}
EXPOSE 3000


# Indicate where uwsgi.ini lives
ENV UWSGI_INI uwsgi.ini

# Tell nginx where static files live. Typically, developers place static files for
# multiple apps in a shared folder, but for the purposes here we can use the one
# app's folder. Note that when multiple apps share a folder, you should create subfolders
# with the same name as the app underneath "static" so there aren't any collisions
# when all those static files are collected together.
ENV STATIC_URL /hello_app/static

# Set the folder where uwsgi looks for the app
WORKDIR /hello_app
#RUN pip install --upgrade ptvsd
# Copy the app contents to the image
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY . /hello_app

# If you have additional requirements beyond Flask (which is included in the
# base image), generate a requirements.txt file with pip freeze and uncomment
# the next three lines.
ENV PYTHONIOENCODING=UTF-8
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP hello_app.webapp

# python -m ptvsd --host 0.0.0.0 --port 3000 -m flask run --no-debugger --no-reload --port=5000 --host=0.0.0.0
ENTRYPOINT [ "/bin/sh","-c","python -m ptvsd --host 0.0.0.0 --port 3000 -m flask run --no-debugger --no-reload --port=5000 --host=0.0.0.0" ]
# or using own wrapper (it is an example, add additional init logic)
# ENTRYPOINT [ "/bin/sh","-c","python launch.py --host 0.0.0.0 --port 3000 -m flask run --no-debugger --no-reload --port=5000 --host=0.0.0.0" ]
