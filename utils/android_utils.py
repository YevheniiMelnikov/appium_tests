import subprocess


def android_get_desired_capabilities() -> dict:
    output = subprocess.getoutput("./adb devices")
    udid = output.split("\n")[1].split(" ")[0]
    
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '14',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': "emulator-5554",  # test
        # 'udid': udid,  # prod
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
