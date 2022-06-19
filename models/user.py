class User(object):
	"""docstring for User"""
	def __init__(self):
		super(User, self).__init__()
		self.city = ''
		self.destinationId = ''
		self.hotelCount = ''
		self.img = False
		self.imgCount = ''
		self.low = False

	def set_city(self, city):
		self.city = city

	def set_destinationId(self, destinationId):
		self.destinationId = destinationId
		
	def set_hotel_count(self, hotelCount):
		self.hotelCount = hotelCount

	def set_img_count(self, imgCount):
		self.imgCount = imgCount

	def set_low(self, low):
		self.low = low

	def set_img(self, img):
		self.img = img

data = User()

def get_data():
	global data
	return data

def set_data(d):
	global data
	data = d