import allure

def attach_screenshot(page, name="Screenshot"):

   # Capture screenshot and attach it to Allure report.

    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )

def attach_video(page, name="Test Video"):

    #Attach recorded video to Allure report (if enabled in Playwright config).

    if page.video:
        video_path = page.video.path()
        with open(video_path, "rb") as video_file:
            allure.attach(
                video_file.read(),
                name=name,
                attachment_type=allure.attachment_type.MP4
            )