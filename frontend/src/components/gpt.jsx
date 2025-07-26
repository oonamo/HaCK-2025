import { useEffect, useState, useRef } from 'react'
import socket from '../socket'

export default function GPT() {
  const [hasPicture, setHasPicture] = useState(false)
  const [tts, setTTS] = useState(null)
  const [image, setImage] = useState(null)

  function playAudio() {
    const audio = new Audio(tts)
    audio.play()
  }

  useEffect(() => {
    if (tts) {
      playAudio()
    }
  }, [tts])

  useEffect(() => {
    socket.on("picture_taken", data => {
      console.log("picture taken!")
      if (data.success) {
        setHasPicture(true)
        setTTS(require("../tts.wav"))
        setImage(require("../downloaded_image.jpg"))
      }
    })
  }, [])

  function onClick() {
    socket.emit("take_picture")
  }

  return (
    <div>
      <button onClick={onClick}>GPT DO THING</button>
      {hasPicture && <img src={image} />}
    </div>
  )
}
