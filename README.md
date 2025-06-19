# 🌡️ Raspberry Pi Temperature & Undervoltage Monitor

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Raspberry--Pi-green?logo=raspberry-pi&style=flat-square)
![License](https://img.shields.io/badge/License-GNU%20GPL-red?logo=gnu&style=flat-square)

> A simple, elegant terminal tool to monitor CPU temperature and undervoltage warnings on your Raspberry Pi, using Python and [`rich`](https://github.com/Textualize/rich).  
> Built with ❤️ by [@islamux](https://github.com/islamux)

---

## 🚀 Features

- 🌡️ Live temperature monitoring with color-coded alerts
- 🔌 Real-time undervoltage detection via `vcgencmd`
- 🎨 Beautiful terminal UI with [Rich](https://github.com/Textualize/rich)
- 🔊 Terminal sound alert when overheating
- 🐍 Lightweight & perfect for headless Pis (no GUI required)

---

## 📷 Preview

```shell
+---------------------------------------------+
|     Raspberry Pi Temp Monitor               |
+---------------------------------------------+
| 🌡️ CPU Temperature: 68.24°C                  |
| 🔴 Undervoltage detected now!               |
| 🕓 Undervoltage has occurred before         |
|                                            |
| 🔥 Overheating!                             |
+---------------------------------------------+
````

---

## 📦 Requirements

* Python 3.x
* `vcgencmd` command (usually pre-installed on Raspberry Pi OS)
* [`rich`](https://pypi.org/project/rich/)

Install dependencies:

```bash
pip install rich
sudo apt install libraspberrypi-bin
```

---

## 🧪 How to Use

```bash
git clone https://github.com/islamux/temp-monitor-raspberrypi4.git
cd temp-monitor-raspberrypi4

# (Optional) Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the monitor
python main.py
```

---

## 📂 File Structure

```
temp-monitor-raspberrypi4/
├── main.py               # Main script (real-time monitor)
├── requirements.txt      # Dependencies (rich)
└── README.md             # Project info
```

---

## 🧠 How It Works

* `main.py` reads the CPU temp from `/sys/class/thermal/thermal_zone0/temp`

* It calls `vcgencmd get_throttled` and decodes the hex response like:

  * `0x0` → No issues
  * `0x50000` → Past undervoltage detected
  * `0x50005` → Current and past undervoltage/throttling

* Displays user-friendly messages like:

  * 🔴 Undervoltage detected!
  * 🕓 Undervoltage has occurred before
  * 🐢 Currently throttled

---

## 📜 License

This project is licensed under the **GNU General Public License**.
Free as in freedom 🐧
Read more: [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

---

## ✨ Author

**[@islamux](https://github.com/islamux)**
💻 Muslim Developer • Linux Terminal Lover • Open Source Enthusiast
🕊️ "وَمَا أَرْسَلْنَاكَ إِلَّا رَحْمَةً لِّلْعَالَمِينَ" – الأنبياء 107
*Using technology to spread peace and benefit all of humanity.*

---

## ☁️ Future Ideas

* Logging temperature and undervoltage events to a file
* Display historical graph (CLI-based)
* Integration with MQTT / push notifications

```
