import time
from datetime import datetime

current_time = time.localtime()
formatted_seconds = f"{current_time.tm_sec:,.4f}"
scientific_seconds = f"{current_time.tm_sec:.2e}"

print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_seconds} in scientific notation.")

print(datetime.now().strftime("%b %d %Y"))
