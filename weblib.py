import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import expected_conditions as EC


def InitFirefoxDriver(executable_path=None):
    """
    Creates firefox driver initialized for logging and testing options
    """
    c = DesiredCapabilities.FIREFOX.copy()
    c['loggingPrefs'] = {'browser': 'ALL'}

    p = webdriver.FirefoxProfile()
    # p.set_preference(u'dom.disable_window_flip', False)
    #p.set_preference(u'services.sync.prefs.sync.dom.disable_window_flip', False)
    p.set_preference(u'dom.webnotifications.enabled', False)
    p.set_preference(u'media.navigator.permission.disabled', True)
    p.set_preference(u'security.mixed_content.block_display_content', True)
    p.set_preference(u'security.mixed_content.block_active_content', True)

    #    p.set_preference(u'devtools.chrome.enabled', True)
    #    p.set_preference(u'devtools.webconsole.persistlog', True)
    #
    #    p.set_preference(u'devtools.webconsole.filter.jslog', True)
    #    p.set_preference(u'devtools.webconsole.filter.warn', True)
    #    p.set_preference(u'devtools.webconsole.filter.network', True)
    #    p.set_preference(u'devtools.browserconsole.filter.jslog', True)
    #    p.set_preference(u'devtools.browserconsole.filter.log', True)
    #
    #    p.set_preference(u'extensions.sdk.console.logLevel', 'ALL')
    #    p.set_preference(u'webdriver.log.browser.level', 'ALL')

    #p.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/wav")
    #p.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/x-wav")
    #p.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")
    p.set_preference("browser.helperApps.neverAsk.saveToDisk",
                     "audio/wav,audio/x-wav,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    if executable_path:
        binary = FirefoxBinary(firefox_path=executable_path)
        return webdriver.Firefox(capabilities=c, firefox_profile=p, firefox_binary=binary)
    return webdriver.Firefox(capabilities=c, firefox_profile=p)


def InitChromeDriver(executable_path=None):
    """
    Creates Chrome driver initialized for logging and testing options
    """
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    if executable_path:
        opts = Options()
        opts._binary_location = executable_path
        return webdriver.Chrome(chrome_options=opts, desired_capabilities=d)
    opts = Options()
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--use-fake-ui-for-media-stream')
    opts.add_argument('--disable-notifications')
    opts.add_argument('--allow-running-insecure-content')
    opts.add_argument('--allow-running-insecure-content=http://192.168.85.232:8090')
    opts.add_argument('--unsafely-treat-insecure-origin-as-secure=http://10.52.98.13:8080')
    return webdriver.Chrome(chrome_options=opts, desired_capabilities=d)

def InitChromeDriverNew(executable_path=None):
    """
    Creates Chrome driver initialized for logging and testing options
    """
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'browser':'ALL' }
    if executable_path:
        opts = Options()
        opts._binary_location = executable_path
        return webdriver.Chrome(chrome_options=opts, desired_capabilities=d)
    opts = webdriver.ChromeOptions()
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--use-fake-ui-for-media-stream')
    opts.add_argument('--disable-notifications')
    opts.add_argument('--allow-running-insecure-content')
    opts.add_argument('--allow-running-insecure-content=http://192.168.85.232:8090')
    opts.add_argument('--unsafely-treat-insecure-origin-as-secure=http://10.52.98.13:8080')
    return webdriver.Remote(command_executor= 'http://127.0.0.1:9515', desired_capabilities=opts.to_capabilities())

class Driver():
    """
    Selenim web driver interface and service methods
    """

    def __init__(self, driver_type):

        self.keepsilence = 0
        self.drivertype = driver_type
        self.driver = None


        for i in range(3):
            try:

                if self.drivertype == "Firefox":
                    self.driver = InitFirefoxDriver()
                elif self.drivertype == "ChromeRemote":
                    self.driver = InitChromeDriverNew()
                else:
                    # self.driver = InitChromeDriver()
                    self.driver = InitChromeDriver()
                if self.driver:
                    print("Driver initialized %s" % (self.drivertype))
                    break
            except Exception, mess:
                print("Can not initialize driver  - trying again %s" % mess)
                time.sleep(1)
        if not self.driver:
            print("Impossible to start browser")


if __name__ == "__main__":
    # for Firefox
    wb_driver = Driver("Firefox")
    wb_driver.driver.get('http://www.google.com/xhtml')
    time.sleep(5)  # Let the user actually see something!
    search_box = wb_driver.driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    wb_driver.driver.quit()
    # for Chrome
    wb_driver = Driver("Chrome")
    wb_driver.driver.get('http://www.google.com/xhtml')
    time.sleep(5)  # Let the user actually see something!
    search_box = wb_driver.driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    wb_driver.driver.quit()
    # for remote chrome
    # on the machine start chromedriver
    # ctl-utamhank-m:browsers utamhank$ ./chromedriver
    # Starting ChromeDriver 2.31.488774 (7e15618d1bf16df8bf0ecf2914ed1964a387ba0b) on port 9515
    # Only local connections are allowed.
    wb_driver = Driver("ChromeRemote")
    wb_driver.driver.get('http://www.google.com/xhtml')
    time.sleep(5)  # Let the user actually see something!
    search_box = wb_driver.driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    wb_driver.driver.quit()
