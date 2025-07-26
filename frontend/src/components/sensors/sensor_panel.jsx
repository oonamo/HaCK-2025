import Humidity from './humidity';
import Temp from './temp';
import Light from './light';
import Ultrasonic from './ultrasonic';

import './sensor_panel.css'

export default function SensorPanels({ }) {
  return (
    <div className="sensor-panel-ctn">
      <Humidity />
      <Temp />
      <Light />
      <Ultrasonic />
    </div>
  )
}
