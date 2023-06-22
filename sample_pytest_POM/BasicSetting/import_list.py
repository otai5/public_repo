import pytest
import os
import random
import time
import gspread
import pyperclip
import json
import requests

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pytest_html_reporter import attach
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
from webdriver_manager.chrome import ChromeDriverManager
