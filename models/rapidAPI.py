class Entitie(object):
	
	def __init__(self, caption, destinationId, name, _type):
		super(Entitie, self).__init__()
		self.caption = caption
		self.destinationId = destinationId
		self.name = name
		self.type = _type

class Hotel(object):
	"""docstring for Hotel"""
	def __init__(self, id, name, starRating, price, address, landmark):
		super(Hotel, self).__init__()
		self.id = id
		self.name = name
		self.starRating = starRating
		self.price = price
		self.landmark = landmark
		self.address = address