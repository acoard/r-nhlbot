#reddit bot for /r/nhl

import praw

user_agent = ("Bot for aggregating hockey team related subreddit top posts. v0.5 /u/acoard")
r = praw.Reddit(user_agent=user_agent)

hockey_subs = ['canucks', "anaheimducks", "calgaryflames", "losangeleskings", 
			"coyotes", "sanjosesharks", "hawks", "coloradoavalanche", "dallasstars", 
			"wildhockey", "predators", "stlouisblues", "winnipegjets", "canes", "bluejackets", 
			"devils", "newyorkislanders", "rangers", "flyers", "penguins", "caps", "bostonbruins", 
			"sabres", "detroitredwings", "floridapanthers", "habs", "ottawasenators", "tampabaylightning", "leafs"]

def getHotHockeyPosts():
	numberOfSubmissions = 1
	#Put submissions in a dictionary so that they can be linked to each subreddit.
	top_submissions = dict() 
	for subreddit in hockey_subs:
		top_submissions[subreddit] = [str(x) for x in r.get_subreddit(subreddit).get_hot(limit=numberOfSubmissions)]
	return top_submissions
