# -*- coding: utf-8 -*-
from flask import Flask, request
from scipy.stats import norm
import numpy as np

HOST="127.0.0.1"
PORT="5000"

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world"

@app.route("/bs_api")
def bs_api():
    to_float = lambda x: float(request.args.get(x, "").encode("utf-8"))
    s0  = to_float("s0")
    k   = to_float("k")
    T   = to_float("T")
    r   = to_float("r")
    vol = to_float("vol")
    return str(call_price_bs(s0, k, T, r, vol))
    
#call option price by black-scholes model
def call_price_bs(s0, k, T, r, vol):
    d1 = (np.log(s0/k)+(r+0.5*(vol**2.0))*T) / (vol * np.sqrt(T))
    d2 = d1-vol*np.sqrt(T)
    return (s0*norm.cdf(d1) - k*np.exp(-r*T)*norm.cdf(d2))

if(__name__ == '__main__'):
    app.run(host=HOST,port=int(PORT))