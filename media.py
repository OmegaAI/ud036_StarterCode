import webbrowser

class Movie():
	
	def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
		# Init function for Movie class.
		self.title = movie_title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def showtrailer(self):
		#Use webbrowser library to open the url and play movie trailer
		webbrowser.open(self.trailer)