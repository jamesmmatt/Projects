import inflection
import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.dailysmarty.com/topics/python')

soup = BeautifulSoup(r.content, 'html.parser')


def links_generator():

	links = []
	for link in soup.find_all('a'):
		links.append(link.get('href'))

	return links

links = links_generator()


def find_links_for_posts(linksList):
	posts = []
	for link in linksList:
		if "/posts/" in link:
			link_with_out_posts = link[7:]
			posts.append(link_with_out_posts)


	return posts

links = find_links_for_posts(links)


def format_titles(lists_from_posts):
	titles = []
	for title in lists_from_posts:
		titles_with_underscores = inflection.underscore(title)
		titles_humanized = inflection.humanize(titles_with_underscores)
		
		titles.append(titles_humanized.title())

	return titles

links = format_titles(links)


for title in links:
	print(title)