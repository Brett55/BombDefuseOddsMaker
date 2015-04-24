Fibonacci GettR
===============

A simple web app that calculates the nth position in the Fibonacci sequence!


On MAC OSX
----------
Requirements: Docker and Docker-Compose

You can setup on both here: `https://docs.docker.com/compose/install/`

Step 1

    $ git clone https://github.com/Brett55/FibonacciGettR

Step 2

    $ cd FibonacciGettR

Step 3

	$ boot2docker start

Step 4

	$ boot2docker ip //write this down

Step 5

	$ docker-compose up

Step 6

Now go to `<your container's ip>:8000` in your browser

Example:

`http://192.168.59.103:8000/'

RESTful API
----------

###'GET' Syntax for API:

`<your container's ip>:8000/v1/calculate/<nThPosition>/<SeedValue1>/<SeedValue2>/`

Example:

`http://192.168.59.103:8000/6/1/1/'

returns

`Result: 8 Finished in 0.0001`


###'POST' Syntax for API:

`<your container's ip>:8000/v1/calculate_and_save/`

Example:

`http://192.168.59.103:8000/6/'

Request object params:
	`{ user_input: <nthPosition> }`

returns

`Result: 8 Finished in 0.0001`


