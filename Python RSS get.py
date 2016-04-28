from bs4 import BeautifulSoup
import urllib2

#Program that gets all important RSS Feeds. 
#Still dont know what to do with them
#Need to output them to html file
#Either output directly to html from this, or write to file and then get the file contents
#Need to find a fancy way to output

#Arrays of RSS Feeds 
list_of_rss = ['http://rss.cnn.com/rss/money_news_economy.rss',"http://www.forbes.com/technology/feed/",'http://www.forbes.com/business/feed/','http://www.forbes.com/finance/feed/',
					'http://www.forbes.com/entrepreneurs/feed/', 'http://www.business-standard.com/rss/finance-features-10302.rss',
					'http://www.business-standard.com/rss/technology-108.rss', 'http://www.economist.com/sections/economics/rss.xml',
					 'http://www.economist.com/sections/science-technology/rss.xml',
					 'http://www.economist.com/blogs/gametheory/index.xml', 'http://www.economist.com/blogs/freeexchange/index.xml',
					 'http://www.economist.com/blogs/economist-explains/index.xml','http://www.economist.com/sections/business-finance/rss.xml',
					'http://rss.cnn.com/rss/money_news_economy.rss','http://feeds.feedburner.com/entrepreneur/growingyourbusiness.rss',
					'http://feeds.feedburner.com/entrepreneur/startingabusiness.rss', 'http://feeds.feedburner.com/entrepreneur/ebiz',
					'http://feeds.feedburner.com/entrepreneur/latest','http://rss.cnn.com/rss/money_technology.rss',
					'http://feeds.feedburner.com/inc/channel/start-up']

def main():
	newsCount = 0;
	HTMLDocBegin = '''
<!DOCTYPE html>
<html>
	<head>
		<LINK href="style.css" rel="stylesheet" type="text/css">
		<script type="text/javascript" src="javascript.js"></script>
		<title>RSS Feed</title>
	</head>
	<body>
		<h2>List of Articles from RSS Feeds:</h2>
		<h4 onclick="randomArticle();">Click Me For a Random Article</h4>
		<h5 id="randomLinkTitle">A Random Article Will Appear Here when you click the text above.</h5>
		<h5 id="randomLink">A Random Link Will Appear Here when you click the text above.</h5>
	'''
	HTMLDocEnd = '''
	</body>
</html>
	'''
	#Writes to file
	with open("index.html", "w") as myfile:

		myfile.write(HTMLDocBegin) #writes beginning template of regular html doc

		#For loop to iterate through rss feeds
		for url in list_of_rss:
			#print(url) #Prints location of RSS Feed
			req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' }) #User Agent because Economist is a fucking bitch
			rss_feed_url = urllib2.urlopen(req).read()
			soup = BeautifulSoup(rss_feed_url, "lxml-xml")
			for item in soup.find_all('item'):
				#myfile.write("<div class=\"surrounding\">") #div to surround story
				linkNoShit = str(item.link).replace("<link>","<div class=\"story\"> <a href=").replace("</link>",">")
				titleNoShit = str(item.title).replace("<title>","").replace("</title>","</a></div>")
				myfile.write(linkNoShit + titleNoShit)#combines and makes title a clickable link
				#myfile.write("</div>") #div to end surrounding
				newsCount += 1

		myfile.write(HTMLDocEnd) #writes end template of regular html doc

	print(newsCount)
		

main()