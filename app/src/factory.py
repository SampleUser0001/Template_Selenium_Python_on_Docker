# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

from selenium import webdriver

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

class SeleniumDriverFactory:
    
    @staticmethod
    def create():
        # .envの取得
        SELENIUM_HOST_NAME = setting.ENV_DIC[ImportEnvKeyEnum.SELENIUM_HOST_NAME.value]
    
        # Chrome のオプションを設定する
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        
        # Selenium Server に接続する
        return webdriver.Remote(
            command_executor='http://{}:4444/wd/hub'.format(SELENIUM_HOST_NAME),
            options=options
        )
