# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

# 起動引数を使う場合はコメントを外す。
# import sys
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

from selenium import webdriver
from factory import SeleniumDriverFactory as Factory

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

if __name__ == '__main__':
    # 起動引数の取得
    # args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。

    # Selenium 経由でブラウザを操作する
    URL_HOME = setting.ENV_DIC[ImportEnvKeyEnum.URL_HOME.value]
    
    try: 
        driver = Factory.create()
        driver.get(URL_HOME)
        logger.info(driver.current_url)

    finally:
        # ブラウザを終了する
        driver.quit()

