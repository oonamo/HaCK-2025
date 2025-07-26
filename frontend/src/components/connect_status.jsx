import socket from '../socket';

import './connect.css'

import { useEffect, useState } from 'react';

export default function ConnectionStatus(props) {
  const [connected, setConnected] = useState(false)

  useEffect(() => {
    socket.on("connect", () => {
      console.log("connected!")
      setConnected(true)
    }
    )

    return () => socket.off("connect")
  })

  return (
    <div className={`connect-status ${connected ? "connected" : "disconnected"}`}>
      <div className="connect-dot" />
      <span className="connect-text">
        {connected ? "ACTIVE" : "DISCONNECTED"}
      </span>
    </div>
  )
}
