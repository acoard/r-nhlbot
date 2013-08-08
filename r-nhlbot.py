#reddit bot for /r/nhl
import praw
import time

r = praw.Reddit("User Agent: NHLBot for /r/hockey. v1.0 created by /u/acoard")
nb = "NHLBot"

class NHLBot:
	hockey_subs = ['canucks', "anaheimducks", "calgaryflames", "losangeleskings", 
			"coyotes", "sanjosesharks", "hawks", "coloradoavalanche", "dallasstars", 
			"wildhockey", "predators", "stlouisblues", "winnipegjets", "canes", "bluejackets", 
			"devils", "newyorkislanders", "rangers", "flyers", "penguins", "caps", "bostonbruins", 
			"sabres", "detroitredwings", "floridapanthers", "habs", "ottawasenators", "tampabaylightning", "leafs"]
	hockey_subs_TEMP = ['canucks', 'leafs', 'flyers']

	def getTopPosts(self):
		"""
		Returns submissions in a dictionary so that they can be linked to each subreddit.
		e.g. dict["teamName"] = TopWeeklyPost
		"""
		numberOfSubmissions = 1
		top_submissions = dict() 
		for subreddit in self.hockey_subs_TEMP: #DEV only
			top_submissions[subreddit] = [x for x in r.get_subreddit(subreddit).get_top_from_week(limit=numberOfSubmissions)][0]
			print "Finished getting data for " + subreddit
			time.sleep(5) #29 teams, 5 second rest == 145sec wait.
		return top_submissions

	def formatPosts(self, posts):
		"""
		Takes getTopPosts() for input.  Returns a string.
		Formats the output into a bullet point list, with the title of each 
		thread linking to the thread itself.

		Idea: add a functin that sorts getTopPosts() in various ways, e.g. by karma, alphabetically, etc.
		Would likely have to rewrite formatPosts() as well, can't hardcode in table.
		"""
		message = "Top posts for each hockey team's subreddit.\n\n"
		message = "Team [A-Z] | Post | Karma \n :---|:---|:---\n"
		for i in posts:
			message += "[](/" + i + ")" + "/r/" + i + "|" #adds team flair and subreddit link
			message += "[" + str(posts[i]).split(' :: ')[1] +"](" + str(posts[i].short_link) + ")"  + "|" #title and link
			message += str(posts[i]).split(' ::')[0] + "\n"

		#Original code.
		# for i in posts:
		# 	message += "* " + str(i) + ": " + "[" + str(posts[i]).split(' :: ')[1] +"](" + str(posts[i].short_link) + ")" \
		# 	+ " with a karma of " + str(posts[i]).split(' ::')[0] + "\n\n"
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

NHLBot = NHLBot()
posts = NHLBot.getTopPosts()
formy = NHLBot.formatPosts(posts)