class Time():
	def __init__(self, hour, minute, second):
		self.hours = hour
		self.minutes = minute
		self.seconds = second
		self.time = second + 60 * minute + 60 ** 2 * hour

	def __add__(self, other):
		if isinstance(other, Time):
			tem = self.time + other.time
			hour = tem // 60 ** 2
			minute = (tem % 60 ** 2) // 60
			second = (tem % 60 ** 2) % 60
			return hour, minute, second
		elif isinstance(other, float) or isinstance(other, int):
			tem = int(self.time - other)
			hour = tem // 60 ** 2
			minute = (tem % 60 ** 2) // 60
			second = (tem % 60 ** 2) % 60
			return hour, minute, second
		else:
			raise TypeError

	def __getattribute__(self, item):
		print(item)
		return super().__getattribute__(item)

	def __getattr__(self, item):
		print(f'get{item}')
		return super().__getattribute__()

	def __repr__(self):
		return f'{self.hours}.{self.minutes}.{self.seconds}'


now = Time(15, 4, 13)

after = Time(15, 5, 12)
print(after + now)
# print(after - now) #which is -