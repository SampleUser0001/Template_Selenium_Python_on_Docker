# -*- coding: utf-8 -*-
import os
from os.path import join, dirname
from dotenv import load_dotenv
from enum import Enum

class ImportEnvKeyEnum(Enum):
  """ .envファイルのキーを書く """
  SELENIUM_HOST_NAME="SELENIUM_HOST_NAME"
  URL_HOME="URL_HOME"

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ENV_DIC = {}
# ImportEnvKeyEnumの値を書く
ENV_KEYS = [
  ImportEnvKeyEnum.SELENIUM_HOST_NAME,
  ImportEnvKeyEnum.URL_HOME
]

for e in ImportEnvKeyEnum:
  ENV_DIC[e.value] = os.environ.get(e.value)