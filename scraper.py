import re
import requests
import time
from datetime import datetime, timedelta
from collections import OrderedDict
from zoneinfo import ZoneInfo

# ========== CONFIGURATION ==========
TEHRAN_TZ = ZoneInfo("Asia/Tehran")

CHANNELS = [
    "xgvpn",
    "npvtunel_karing_hiddify",
    "appxa",
    "RavenAzad",
    "appxa2",
    "baraye_azadi_gp",
    "amir_webstudio",
    "IRAN_V2RAY1",
    "SlipNet_decode",
    "blackRay",
    "SparrK_VPN",
    "slipnet_chat",
    "SlipNet_app",
    "VConfing",
    "capcutchina"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

SLIPNET_REGEX = re.compile(r'slipnet(?:-enc)?:\/\/[^\s<>"\'\[\]{}|\\^`]+', re.IGNORECASE)

OUTPUT_FILE = "☬SHΞN™.txt"

# ========== FUNCTIONS ==========
def fetch_channel_page(username: str) -> str:
    url = f"https://t.me/s/{username}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"[!] Error fetching {username}: {e}")
        return ""

def extract_links_from_html(html: str) -> set:
    return set(SLIPNET_REGEX.findall(html))

def get_next_refresh(minutes=10) -> str:
    """زمان بعدی به‌روزرسانی با وقت تهران (بر اساس cron 10 دقیقه)"""
    now_tehran = datetime.now(TEHRAN_TZ)
    future = now_tehran + timedelta(minutes=minutes)
    return future.strftime("%I:%M %p").lstrip("0")

def generate_output(per_channel_data: OrderedDict, total_unique: int) -> str:
    now_tehran = datetime.now(TEHRAN_TZ)
    now_str = now_tehran.strftime("%Y-%m-%d %H:%M:%S")
    next_refresh = get_next_refresh(10)  # 10 دقیقه بعد

    lines = []
    lines.append("☬Exclusive SHΞN™ made")
    lines.append("Live SlipNet🪽 Collector")
    lines.append(f"Last update: {now_str}      Total node : {total_unique}   Next refresh: {next_refresh}")
    lines.append("")  # خط خالی قبل از اولین بخش

    for ch, links in per_channel_data.items():
        count = len(links)
        if count == 0:
            continue
        lines.append(f"☬Slipnet Node From : {ch} {count} Node")
        lines.append("")  # خط خالی بعد از عنوان
        # هر کانفیگ در یک خط مجزا (بدون کاراکتر اضافی)
        for link in links:
            lines.append(link)
        lines.append("")  # خط خالی بین سورس‌ها

    # ========== فوتر جدید با آرت ASCII ==========
    lines.append("Overhauld ☬ SHΞЯVIN™")
    lines.append("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠉⠉⠉⠉⠉⠉⠉⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⢀⣤⣾⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠉⠀⠀⠚⠛⠛⠛⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⣀⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠀⠉⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⠤⠀⠉⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠉⠉⢀⣀⣤⣶⣾⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠒⠛⠛⠛⠛⠛⠛⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠀⣶⣶⠀⢰⣶⣶⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⡀⠙⠋⢀⡀⠈⠛⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠿⣶⡶⠿⣿⣿⠶⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠀⣿⡇⠀⣿⣿⠀⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠀⣿⣇⣀⣿⣿⠀⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠛⠛⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣶⣶⣶⠀⣶⣶⣶⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠿⠿⠿⠀⠿⠿⠿⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠋⢀⣿⠋⢀⡀⠙⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣇⠀⢿⡏⢀⣾⡿⠀⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣤⣀⣀⣼⣇⣀⣰⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    lines.append("☬Exclusive SHΞN™ made")
    lines.append("More !? T.me/Shervini")

    return "\n".join(lines)

def main():
    print(f"[{datetime.now(TEHRAN_TZ).isoformat()}] Starting SlipNet collector (TXT mode)")

    per_channel_links = OrderedDict()
    all_unique_links = set()

    for ch in CHANNELS:
        print(f"  -> Fetching {ch}")
        html = fetch_channel_page(ch)
        if not html:
            per_channel_links[ch] = []
            continue

        links = extract_links_from_html(html)
        if not links:
            per_channel_links[ch] = []
            print(f"      No slipnet links found")
        else:
            unique_links = list(links)
            per_channel_links[ch] = unique_links
            all_unique_links.update(unique_links)
            print(f"      Found {len(unique_links)} unique slipnet link(s)")

        time.sleep(1)  # احترام به محدودیت

    total_unique_all = len(all_unique_links)
    print(f"Total unique configs (across all channels): {total_unique_all}")

    # بازنویسی کامل فایل (حتی اگر لینک‌ها تغییر نکرده باشند، timestamp ها عوض می‌شوند)
    output_content = generate_output(per_channel_links, total_unique_all)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Output saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
