# Python Sample Code

This is a python project that provides the REST API to fetch the Company Name on providing the Mac Address as argument.

- Clone the Project using `git clone https://github.com/surya2706/Test.git`
- Open the terminal and `cd` into the cloned directory.
- Run the command `docker build -t cisco-test .` to build the docker image. (Make sure that Docker is installed in your machine)
- Now run the docker container by entering the command with appropriarte mac address`docker run -p 5000:5000 cisco-test`.
- The python project will execute and run on `http://0.0.0.0:5000/`.

#### REST API implementation

##### Endpoint: `/mac_address/<mac_address>`

##### Method: `GET`

##### Success Response:

```
{
    "success": true,
    "companyName": "Apple, Inc"
}
```

##### Error Response:

```
{
    "success": false,
    "error": "Please check the mac address"
}
```

The folder structure is

```
project
│   README.md
│   Dockerfile
|   .gitigore
│
└─── main
│   |   api_helper.py
│   │   conf.py
│   │   main.py
|   |   requirements.txt
|   └─── service
|   |   |   mac_service.py
```

# Note

- The `Dockerfile` contains the code to build the docker image.
- The python source code resides inside the `main` folder.
- `api_helper.py` inside main directory contains the `ApiHelper` python class which fetches the response from the url.
- `conf.py` inside main directory is the configuration file that contains the static variables such as `api_key`. (`api_key` is obtained by signing into the `https://https://macaddress.io/`)
- `requirements.txt` lists down all the required packages to install on the environment before running the project.
- `mac_service.py` inside `service` directory fetches the response by invoking the `ApiHelper` class's `get` method with `url` and `header` as parameters.
- `main.py` inside main directory is the one which is executed on running the docker container.

##### Security

- `JWT Token Based Authentication` can be used to secure this application in order to provide access to resources only for Authorized users. The authorized users will be verified and provided with an `AccessToken` on their login and this token will be passed in the `HEADER` on each subsequent requests. The token will be verified on each and every requests for their validity and then the resources are provided as response. The Token will be destroyed on logout which will then restrict the access to resources. The token can also have a expire time which enables the server to verify the token's lifetime and send response accordingly.
