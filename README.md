# E6.9Fibonacci
# Python/Flask tutorial sample for Visual Studio Code

* This project contains the Dockerfile necessary to build a container with a development server. The resulting image works both locally and when deployed to Heroku App Service.

## Navigation

The `app.py` file, for its part, is specifically for deploying to Heroku App Service on Linux without containers. Because the app code is in its own *module* folder, trying to start the Gunicorn server within App Service on Linux produces an "Attempted relative import in non-package" error. The `app.py` file, therefore, is just a shim to import the app object from the `fib_handler` module, which then allows you to use startup:app in the Gunicorn command line (`gunicorn --bind=0.0.0.0 --workers=4 startup:app`).

Build container:
`docker-compose build`
`docker build -t E6.9Fibonacci .`
`docker-compose up`