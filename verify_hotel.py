from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    # 1. Home Page
    page.goto("http://localhost:8000")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/home.png")

    # 2. Room Catalog
    page.get_by_role("link", name="Бөлмелер қоры").first.click()
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/catalog.png")

    # 3. Room Detail
    page.get_by_role("link", name="Толығырақ").first.click()
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/detail.png")

    # 4. Booking Form
    page.get_by_role("link", name="Қазір брондау").click()
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/booking_form.png")

    # 5. Fill Form
    page.get_by_label("Аты-жөніңіз").fill("Асхат Қазақбаев")
    page.wait_for_timeout(500)
    page.get_by_label("Телефон нөмірі").fill("+77012345678")
    page.wait_for_timeout(500)
    page.get_by_label("Электронды пошта").fill("askhat@example.kz")
    page.wait_for_timeout(500)
    page.get_by_label("Келу күні").fill("2024-12-01")
    page.wait_for_timeout(500)
    page.get_by_label("Кету күні").fill("2024-12-05")
    page.wait_for_timeout(500)
    page.get_by_label("Қонақтар саны").fill("2")
    page.wait_for_timeout(500)

    page.screenshot(path="/home/jules/verification/screenshots/booking_filled.png")
    page.get_by_role("button", name="Брондауды растау").click()
    page.wait_for_timeout(1000)

    # 6. Success Page
    page.screenshot(path="/home/jules/verification/screenshots/booking_success.png")
    page.wait_for_timeout(1000)

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
