package mtsp;

import jade.core.Agent;
import jade.core.behaviours.CyclicBehaviour;
import jade.lang.acl.ACLMessage;
import jade.lang.acl.MessageTemplate;
import org.jgrapht.*;
import org.jgrapht.graph.*;
import java.util.Random;
import java.util.Set;
import java.util.ArrayList;
import java.util.List;

public class MyAgent extends Agent {

    private Graph graph;
    private String currentLocation;
    private List<String> locations;

    protected void setup() {
        // Initialize the agent
        System.out.println("Agent " + getLocalName() + " is ready.");

        locations = new ArrayList<>();
        // Add your locations to the 'locations' list
        locations.add("Location1");
        locations.add("Location2");
        locations.add("Location3");

        currentLocation = getRandomLocation();

        addBehaviour(new MessageHandlerBehaviour());
        addBehaviour(new MovementBehaviour());
    }

    protected void takeDown() {
        System.out.println("Agent " + getLocalName() + " is terminating.");
    }

    public static String getRandomLocation() {
        int randomIndex = new Random().nextInt(locations.size());
        return locations.get(randomIndex);
    }


    private class MessageHandlerBehaviour extends CyclicBehaviour {

        public void action() {
            // Message handling logic
            ACLMessage msg = receive(MessageTemplate.MatchPerformative(ACLMessage.REQUEST));
            if (msg != null) {
                // Process the received message
                String content = msg.getContent();

                // Update agent's current location
                currentLocation = getRandomLocation();

                // Reply to the message
                ACLMessage reply = msg.createReply();
                reply.setPerformative(ACLMessage.INFORM);
                reply.setContent("Agent " + getLocalName() + " moved to " + currentLocation);
                send(reply);
            } else {
                block();
            }
        }
    }

    private class MovementBehaviour extends CyclicBehaviour {

        public void action() {

            String nextLocation = getRandomLocation();

            currentLocation = nextLocation;

            System.out.println("Agent " + getLocalName() + " is at location " + currentLocation);


            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
