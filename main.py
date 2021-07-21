from selenium import webdriver
driver = webdriver.Firefox(executable_path="C:\\Users\\I525775\\PycharmProjects\\youtube_comment_scrapping\\geckodriver.exe")
driver.get("https://www.youtube.com/watch?v=sE1m3EWXP5o")
title = driver.find_element_by_css_selector(".title yt-formatted-string").text
views = driver.find_element_by_css_selector("ytd-video-view-count-renderer").text
date = driver.find_element_by_css_selector("#info-strings yt-formatted-string").text
comments = []
for comment in driver.find_elements_by_css_selector("#contents ytd-comment-thread-renderer"):
    comment_user = comment.find_element_by_css_selector("#text").text
    comment_body = comment.find_element_by_css_selector("#content_text").text
    comments.append([comment_user, comment_body])