import { useState, useEffect } from 'react';

import io from 'socket.io-client';
const socket = io('http://localhost:8000');

export default function({ topic, className, units, transform }) {
  const [data, setData] = useState([])

  useEffect(() => {
    socket.on(topic, payload => {
      setData((data) => data.push(payload))
    })

    return () => {
      socket.off(topic)
    }
  }, [])

  return (
    <div className={className}>
      {
        data.length !== 0 ?
          data.map((val, i) => {
            <span className={topic} key={i}>
              {val}
            </span>
          })
          : ""
      }
    </div>
  )
}
