import socket from '../socket';

import { useEffect, useState } from 'react';

import './lcd.css'

export default function LCD() {
  const [message, setMessage] = useState("")
  const [history, setHistory] = useState([])

  function sendMessage() {
    if (message.length <= 0) return;

    const timestamp = new Date().toLocaleTimeString();
    const newHistory = {
      message: message,
      timestamp: timestamp
    }
    console.log("new entry:", newHistory)

    setHistory((prev) => [...prev, newHistory])

    setMessage("")
  }

  useEffect(() => {
    console.log("Updated history:", history);
  }, [history]);

  return (
    <div className="lcd-comm">
      <div className="lcd-history">
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
        <input value={message} onChange={(e) => setMessage(e.target.value)} />
        <button className="lcd-text-btn" onClick={sendMessage}>Send</button>
      </div>
    </div>
  )
}
