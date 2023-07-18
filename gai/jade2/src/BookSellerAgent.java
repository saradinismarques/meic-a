package jadelab2;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.*;
import jade.lang.acl.ACLMessage;
import jade.lang.acl.MessageTemplate;
import jade.domain.DFService;
import jade.domain.FIPAException;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;

import java.util.*;

public class BookSellerAgent extends Agent {
	private Hashtable catalogue;
	private BookSellerGui myGui;
	private Hashtable shippingCosts;

	private Hashtable<String, Long> reservedBooks;
	protected void setup() {
		catalogue = new Hashtable();
		myGui = new BookSellerGui(this);
		shippingCosts = new Hashtable();
		reservedBooks = new Hashtable<String, Long>();
		int interval = 20000;

		myGui.display();

		//book selling service registration at DF
		DFAgentDescription dfd = new DFAgentDescription();
		dfd.setName(getAID());
		ServiceDescription sd = new ServiceDescription();
		sd.setType("book-selling");
		sd.setName("JADE-book-trading");
		dfd.addServices(sd);
		try {
			DFService.register(this, dfd);
		}
		catch (FIPAException fe) {
			fe.printStackTrace();
		}

		addBehaviour(new OfferRequestsServer());

		addBehaviour(new PurchaseOrdersServer());

		addBehaviour(new TickerBehaviour(this, interval)
		{
			protected void onTick()
			{
				for (Map.Entry<String,Long> entry : reservedBooks.entrySet()) {
					long currentTime = System.currentTimeMillis();

					if(currentTime-entry.getValue() > 10000)
						reservedBooks.remove(entry.getKey());
				}
			}

		});
	}

	protected void takeDown() {
		//book selling service deregistration at DF
		try {
			DFService.deregister(this);
		}
		catch (FIPAException fe) {
			fe.printStackTrace();
		}
		myGui.dispose();
		System.out.println("Seller agent " + getAID().getName() + " terminated.");
	}

	//invoked from GUI, when a new book is added to the catalogue
	public void updateCatalogue(final String title, final int price) {
		addBehaviour(new OneShotBehaviour() {
			public void action() {
				catalogue.put(title, new Integer(price));
				System.out.println(getAID().getLocalName() + ": " + title + " put into the catalogue. Price = " + price);
			}
		} );
	}

	public void updateShippingCosts(final String title, final int shippingCost) {
		addBehaviour(new OneShotBehaviour() {
			public void action() {
				shippingCosts.put(title, new Integer(shippingCost));
				System.out.println(getAID().getLocalName() + ": " + title + " added shipping cost = " + shippingCost);
			}
		} );
	}

	private class OfferRequestsServer extends CyclicBehaviour {
		public void action() {
			//proposals only template
			MessageTemplate mt = MessageTemplate.MatchPerformative(ACLMessage.CFP);
			ACLMessage msg = myAgent.receive(mt);
			if (msg != null) {
				String title = msg.getContent();
				ACLMessage reply = msg.createReply();
				Integer price = (Integer) catalogue.get(title);
				Integer shippingCost = (Integer) shippingCosts.get(title);
				long startTime = System.currentTimeMillis();

				if (price != null && reservedBooks.get(title) == null) {
					//title found in the catalogue, respond with its price as a proposal
					reply.setPerformative(ACLMessage.PROPOSE);
					reply.setContent(String.valueOf(price.intValue()+shippingCost.intValue()));
					reservedBooks.put(title, startTime);
				}
				else {
					//title not found in the catalogue
					reply.setPerformative(ACLMessage.REFUSE);
					reply.setContent("not-available");
				}
				myAgent.send(reply);
			}
			else {
				block();
			}
		}
	}


	private class PurchaseOrdersServer extends CyclicBehaviour {
		public void action() {
			//purchase order as proposal acceptance only template
			MessageTemplate mt = MessageTemplate.MatchPerformative(ACLMessage.ACCEPT_PROPOSAL);
			ACLMessage msg = myAgent.receive(mt);
			if (msg != null) {
				String title = msg.getContent();
				ACLMessage reply = msg.createReply();

				Integer price = (Integer) catalogue.remove(title);
				if (price != null) {
					reply.setPerformative(ACLMessage.INFORM);
					System.out.println(getAID().getLocalName() + ": " + title + " sold to " + msg.getSender().getLocalName());
					reservedBooks.remove(title);
				}
				else {
					//title not found in the catalogue, sold to another agent in the meantime (after proposal submission)
					reply.setPerformative(ACLMessage.FAILURE);
					reply.setContent("not-available");
				}
				myAgent.send(reply);
			}
			else {
				block();
			}
		}
	}
}
