import web
import sqlite3



urls = (
	"/messages", "Message",
	"/", "UIRedirect"
)



class Message:
	
	def GET(self):
		
		conn = sqlite3.connect("chat.db")
		c = conn.cursor()
		ret = "["
		for row in reversed(list(c.execute("SELECT * FROM chat"))):
			print row
			ret+="\""+row[0]+"\","
		ret +="\"nope\"]"
		conn.close()
		return ret
	
	def POST(self):
		conn = sqlite3.connect("chat.db")
		c = conn.cursor()
		message = web.input()["message"]
		print message
		c.execute("INSERT INTO chat VALUES(?)", (message,))
		conn.commit()
		conn.close()
		
		

class UIRedirect:
	def GET(self):
		return web.redirect("/static/ui.html")


app = web.application(urls, globals())


if __name__ == "__main__":
	try:
		conn = sqlite3.connect("chat.db")
		c = conn.cursor()
		c.execute("CREATE TABLE chat (message text)")
		conn.close()
	except sqlite3.OperationalError:
		pass
	
	app.run()
	