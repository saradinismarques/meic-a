package mtsp;

import jade.core.Runtime;
import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.lang.acl.MessageTemplate;
import jade.wrapper.AgentContainer;
import jade.wrapper.AgentController;
import jade.lang.acl.ACLMessage;
import jade.wrapper.ControllerException;
import org.jgrapht.*;

import java.util.HashSet;
import java.util.Set;
import org.jgrapht.graph.*;
import java.util.Random;


public class MTSPSimulation {

    private AgentContainer agentContainer;
    private int numAgents;
    private Graph graph; 

    public MTSPSimulation(int numAgents) {
        this.numAgents = numAgents;
    }

    public void startSimulation() throws ControllerException {
        MyAgent myAgent = new MyAgent();

        // Initialize JADE runtime
        Runtime runtime = Runtime.instance();
        Profile profile = new ProfileImpl();
        agentContainer = runtime.createMainContainer(profile);



        // Create agents and assign random starting locations
        for (int i = 0; i < numAgents; i++) {
            createSalesmanAgent("SalesmanAgent" + i, myAgent.getRandomLocation());
        }

        // Start the simulation loop
        while (!isTerminationConditionMet()) {
            // Move agents and update their state
            moveAgents();
        }

        // Terminate the simulation
        runtime.shutDown();
    }

    private void createSalesmanAgent(String agentName, String startingLocation) {
        try {
            AgentController agentController = agentContainer.createNewAgent(agentName, SalesmanAgent.class.getName(), null);
            agentController.start();
            sendStartingLocation(agentName, startingLocation);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void sendStartingLocation(String agentName, String startingLocation) throws ControllerException {
        // Send a message to the agent with its starting location
        ACLMessage msg = new ACLMessage(ACLMessage.INFORM);
        msg.setContent(startingLocation);
        msg.addReceiver(agentContainer.getAgent(agentName).getAID());
        agentContainer.post(msg);
    }

    private boolean isTerminationConditionMet() {
        // Create a set to keep track of visited locations
        Set<String> visitedLocations = new HashSet<>();

        // Iterate over all agents
        SalesmanAgent[] agents = new SalesmanAgent[0];
        for (SalesmanAgent agent : agents) {
            // Get the current location of the agent
            String agentLocation = agent.getCurrentLocation();

            // Check if the agent's location is already visited
            if (visitedLocations.contains(agentLocation)) {
                continue; // Move to the next agent
            }

            // Add the agent's location to the visited set
            visitedLocations.add(agentLocation);

            // Check if all locations have been visited
            if (visitedLocations.size() == graph.getNumberOfLocations()) {
                return true; // Termination condition met
            }
        }

        return false; // Termination condition not met
    }


    private void moveAgents() throws ControllerException {
        for (int i = 0; i < numAgents; i++) {
            String agentName = "SalesmanAgent" + i;

            // Send a message to the agent to trigger movement
            ACLMessage msg = new ACLMessage(ACLMessage.REQUEST);
            msg.setContent("Move"); // You can define your own message content
            msg.addReceiver(agentContainer.getAgent(agentName).agentController());
            agentContainer.send(msg);

            // Wait for the reply from the agent
            ACLMessage reply = agentContainer.getAgent(agentName).receive(MessageTemplate.MatchPerformative(ACLMessage.INFORM));
            if (reply != null) {
                // Process the reply message if needed
            }
        }
    }

}
