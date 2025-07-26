import { useState, useEffect } from 'react';
import socket from '../../socket';

import './sensor.css'

export default function({ topic, className, units, transform }) {
  const [data, setData] = useState([])

  useEffect(() => {
    socket.on(topic, payload => {
      if (payload) {
        // setData((data) => data.push(payload))
        const timestamp = new Date().toLocaleTimeString();
        console.log("data", data)

        setData(data => {
          data.push({ message: payload, timestamp })
        })
      }
    })

    return () => {
      socket.off(topic)
    }
  }, [])

  return (
    <div className="sensor-ctn">
      <div className="sensor-name">
        <span>{topic}</span>
      </div>
      <div className="sensor-content">
        {
          Array.isArray(data) && data.length !== 0 ?
            data.map((val, i) => {
              <div className="sensor-entry" key={i}>
                <span className="sensor-time">
                  {val.timestamp}
                </span>
                {val.message}
              </div>
            })
            : ""
        }
      </div>
    </div>
  )
}
