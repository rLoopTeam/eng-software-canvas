
import time
import canvas

id_filter = ['100']

def main():
	
	receiver = canvas.init_receiver()
	sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	canvas.add_id(receiver, id_filter)

	message_id = "asdf"
	message_data = "Ping from node 1"

	while 1:
		#print to stdout. python's standard print can interfere with supervisord's
		#output and logging functionality in strange ways. 
		#please use this instead.
		canvas.print_out( "This is node 1" )
		canvas.send(sender, message_id, message_data)
	    	
		msg_id, data = canvas.recv(receiver)

		canvas.print_out("Node 1 recieved: %s" % data)
		time.sleep(5)

if __name__ == '__main__':
    main()
