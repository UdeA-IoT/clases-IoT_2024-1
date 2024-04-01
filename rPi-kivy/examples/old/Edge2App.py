import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import paho.mqtt.client as mqtt
broker_address = "127.0.0.1"

class MyBox(BoxLayout):
	pass


class Edge2App(App):
	
	def build(self):
		return MyBox()
	
	def toggle_light(self):
		print("button pressed: publishing a message to the broker")
		self.client.publish("Light/0","2")
	
		
	def on_start(self):
		
		def on_message(client, userdata, message):
			print("message received",  str(message.payload.decode("utf-8")))
			print("message topic", message.topic)
			userdata['self'].root.ids.temp_lbl.text = str(message.payload.decode("utf-8"))
		
		parameters = {'self':self}
		self.client = mqtt.Client(client_id='p1',
									clean_session = True,
									userdata = parameters)
		self.client.connect(broker_address)
		self.client.on_message = on_message
		self.client.loop_start()
		print("Subscribing to a topic")
		self.client.subscribe("home")
		
	
if __name__ == "__main__":
	Edge2App().run()
