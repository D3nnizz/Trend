import matplotlib.pyplot as plt
import mpld3
import subprocess

# Timeframes die je wilt maken
timeframes = ["3m", "5m", "15m", "30m", "1h", "4h", "1d"]

# === 1. Maak charts voor elk timeframe ===
for tf in timeframes:
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [12, 20, 25, 30], marker="o")  # vervang dit met je eigen data per timeframe
    ax.set_title(f"Chart voor {tf}")

    chart_file = f"chart_{tf}.html"
    with open(chart_file, "w", encoding="utf-8") as f:
        f.write(mpld3.fig_to_html(fig))

    print(f"✅ Chart opgeslagen als {chart_file}")

# === 2. Maak dashboard met dropdown ===
dashboard_file = "dashboard.html"
dashboard_html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <title>Charts Dashboard</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }}
    header {{
      background: #f8f8f8;
      padding: 10px;
      border-bottom: 1px solid #ccc;
    }}
    iframe {{
      border: none;
      width: 100%;
      height: calc(100vh - 50px);
    }}
    select {{
      font-size: 16px;
      padding: 5px;
    }}
  </style>
</head>
<body>
  <header>
    <label for="timeframe">Kies timeframe: </label>
    <select id="timeframe">
      {''.join([f'<option value="chart_{tf}.html"> {tf} </option>' for tf in timeframes])}
    </select>
  </header>

  <iframe id="chartFrame" src="chart_{timeframes[0]}.html"></iframe>

  <script>
    const select = document.getElementById("timeframe");
    const iframe = document.getElementById("chartFrame");

    select.addEventListener("change", () => {{
      iframe.src = select.value + "?cachebuster=" + new Date().getTime();
    }});

    // Auto-refresh elke 30s
    setInterval(() => {{
      iframe.src = select.value + "?cachebuster=" + new Date().getTime();
    }}, 30000);
  </script>
</body>
</html>
"""

with open(dashboard_file, "w", encoding="utf-8") as f:
    f.write(dashboard_html)

print(f"✅ Dashboard opgeslagen als {dashboard_file}")

# === 3. Commit & push naar GitHub ===
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Update charts and dashboard"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("🚀 Charts en dashboard succesvol naar GitHub Pages gepusht!")
except subprocess.CalledProcessError as e:
    print("⚠️ Git-commando mislukt:", e)
