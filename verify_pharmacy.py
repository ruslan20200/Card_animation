from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    # Go to homepage
    page.goto("http://localhost:8000")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/home.png")

    # Go to catalog
    page.get_by_role("link", name="Дәрі-дәрмектер").click()
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/catalog.png")

    # Filter by category
    page.get_by_role("link", name="Витаминдер").click()
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/catalog_filtered.png")

    # Go to detail of first medicine
    page.get_by_role("link", name="Толығырақ").first.click()
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/detail.png")

    # Click order button in main content
    page.get_by_role("main").get_by_role("link", name="Тапсырыс беру").click()
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/order_form.png")

    # Fill order form by placeholder if label fails
    page.get_by_placeholder("Атыңыз").fill("Серік Болатов")
    page.wait_for_timeout(500)
    page.get_by_placeholder("+7 (7xx) xxx-xx-xx").fill("+77071112233")
    page.wait_for_timeout(500)
    page.screenshot(path="/home/jules/verification/screenshots/order_form_filled.png")

    page.get_by_role("button", name="Өтінімді жіберу").click()
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/success.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
