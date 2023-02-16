
import streamlit as st # web development
import numpy as np # np mean, np random
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop
import plotly.express as px # interactive charts

import asyncio #running coroutines
from tflm_hello_world.tcp_hello_observer import TcpHelloObserver

HOSTNAME = "frontend"
TCP_PORT = 50007


class HelloWorldVisualizer:
    def __init__(self):
        self.plot = st.empty()
        self.datagram = st.empty()

    def render(self, x, y):
        x = x[-40:]
        y = y[-40:]
        data = pd.DataFrame(data={"X value":x, "Y value":y})
        fig = px.scatter(data, x="X value", y="Y value")
        self.plot.write(fig)
        self.datagram.write(data)


async def main():
    obs = TcpHelloObserver()
    await obs.start_server(HOSTNAME, TCP_PORT)

    conn_text = st.text("")
    visualizer = HelloWorldVisualizer()

    async with obs.server:
        while True:
            await obs.serve_connection()
            if obs.is_connected():
                conn_text.text("HelloWorld Connected!")
            else:
                conn_text.text("Waiting for connection...")
            
            visualizer.render(obs.x, obs.y)
            await asyncio.sleep(1)


asyncio.run(main())
