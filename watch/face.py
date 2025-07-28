import time
from math import cos, sin
from ssd1306 import SSD1306_I2C
from machine import I2C, Pin

DEGREES_TO_RADIANS = 0.0174533

ORDER = ["6", "5", "4", "3", "2", "1", "12", "11", "10", "9", "8", "7"]


class WatchFace:
    def __init__(self, height, width, lcd):
        self._lcd = lcd
        self._center_x = width // 2
        self._center_y = height // 2
        self._radius = min(height, width) / 2 - 1

    def _get_time(self):
        local_time = time.localtime()

        return { "seconds": local_time[5], "minutes": local_time[4], "hour": local_time[3]}

    def _draw_ticks(self):
        self._draw_minute_ticks()
        self._draw_hour_ticks()

    def _draw_minute_ticks(self):
        for i in range(1, 61):
            angle = i * 6
            angle = angle * DEGREES_TO_RADIANS

            x1 = (self._center_x + (sin(angle) * self._radius))
            y1 = (self._center_y + (cos(angle) * self._radius))
            x2 = (self._center_x + (sin(angle) * (self._radius - 4)))
            y2 = (self._center_y + (cos(angle) * (self._radius - 4)))

            self._lcd.line(int(x1), int(y1), int(x2), int(y2), 1)

    def _draw_hour_ticks(self):
        for i in range(0, 12):
            angle = i * 30 * DEGREES_TO_RADIANS

            x1 = (self._center_x + (sin(angle) * self._radius))
            y1 = (self._center_y + (cos(angle) * self._radius))
            x2 = (self._center_x + (sin(angle) * (self._radius - 4)))
            y2 = (self._center_y + (cos(angle) * (self._radius - 4)))
            self._lcd.line(int(x1), int(y1), int(x2), int(y2), 1)

            x2 = (self._center_x + (sin(angle) * (self._radius - 8)))
            y2 = (self._center_y + (cos(angle) * (self._radius - 8)))

            self._lcd.text(str(ORDER[i]), int(x2 - 2), int(y2 - 2), 2)

    def _draw_seconds_line(self, sec):
        angle = sec * 6 * DEGREES_TO_RADIANS
        x = (self._center_x + (sin(angle) * (self._radius - 1)))
        y = (self._center_y - (cos(angle) * (self._radius - 1)))
        self._lcd.line(int(self._center_x), int(self._center_y), int(x), int(y), 1)

    def _draw_minutes_line(self, min):
        angle = min * 6 * DEGREES_TO_RADIANS
        x = (self._center_x + (sin(angle) * (self._radius - 10)))
        y = (self._center_y - (cos(angle) * (self._radius - 10)))
        self._lcd.line(int(self._center_x), int(self._center_y), int(x), int(y), 1)

    def _draw_hour_line(self, hour, min):
        angle = ((hour * 30) + ((min / 12) * 6)) * DEGREES_TO_RADIANS
        x = (self._center_x + (sin(angle) * (self._radius/ 2)))
        y = self._center_y - (cos(angle) * (self._radius / 2))
        self._lcd.line(int(self._center_x), int(self._center_y), int(x), int(y), 1)

    def _draw_lines(self, time_dict):
        self._draw_seconds_line(time_dict["seconds"])
        self._draw_minutes_line(time_dict["minutes"])
        self._draw_hour_line(time_dict["hour"], time_dict["minutes"])

    def draw(self):
        self._lcd.fill(0)
        time = self._get_time()
        self._draw_ticks()
        self._draw_lines(time)
        self._lcd.show()