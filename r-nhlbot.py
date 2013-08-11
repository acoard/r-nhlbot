#reddit bot for /r/nhl
import praw
import time

r = praw.Reddit("User Agent: NHLBot for /r/hockey. v1.0 created by /u/acoard")
nhlb = "NHLBot"

hockey_subs = [('canucks', "Vancouver Canucks"), ("anaheimducks", "Anaheim Ducks"), ("calgaryflames", "Calgary Flames"), ("losangeleskings", "Los Angeles Kings"), \
			("coyotes", "Phoenix Coyotes"), ("sanjosesharks", "San Jose Sharks"), ("hawks", "Chicago Blackhawks"),  ("coloradoavalanche", "Colorado Avalanche"), ("dallasstars", "Dallas Stars"),  
			("wildhockey", "Minnesota Wild"), ("predators", "Nashville Predators"), ("stlouisblues", "St. Louis Blues"), ("winnipegjets", "Winnipeg Jets"), ("canes", "Carolina Hurricanes"), ("bluejackets", "Columbus Blue Jackets"), 
			("devils", "New Jersey Devils"), ("newyorkislanders", "New York Islanders"), ("rangers", "New York Rangers"), ("flyers", "Philidelphia Flyers"), ("penguins", "Pittsburg Penguins"), ("caps", "Washington Capitals"), ("bostonbruins", "Boston Bruins"), 
			("sabres", "Buffalo Sabres"), ("detroitredwings", "Detroit Red Wings"), ("floridapanthers", "Florida Panthers"), ("habs", "Montreal Canadiens"), ("ottawasenators", "Ottawa Senators"), ("tampabaylightning", "Tampa Bay Lightning"), ("leafs", "Toronto Maple Leafs")]
hockey_subs_TEMP = [('canucks', "Vancouver Canucks"), ("anaheimducks", "Anaheim Ducks"), ("calgaryflames", "Calgary Flames")]

class TrackedSubreddit:
		def __init__(self, subreddit):
			self.subreddit = subreddit
			self.top_weekly_post = dict()
		def __repr__(self):
			return str(self.subreddit)
		def test(self):
			print "A test!"
		
		def getTopWeeklyPost(self, numberOfPosts=1):
			"""Returns a dict, keys: "title", "karma".  Currently does NOT SUPPORT multiple top posts."""
			self.numberOfPosts = numberOfPosts	
			self.top_weekly_post_response = r.get_subreddit(self.subreddit).get_top_from_week(limit=numberOfPosts)
			for i in self.top_weekly_post_response:
				self.top_weekly_post["title"] = str(i).split(" :: ")[1]
				self.top_weekly_post["karma"] = str(i).split(" :: ")[0]
			return self.top_weekly_post


class NHLBot:
	#TODO: Generalize NHLBot, make "NHL" be a paramater it takes.
	def __init__(self):
		self.numberOfSubmissions = 1
		self.top_submissions = dict()
		self.message = "" 
	
	def trackSubs(self):
		"""Creates the TrackSubreddit classes for each sub in the list. Returns a list of each instance."""
		self.list_of_subreddit_classes = list()
		for subreddit in hockey_subs_TEMP:
			print "Subreddit: " + subreddit[0]
			x = TrackedSubreddit(subreddit[0])
			self.list_of_subreddit_classes.append(x)
			print x.getTopWeeklyPost()
		return self.list_of_subreddit_classes

	def getTopPosts(self):
		"""
		Returns submissions in a dictionary of lists that they can be linked to each subreddit.
		e.g. dict["teamName"] = [List: 0=TopWeeklyPost, 1=name]
		TODO: implement the above.
		Use generator expressions - http://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
		"""		
		for subreddit in nb.hockey_subs_TEMP:
			#self.subreddit[0] = sub url, self.subreddit[1] = sub name.
			nb.top_submissions[subreddit[0]] = [x for x in r.get_subreddit(subreddit[0]).get_top_from_week(limit=1)]
			nb.top_submissions[subreddit[0]].append(subreddit[1])

			#if hockey_subs is just a list of subreddit urls, if it is a tuple print the second value
			print "Finished getting data for " + (subreddit or subreddit[0] if subreddit[1] == False else subreddit[1])
			time.sleep(5) #29 teams, 5 second rest == 145sec wait.
		return self.top_submissions

	def formatPosts(self, posts):
		"""
		Takes getTopPosts() for input.  Returns a string.
		Formats the output into a bullet point list, with the title of each 
		thread linking to the thread itself.

		Idea: add a functin that sorts getTopPosts() in various ways, e.g. by karma, alphabetically, etc.
		As it stands, currently the first item in the list will be the bottom on the table.
		Would likely have to rewrite formatPosts() as well, can't hardcode in table.
		"""
		message = "Top posts for each hockey team's subreddit.\n\n"
		message = "Team [A-Z] | Post | Karma \n :---|:---|:---\n"
		for i in posts:
			message += "[](/" + i + ")" + "/r/" + i + "|" #adds team flair and subreddit link
			message += "[" + str(posts[i]).split(' :: ')[1] +"](" + str(posts[i].short_link) + ")"  + "|" #title and link
			message += str(posts[i]).split(' ::')[0] + "\n"
		return message

	def run(self):
		"""
		The bot logic, makes the bot post once week.  How is the best way to manage this?
		"""
		pass

	def makePost(self, subreddit, title):
		"""
		TODO: Use proper error catching for checking if not logged in.
		"""

		if not r.is_logged_in():
			print "Bot is not logged in.  Please login by typing r.login()."
		else:
			r.submit(subreddit, title, text=formy)

	def editSidebar(self, subreddit):
		pass

nb = NHLBot()
#posts = NHLBot.getTopPosts()
#formy = NHLBot.formatPosts(posts)