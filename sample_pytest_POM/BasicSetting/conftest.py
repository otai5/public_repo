from BasicSetting.import_list import *

# driver settings
@pytest.fixture(autouse=False, scope='module')
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--window-size=1920,1080')
    options.add_argument('disable-gpu')
    options.add_argument("--use-fake-ui-for-media-stream") # mic & cam allow
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://google.com') # sample (target Url)
    driver.implicitly_wait(30)
    wait = WebDriverWait(driver, 20)
    yield driver
    driver.quit()

@pytest.fixture(autouse=False, scope='module')
def worksheet():
    # 구글 스프레드시트 연동
    scope = ([
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ])
    credentials = Credentials.from_service_account_file('keys', scopes=scope) # sample
    gc = gspread.authorize(credentials)
    spreadsheet_url = 'https://docs.google.com/spreadsheets/sampleurl' # sample
    doc = gc.open_by_url(spreadsheet_url)
    worksheet = doc.worksheet('sheet') # sample
    yield worksheet

