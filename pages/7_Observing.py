
import streamlit as st # web development
import numpy as np # np mean, np random
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop
import plotly.express as px # interactive charts
import asyncio # tcp server

HOSTNAME = "frontend"
TCP_PORT = 50007

class TcpHelloObserver:
    
    def __init__(self):
        self.x = []
        self.y = []
        self.server = None
        self.__connected = False
    
    def parse_num(num_str):
        base = num_str[:num_str.find('*')]
        exponent = num_str[num_str.find('^')+1:]
        return float(base) * (2 ** int(exponent))

    def parse_data(message):
        # message is of form: "x_value: 1.2566366*2^0, y_value: 1.9316164*2^-1"
        parts = message.split(' ')
        return (TcpHelloObserver.parse_num(parts[1][:-1]), TcpHelloObserver.parse_num(parts[3]))

    async def __handle_connection(self, reader, writer):
        self.__connected = True
        while True:
            data = await reader.readline()
            if not data:
                break

            message = data.decode()
            if len(message) > 2: # if not an empty line
                point = TcpHelloObserver.parse_data(message)
                self.x.append(point[0])
                self.y.append(point[1])
            
            await asyncio.sleep(0) # pass control to main
        self.__connected = False

    async def start_server(self, hostname, portnum):
        self.server = await asyncio.start_server(
                self.__handle_connection, hostname, portnum)

    async def serve_connection(self):
        await self.server.start_serving()

    def is_connected(self):
        return self.__connected


class HelloWorldVisualizer:
    def __init__(self, container):
        self.container = container
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
    visualizer = HelloWorldVisualizer(st.container())

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
