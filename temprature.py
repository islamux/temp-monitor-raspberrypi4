#!/usr/bin/env python3
import time
import os
from rich.console import Console
from rich.live import Live
from rich.panel import Panel

console = Console()

TEMP_THRESHOLD = 70  # درجة الحرارة القصوى قبل إطلاق التنبيه

def get_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_str = f.readline()
        return float(temp_str) / 1000
    except FileNotFoundError:
        return None

def make_panel(temp):
    status = "🔥 [bold red]Overheating![/bold red]" if temp >= TEMP_THRESHOLD else "✅ [green]Normal[/green]"
    panel = Panel(
        f"🌡️ [bold]CPU Temperature:[/bold] {temp:.2f}°C\n\n{status}",
        title="Raspberry Pi Temp Monitor",
        border_style="cyan" if temp < TEMP_THRESHOLD else "red"
    )
    return panel

def beep():
    # هذا يصدر beep من الطرفية إذا كان الصوت مفعلاً
    print('\a', end='', flush=True)

def main():
    with Live(console=console, refresh_per_second=1) as live:
        while True:
            temp = get_cpu_temperature()
            if temp:
                if temp >= TEMP_THRESHOLD:
                    beep()
                live.update(make_panel(temp))
            else:
                live.update(Panel("🚫 [red]Temperature sensor not found![/red]", title="Error"))
            time.sleep(1)

if __name__ == "__main__":
    main()

