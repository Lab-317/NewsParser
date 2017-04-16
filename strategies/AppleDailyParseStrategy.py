#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Nicole
# @Date:   2014-11-02 12:11:06
# @Last Modified by:   Nicole
# @Last Modified time: 2014-11-03 21:42:49

from AbstractNewsParseStrategy import AbstractNewsParseStrategy

class AppleDailyParseStrategy(AbstractNewsParseStrategy):

	def isURLMatch(self, url):
		# http://www.appledaily.com.tw/
		return ".appledaily.com" in url

	def getTitle(self, beautiful_soup_object):
		paragraph_list = beautiful_soup_object.find("div", attrs={"id": "rt_headpic"}).find("header")
		print type(paragraph_list)

		title = ""
		for item in paragraph_list:
			title += item.text.strip()

		return title

	def getAuthor(self, beautiful_soup_object):
		pass
		# return beautiful_soup_object.select('#story_author')[0].text

	def getContent(self, beautiful_soup_object): 
		paragraph_list = beautiful_soup_object.find_all("p", id="summary")
		print paragraph_list	#拿掉這行就[Decode error - output not utf-8]

		content = ""
		for item in paragraph_list:
			content += item.text.strip()

		return content



	def getPublishDate(self, beautiful_soup_object):
		pass
