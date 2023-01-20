# Description

`Bitlyapi` is the console tool to communicate with `Bitly.com` service API. 

Main tool features are: 
+ make short links from fully URL given by the user
+ make bitlinks calculations after it being clicked


# Prerequisites

Firstly, you have to install package `python3-venv` to work with python virual environment.

Update packages on your system `!(it depends on your operating system)`

in this document I use Ubuntu as my operating system. So run update:
```console
$ sudo apt update
```

and run command:
```console
$ sudo apt install -y python3-venv
```

Then jump to project folder:
```console
$ cd bitlyapi
```

and create new python environment to run the code:
```console
$ python3 -m venv venv
```

Activate new virtual environment:
```console
$ source venv/bin/activate
```

As a result, you will see command line prompt like this:
```console
(venv) bitlyapi $ 
```

Next step you have to create your personal text file `.env` file in the `bitlyapi` folder:
```console
(venv) bitlyapi $ touch .env
```

Fill `.env` file with your personal bitly-API token:

```console
(venv) bitlyapi $ echo 'BITLY_TOKEN=xxxxxxxxxxxxx' > .env
```

Instead of `BITLY_TOKEN=xxxxxxxxxxxxx` initialize BITLY_TOKEN value by your personal token value you got after bitly.com registration

# Install dependencies

In the virtual environment run command:

```console
(venv) bitlyapi $  pip install -r requirements.txt
```

This command install `requests` and `python-dotenv` library in  the `venv` virtual environment.

# Run program 

    (venv) bitlyapi $ python bitlyapi.py

# Control results

If program running successfully, you will see result like this:

![Alt text](img/img1.png?raw=true "Bitly output")


# Final steps

Deactivate virtual environment:

```console
(venv) bitlyapi $ deactivate
```

Close console:
```console
$ exit
```