from playwright.async_api import async_playwright, async_find_all
import playwright
import os
import time
from dotenv import load_dotenv

load_dotenv()


async def start():
    async with async_playwright() as playwright:
        BROWSER = await playwright.chromium.launch(headless=False)
        PAGE = await BROWSER.new_page()

        await PAGE.goto("https://chat.openai.com/chat")

        # login
        await PAGE.click("button[class*='btn-primary']")
        await PAGE.wait_for_selector("input[name='username']")
        # fill in the email and password
        await PAGE.fill("input[name='username']", os.getenv("OPENAI_EMAIL"))
        # Click the continue button
        await PAGE.click("button[name='action']")
        await PAGE.fill("input[name='password']", os.getenv("OPENAI_PASSWORD"))
        # click the login button
        await PAGE.click("button[name='action']")
        # wait for the login to complete
        await PAGE.wait_for_selector(
            "div[class*='PromptTextarea__TextareaWrapper']")
        print("Logged in")

        # Click this 'next' ensuring 'next' is the text content button <button class="btn flex gap-2 justify-center btn-neutral ml-auto" tabindex="0">Next</button>
        await PAGE.click("button:has-text('Next')", timeout=3000)
        await PAGE.click("button:has-text('Next')", timeout=3000)
        await PAGE.click("button:has-text('Done')", timeout=3000)

        await PAGE.fill("div[class*='PromptTextarea__TextareaWrapper'] textarea", "What is python")
        # Click the send message button
        await PAGE.click("button[class*='PromptTextarea__PositionSubmit']")
        # Get the first message
        response = await PAGE.wait_for_selector("div[class*='request-:R2dm:-0 markdown prose dark:prose-invert break-words light']")
        # Get the actual text from the response
        response_text = await PAGE.evaluate("response => response.textContent", response)
        test = await PAGE.async_find_all(".ConversationItem__Message-sc-18srrdc-1")
        print(test)
        return response_text

        # Keep the page from closing
        while True:
            time.sleep(1)
