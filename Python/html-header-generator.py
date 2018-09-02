"""
heading_generator(title, heading_type)
heading_generator('Greeting', '1')
"""

def heading_generator(title, heading_type):
	return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator("hello", "1"))
print(heading_generator("goodbye", "5"))