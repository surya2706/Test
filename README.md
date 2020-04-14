# Test-Script

This is a python script that fetches the Company Name on providing the Mac Address as command line argument.

- Clone the Project using `git clone https://github.com/surya2706/Test.git`
- Open the terminal and `cd` into the cloned directory.
- Run the command `docker build -t cisco-test:0.1 .` to build the docker image. (Make sure that Docker is installed in your machine)
- Now run the docker container by entering the command with appropriarte mac address`docker run cisco-test:0.1 <mac_address>`. (`mac_address` for which the Company Name is to be fetched)
- The python script will execute and return the `Company name` if the entered mac address is correct.
- If the entered mac address is incorrect, then you will get a response `Sorry, there is an Error. Check the mac address.`

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
```

# Note

- The `Dockerfile` file contains the code to build the docker image.
- The python source course resides inside the `main` folder.
- `api_helper.py` file contains the `ApiHelper` python class which fetches the response from the url.
- `conf.py` file is the configuration file that contains the static variables such as `api_key` and `url`. (`api_key` is obtained by signing into the `https://https://macaddress.io/`)
- `main.py` file is the one which is executed on running the docker container.
