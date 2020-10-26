from hello_app.webapp import app
pycon = {2016: "Portland", 2018: "Cleveland"}
europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}
print({**pycon, **europython})