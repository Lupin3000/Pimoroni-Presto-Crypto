# Pimoroni-Presto Crypto Display

Simple example to show crypto prices on [Pimoroni-Presto](https://shop.pimoroni.com). You can find the repository and firmware releases [here](https://github.com/pimoroni/presto).

## Prerequisite

- Python installed
- latest [VCP driver]( https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads) installed (_depending on used OS_)

## Project setup

Clone the repository to your local environment.

```shell
# clone repository
$ git clone https://github.com/Lupin3000/Pimoroni-Presto-Crypto.git

# change into cloned directory
$ cd Pimoroni-Presto-Crypto/
```

Create Python virtualenv and install required packages.

```shell
# create virtual environment
$ python3 -m venv .venv

# list directory (optional)
$ ls -la

# activate virtual environment
$ .venv/bin/activate

# update pip (optional)
(.venv) $ pip3 install -U pip

# install wheel and rshell
(.venv) $ pip3 install wheel rshell
```

## Configuration

1. open `secrets.py` and add your values for **WIFI_SSID** and **WIFI_PASSWORD**.
2. open `main.py` and change constants **TARGET_CURRENCY** and **CRYPTO**

> **Note:** The free API _V1_ of [CoinCap](https://www.coincap.io) is used. Only 200 requests per minute are allowed.
> 
> This version return the prices in USD (_constant: **BASE_CURRENCY**_).
> To convert the currency, the API of [Frankfurter](https://frankfurter.dev) is used.

## Upload and run

Upload following directories and files to Pimoroni-Presto (_RP2350_) via `rshell`.

```shell
# start serial connection
(.venv) $ rshell -p [SERIAL PORT]

# upload to device
Pimoroni-Presto-Crypto> cp main.py /pyboard/
Pimoroni-Presto-Crypto> cp secrets.py /pyboard/
Pimoroni-Presto-Crypto> cp -r lib /pyboard/
Pimoroni-Presto-Crypto> cp -r fonts /pyboard/

# verify files on device (optional)
Pimoroni-Presto-Crypto> ls /pyboard/
```

## Run application via REPL

```shell
# start REPL
Pimoroni-Presto-Crypto> repl
```

- Press `control` + `d` for soft reboot.
- Press `control` + `c` to stop execution.
- Press `control` + `x` to leave the REPL.
