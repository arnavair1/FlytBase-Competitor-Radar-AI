import time
from dotenv import load_dotenv


from config import COMPETITORS
from scraper import scrape_page
from database import load_snapshot, save_snapshot
from change_detector import has_changed
from ai_generator import generate_battle_card


# ===============================
# Load ENV (for GEMINI_API_KEY)
# ===============================
load_dotenv()


# ===============================
# Main Agent
# ===============================
def run_agent():
    print("\n==============================")
    print("🚀 FlytBase Competitor Agent")
    print("==============================")

    for comp in COMPETITORS:
        try:
            print(f"\n🔎 Checking {comp['name']}...")

            new_text = scrape_page(comp["url"])
            if not new_text:
                print("❌ Could not scrape page.")
                continue

            old_text = load_snapshot(comp["name"])

            if has_changed(old_text, new_text):
                print("🚨 Change detected!")

                # Save new snapshot
                save_snapshot(comp["name"], new_text)

                print("🤖 Generating AI battle card...\n")
                ai_output = generate_battle_card(
                    comp["name"], new_text
                )

                print("\n========== AI OUTPUT ==========\n")
                print(ai_output)
                print("\n===============================\n")

            else:
                print("✅ No change detected.")

        except Exception as e:
            print(f"❌ Error checking {comp['name']}: {e}")


# ===============================
# Scheduler
# ===============================
if __name__ == "__main__":
    while True:
        run_agent()
        print("😴 Sleeping...\n")
        time.sleep(3600)   # change to 3600 later
