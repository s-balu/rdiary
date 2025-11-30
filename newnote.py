from datetime import date
from pathlib import Path

# Paths
daily_dir = Path("source/daily")
daily_dir.mkdir(parents=True, exist_ok=True)

# Today's date
today = date.today()
filename = daily_dir / f"{today}.md"

# Format date with weekday and month name
title = today.strftime("%A, %d %B %Y")

# Only create if it doesn't exist
if not filename.exists():
    content = f"""# {title}

"""
    filename.write_text(content)
    print(f"Created new daily note: {filename}")
else:
    print(f"Daily note already exists: {filename}")
