package jadelab1;

import jade.core.*;
import jade.core.behaviours.*;
import jade.lang.acl.*;
import jade.domain.*;
import jade.domain.FIPAAgentManagement.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.HashMap;
public class MyAgent extends Agent {
	protected void setup () {
		displayResponse("Hello, I am " + getAID().getLocalName());
		addBehaviour(new MyCyclicBehaviour(this));
		//doDelete();
	}
	protected void takeDown() {
		displayResponse("See you");
	}
	public void displayResponse(String message) {
		JOptionPane.showMessageDialog(null,message,"Message",JOptionPane.PLAIN_MESSAGE);
	}
	public void displayHtmlResponse(String html) {
		JTextPane tp = new JTextPane();
		JScrollPane js = new JScrollPane();
		js.getViewport().add(tp);
		JFrame jf = new JFrame();
		jf.getContentPane().add(js);
		jf.pack();
		jf.setSize(400,500);
		jf.setVisible(true);
		tp.setContentType("text/html");
		tp.setEditable(false);
		tp.setText(html);
	}
}

class MyCyclicBehaviour extends CyclicBehaviour {
	MyAgent myAgent;
	int messageCounter;
	HashMap<Integer, String> storage;
	public MyCyclicBehaviour(MyAgent myAgent) {
		this.myAgent = myAgent;
		this.messageCounter = 0;
		this.storage = new HashMap<Integer, String>();
	}
	public void action() {
		ACLMessage message = myAgent.receive();
		if (message == null) {
			block();
		} else {
			String ontology = message.getOntology();
			String content = message.getContent();
			String inReplyTo = message.getInReplyTo();
			int performative = message.getPerformative();

			if (performative == ACLMessage.REQUEST)
			{
				messageCounter++;
				storage.put(messageCounter, content);
				//I cannot answer but I will search for someone who can
				DFAgentDescription dfad = new DFAgentDescription();
				ServiceDescription sd = new ServiceDescription();
				sd.setName("service");
				dfad.addServices(sd);
				try
				{
					DFAgentDescription[] result = DFService.search(myAgent, dfad);
					if (result.length == 0) myAgent.displayResponse("No service has been found ...");
					else
					{
						String foundAgent = result[0].getName().getLocalName();
						myAgent.displayResponse("Agent " + foundAgent + " is a service provider. Sending message to " + foundAgent);
						ACLMessage forward = new ACLMessage(ACLMessage.REQUEST);
						forward.addReceiver(new AID(foundAgent, AID.ISLOCALNAME));
						forward.setContent(content);
						forward.setOntology(ontology);
						forward.setReplyWith(String.valueOf(messageCounter));
						myAgent.send(forward);
					}
				}
				catch (FIPAException ex)
				{
					ex.printStackTrace();
					myAgent.displayResponse("Problem occured while searching for a service ...");
				}
			}
			else
			{	//when it is an answer

				String response = storage.get(Integer.valueOf(inReplyTo));

				myAgent.displayHtmlResponse(response + content);
			}
		}
	}
}
