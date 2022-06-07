import java.util.ArrayList;

public class CafeUtil{
    static int getStreakGoal() {
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            sum += i;
        }
        return sum;
    }

    static double getOrderTotal(double[] lineItems) {
        double sum = 0;
        for(int i = 0; i < lineItems.length; i++) {
           sum += lineItems[i];
        }
        return sum;
    }

    static void displayMenu(ArrayList<String> menu) {
        for(String item: menu) {
            System.out.println(item);
        }
    }

    static void addCustomer(ArrayList<String> customer) {
        System.out.println("Please Enter your name: " );
        String userName = System.console().readLine();
        System.out.println("Hello " + userName);
        System.out.printf("There are %s people in front of you", customer.size());
        customer.add(userName);

    }
}


