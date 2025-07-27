import { useState, useEffect, useRef } from 'react';
import socket from '../../socket';

import './sensor.css'

export default function({ topic, className, units, transform }) {
  const [data, setData] = useState([])
  const containerRef = useRef(null)

  useEffect(() => {
    socket.on(topic, payload => {
      if (payload) {
        console.log("called topic:", topic)
        // setData((data) => data.push(payload))
        const timestamp = new Date().toLocaleTimeString();

        const newData = {
          message: payload,
          timestamp
        }

        setData(prev => [...prev, newData])
      }
    })

    return () => {
      socket.off(topic)
    }
  }, [])

  useEffect(() => {
    const container = containerRef.current

    if (container) {
      container.scrollTop = container.scrollHeight
    }
  }, [data]);

  return (
    <div className="sensor-ctn">
      <div className="sensor-name">
        <span>{topic}</span>
      </div>
      <div className="sensor-content" ref={containerRef}>
        {
          data.map((val, i) => (
            <div className="sensor-entry" key={i}>
              <span className="sensor-time">
                {val.timestamp}
              </span>
              {val.message}
            </div>
          ))
        }
      </div>
    </div>
  )
}
