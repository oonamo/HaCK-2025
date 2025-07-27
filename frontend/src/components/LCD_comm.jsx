import socket from '../socket';

import { useEffect, useState, useRef } from 'react';

import './lcd.css'

export default function LCD() {
  const [message, setMessage] = useState("")
  const [history, setHistory] = useState([])
  const containerRef = useRef(null)

  function sendMessage() {
    if (message.length <= 0) return;

    const timestamp = new Date().toLocaleTimeString();
    const newHistory = {
      message: message,
      timestamp: timestamp
    }
    console.log("new entry:", newHistory)

    setHistory((prev) => [...prev, newHistory])

    socket.emit("display", message)

    setMessage("")
  }

  useEffect(() => {
    console.log("Updated history:", history);

    const container = containerRef.current

    if (container) {
      container.scrollTop = container.scrollHeight
    }
  }, [history]);

  return (
    <div className="lcd-comm">
      <div className="lcd-console">
        <span>Console</span>
      </div>
      <div className="lcd-history" ref={containerRef}>
        {
          history.map((val, i) =>
          (
            <div className="lcd-history-entry" key={i}>
              <span className="lcd-time">
                {val.timestamp}
              </span>
              {val.message}
            </div>)
          )
        }
      </div>
      <div className="lcd-chat">
        <input value={message} onChange={(e) => setMessage(e.target.value)} onKeyPress={(e) => e.key == "Enter" && sendMessage()} />
        <button className="lcd-text-btn" onClick={sendMessage}>Send</button>
      </div>
    </div>
  )
}
