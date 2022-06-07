public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        
        // Menu variables (add yours below)
        double mochaPrice = 3.5;
        double dripCoffePrice = 4.75;
        double lattePrice = 6.25;
        double cappucinoPrice = 3.20;
    
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Sam";
        String customer3 = "Jimmy";
        String customer4 = "Noah";
    
        // Order completions (add yours below)
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = true;
        boolean isReadyOrder4 = false;
    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        if (isReadyOrder1) {
            System.out.println(generalGreeting + customer1 + pendingMessage);
        }

        if (isReadyOrder2) {
            double total = lattePrice * 2;
            System.out.println(generalGreeting + customer2 + pendingMessage + readyMessage + displayTotalMessage + total);
        }

        if (isReadyOrder3) {
            double total = 2;
            System.out.println(generalGreeting + customer3 + pendingMessage + readyMessage + displayTotalMessage + total);
        }

        if (isReadyOrder4) {
            System.out.println(generalGreeting + customer4 +  readyMessage + displayTotalMessage + cappucinoPrice);
        }
    }
}
