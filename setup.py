# -*- coding:utf-8 -*-
# ! usr/bin/env python3
"""
Created on 13/07/2020 下午8:23
@Author: xinzhi yao
"""

"""
setup.py是setuptools的构建脚本。
它告诉setuptools你的包（例如名称和版本）以及要包含的代码文件。
"""

import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="PlantTraitEnrichment",
  version="0.0.1",
  author="Xinzhi Yao",
  author_email="xinzhi_bioinfo@163.com",
  description="A python package for plant trait enrichment analysis.",
  long_description=long_description,
  # long_description_content_type="text/markdown",
  long_description_content_type="Markdown",
  url="https://github.com/pypa/sampleproject",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)
