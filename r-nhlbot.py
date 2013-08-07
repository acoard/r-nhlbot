#reddit bot for /r/nhl

import praw

user_agent = ("Bot for aggregating hockey team related subreddit top posts. v0.5 /u/acoard")
r = praw.Reddit(user_agent=user_agent)

class nhlBot:
	hockey_subs = ['canucks', "anaheimducks", "calgaryflames", "losangeleskings", 
			"coyotes", "sanjosesharks", "hawks", "coloradoavalanche", "dallasstars", 
			"wildhockey", "predators", "stlouisblues", "winnipegjets", "canes", "bluejackets", 
			"devils", "newyorkislanders", "rangers", "flyers", "penguins", "caps", "bostonbruins", 
			"sabres", "detroitredwings", "floridapanthers", "habs", "ottawasenators", "tampabaylightning", "leafs"]
	hockey_subs_TEMP = ['canucks', 'leafs', 'flyers']

	def getHockeyPosts(self):
		numberOfSubmissions = 1
		#Put submissions in a dictionary so that they can be linked to each subreddit.
		top_submissions = dict() 
		for subreddit in self.hockey_subs_TEMP: #DEV only
			top_submissions[subreddit] = [x for x in r.get_subreddit(subreddit).get_top_from_week(limit=numberOfSubmissions)][0]
		return top_submissions

	def formatPosts(self, posts):
		#Takes getHockeyPosts() for input.
		message = "Top posts for each hockey team's subreddit.\n"
		for i in posts:
			message += str(i) + ": " + "[" + str(posts[i]).split(' :: ')[1] +"](" + str(posts[i].short_link) + ")" \
			+ " with a karma of " + str(posts[i]).split(' ::')[0] + "\n"
		return message

nhlBot = nhlBot()
posts = nhlBot.getHockeyPosts()