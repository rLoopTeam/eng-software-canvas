
import time
import canvas

#list of message identifiers we want to receive on this node
receive_message_ids = ['200', '7', 'asdf']

def main():
	
	#init canvas sender and receiver
	receiver = canvas.init_receiver()
	sender = canvas.init_sender()
	time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

	#add message id filters on receiver
	canvas.add_id(receiver, receive_message_ids)

	#remove message id filters on receiver (add and remove only take lists for now..)
	canvas.rm_id(receiver, ["7"])

	#you have 2 ways of making CAN messages:
	#either just make 2 strings
	message_id = "100"
	message_data = "Ping from node 2"
	#or a canvas "message"
	message = canvas.msg("100", "Hi it's node 2 again")

	while 1:
		#print to stdout. python's standard print can interfere with supervisord's
		#output and logging functionality in strange ways. 
		#please use this instead.
		canvas.print_out( "This is node 2" )

		#send message on the CAN bus
		canvas.send(sender, message_id, message_data)
		canvas.send_msg(sender, message)	    	

		#you can change a canvas message like this
		message.id = "101"
		message.data="Node 1 should not see this now"

		#receive message from CAN bus (only returns messages that this node has subscribed to)
		#this call will block untill a message is received
		msg_id, msg_data = canvas.recv(receiver)

		#print message to stdout
		canvas.print_out("Node 2 recieved: %s %s" % (msg_id, msg_data))

		#non-blocking receive call (only returns messages that this node has subscribed to) 
		#will return "no_id", "no_message" if no message was received
		msg_id, msg_data = canvas.recv_noblock(receiver)		
		canvas.print_out("Node 2 recieved: %s %s" % (msg_id, msg_data))

		#sleep node for 5 second
		time.sleep(5)

if __name__ == '__main__':
    main()
