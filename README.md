# Web Interface for Sentinel Discord bot

This is a web server handling both frontend and backend for Sentinel Discord bot.
The web server is temporarily available at https://logs.itsuchur.dev domain.

CDN and proxy services are provided by Cloudflare.

Please note the traffic to the Flask server goes through NGINX proxy. Configuring NGINX is outside of the scope of 
this repository.

## Requirements

**To Windows users**: please note you can't actually launch this site using *gunicorn* as the module *fcntl* **is not** 
available for Windows users. Use any other server like *waitress* or build and run Docker container.

Make sure you have installed the following dependencies before proceeding.

- Python 3.8 or higher
- PostgresSQL

## Installation

1. **Clone this repository to your local machine.**
By entering the following command into your console.

```git clone https://github.com/itsuchur/logs.itsuchur.dev```

2. **Initialize a virtual environment** 

Use the following command to initialize venv.

```python -m venv logs.itsuchur.dev/venv```

3. **Activate the venv**

Use the following commmand to activate venv.

```source logs.itsuchur.dev/venv/bin/activate```

4. **Install the dependencies**

Install the required dependencies running the following command:

```pip install -r requirements.txt```

5 **Create .env file with credentials**.

Create a .env file with the following content:

``POSTGRES_PASSWORD=YourPassword``

6. **Launch the site**

``gunicorn -w 4 'app:app'``

## Building and running Docker container

**IMPORTANT**: if you choose this approach then you won't be able to use the reverse proxy setup.

If you prefer to use Docker please read the information below.

1. **Clone this repository to your local machine.**
By entering the following command into your console.

```git clone https://github.com/itsuchur/logs.itsuchur.dev```

2. **Change the directory** 

Change directory by using cd command

``cd logs.itsuchur.dev``

3 **Create .env file with credentials**.

Create a .env file with the following content:

``POSTGRES_PASSWORD=YourPassword``

4. **Build Docker image**

Use the following command to build Docker image

``docker build -t logs.itsuchur.dev .``

5. **Run a Docker container**

Use the following command to run the container from newly created Docker image

``docker run -t logs.itsuchur.dev``



