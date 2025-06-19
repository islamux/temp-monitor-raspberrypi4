## 📄 `main.py`

```python
#!/usr/bin/env python3
import time
import subprocess
from rich.console import Console
from rich.live import Live
from rich.panel import Panel

console = Console()

TEMP_THRESHOLD = 70  # درجة الحرارة التي يعتبر بعدها الجهاز ساخنًا جدًا

# ✅ فحص درجة الحرارة من النظام
def get_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_str = f.readline()
        return float(temp_str) / 1000
    except FileNotFoundError:
        return None

# ✅ فحص الجهد المنخفض عبر vcgencmd
def check_undervoltage():
    try:
        result = subprocess.check_output(['vcgencmd', 'get_throttled']).decode().strip()
        if "0x0" in result:
            return "⚡ Voltage: [green]Normal[/green]"
        else:
            return f"⚡ Voltage: [bold red]Warning![/bold red] ({result})"
    except Exception as e:
        return f"⚡ Voltage: [yellow]Unknown[/yellow] ({e})"

# ✅ إعداد واجهة العرض
def make_panel(temp):
    voltage_status = check_undervoltage()
    status = "🔥 [bold red]Overheating![/bold red]" if temp >= TEMP_THRESHOLD else "✅ [green]Normal[/green]"
    panel = Panel(
        f"🌡️ [bold]CPU Temperature:[/bold] {temp:.2f}°C\n"
        f"{voltage_status}\n\n"
        f"{status}",
        title="Raspberry Pi Temp Monitor",
        border_style="red" if temp >= TEMP_THRESHOLD else "cyan"
    )
    return panel

# ✅ تنبيه صوتي بسيط
def beep():
    print('\a', end='', flush=True)  # يصدر beep في الطرفية إذا كانت مدعومة

# ✅ الحلقة الرئيسية
def main():
    with Live(console=console, refresh_per_second=1) as live:
        while True:
            temp = get_cpu_temperature()
            if temp is not None:
                if temp >= TEMP_THRESHOLD:
                    beep()
                live.update(make_panel(temp))
            else:
                live.update(Panel("🚫 [red]Temperature sensor not found![/red]", title="Error"))
            time.sleep(1)

if __name__ == "__main__":
    main()
```

---

## 🧰 خطوات التشغيل:

1. تأكد من تثبيت `rich`:

   ```bash
   pip install rich
   ```

2. اجعل الملف قابلًا للتنفيذ:

   ```bash
   chmod +x main.py
   ```

3. ثم شغله:

   ```bash
   ./main.py
   ```

---

## 🔐 ملاحظة أمان:

* تأكد أن `vcgencmd` متاح (عادة يكون مرفقًا مع Raspbian).
* لو ظهرت مشكلة في أمر الجهد، أخبرني لأعطيك بديل عبر `dmesg`.
