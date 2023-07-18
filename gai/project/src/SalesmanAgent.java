package mtsp;

import jade.core.Agent;
import jade.core.behaviours.*;
import jade.lang.acl.ACLMessage;
import jade.lang.acl.MessageTemplate;
import org.jgrapht.*;
import org.jgrapht.graph.*;
import java.util.Random;

public class SalesmanAgent extends Agent {

	private String currentLocation;
	private Graph<String, DefaultWeightedEdge> graph;


	protected void setup() {
		MyAgent myAgent = new MyAgent();

		// Initialize the agent
		System.out.println("Salesman agent " + getAID().getName() + " is ready.");

		// Set initial location randomly
		currentLocation = graph.myAgent.getRandomLocation();

		// Add a behavior for message handling
		addBehaviour(new HandleMessagesBehaviour());
		// Create the graph object
		graph = new SimpleDirectedWeightedGraph<>(DefaultWeightedEdge.class);

		// Add vertices for each location
		for (String location : graph.getLocations()) {
			graph.addVertex(location);
		}

		// Add weighted edges between locations based on distances
		for (String location1 : graph.getLocations()) {
			for (String location2 : graph.getLocations()) {
				if (!location1.equals(location2)) {
					double distance = graph.getDistance(location1, location2);
					DefaultWeightedEdge edge = graph.addEdge(location1, location2);
					graph.setEdgeWeight(edge, distance);
				}
			}
		}

	}

	private class HandleMessagesBehaviour extends CyclicBehaviour {

		public void action() {
			// Receive messages
			ACLMessage msg = receive(MessageTemplate.MatchPerformative(ACLMessage.INFORM));
			if (msg != null) {
				// Process received message
				String content = msg.getContent();
				String[] locations = content.split(",");

				// Update current location based on the received message
				updateLocation(locations);

				// Send a reply message
				ACLMessage reply = msg.createReply();
				reply.setPerformative(ACLMessage.INFORM);
				reply.setContent("Location updated");
				send(reply);
			} else {
				block();
			}
		}
	}

	private void updateLocation(String[] locations) {
		String nextLocation = findNextLocation(locations);
		if (nextLocation != null) {
			currentLocation = nextLocation;
			System.out.println(getAID().getName() + " moved to " + currentLocation);
		}
	}

	private String findNextLocation(String[] locations) {
		String currentLocation = getCurrentLocation();

		// Check if all locations have been visited
		if (locations.length == graph.getNumberOfLocations()) {
			return currentLocation; // Return to the starting location
		}

		// Initialize variables
		double minDistance = Double.MAX_VALUE;
		String nextLocation = null;

		// Find the nearest unvisited location
		for (String location : locations) {
			if (!location.equals(currentLocation)) {
				double distance = graph.getDistance(currentLocation, location);
				if (distance < minDistance) {
					minDistance = distance;
					nextLocation = location;
				}
			}
		}

		return nextLocation;
	}
}
