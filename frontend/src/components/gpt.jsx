import { useEffect, useState, useRef } from 'react'
import socket from '../socket'

import { FaRedoAlt, FaCamera } from 'react-icons/fa';

import ChatGPT from '../chat-gpt.png'

export default function GPT() {
  const [hasPicture, setHasPicture] = useState(false)
  const [tts, setTTS] = useState(null)
  const [image, setImage] = useState(null)
  const [playingAudio, setPlayingAudio] = useState(null)

  function playAudio() {
    if (playingAudio) {
      console.log("audio!")
      playingAudio.pause()
    }

    const audio = new Audio(tts)
    setPlayingAudio(audio)
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
    // socket.emit("picture_taken", { "success": true })
    // console.log("click!")
    // setHasPicture(true)
    // setTTS(require("../tts.wav"))
    // setImage(require("../downloaded_image.jpg"))
  }

  return (
    <div className="inline">
      <button onClick={onClick} className="gpt-call">
        INVOKE RECIEVE.PY
      </button>
      {hasPicture && (
        <div className="gpt-img-ctn">
          <button className="gpt-audio" onClick={playAudio}>
            <FaRedoAlt size={30} />
          </button>
          <img src={image} className="gpt-img" onClick={playAudio} />
        </div>
      )}
    </div>
  )
}
