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
        double hotLatte = 4.75;
        double hotAmericano = 6.25;
        double chaiLatte = 3.20;
    
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "John";
        String customer3 = "Michael";
        String customer4 = "Andrew";
    
        // Order completions (add yours below)
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = true;
        boolean isReadyOrder4 = false;
    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        if (isReadyOrder1) {
            System.out.println(generalGreeting + customer1 + readyMessage + displayTotalMessage + mochaPrice);
        }

        if (isReadyOrder2) {
            System.out.println(generalGreeting + customer2 + pendingMessage + readyMessage + displayTotalMessage + hotLatte);
        }

        if (isReadyOrder3) {
            System.out.println(generalGreeting + customer3 + pendingMessage + readyMessage + displayTotalMessage + hotAmericano);
        }

        if (isReadyOrder4) {
            System.out.println(generalGreeting + customer4 + pendingMessage + readyMessage + displayTotalMessage + chaiLatte);
        }
    }
}
