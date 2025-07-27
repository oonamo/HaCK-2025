import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';

import socket from './socket'

import ConnectionStatus from './components/connect_status';
import LCD from './components/LCD_comm';

import SensorPanel from './components/sensors/sensor_panel'

import GPT from './components/gpt';

function App() {
  const [pictureStatus, setPictureStatus] = useState("");

  useEffect(() => {
    // socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });
    return () => {
      socket.off('picture_taken');
    };
  }, []);

  return (
    <>
      <div className="app">
        <div className="info-bar">
          <ConnectionStatus />
        </div>
        <SensorPanel />
        <div className="gpt-bar">
          <LCD />
          <GPT />
        </div>
      </div>
    </>
  );
}

export default App;
