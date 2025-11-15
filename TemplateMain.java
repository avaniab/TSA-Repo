import java.util.Scanner;

public class Template {
    public static void main(String[] args) {
         Scanner console = new Scanner(System.in);
         int columns = console.nextInt();
         int rows = console.nextInt();
         console.nextLine(); 
         String inputString = console.nextLine();
         int[] array = processInput(inputString);
         char exampleChar = 'A';
         performOperations(columns, rows, array, charValue);
         console.close();
     }
     private static int[] processInput(String input) { //array of integers 
         String[] parts = input.split(" ");
         int[] result = new int[parts.length];
         for (int i = 0; i < parts.length; i++) {
             result[i] = Integer.parseInt(parts[i]);
         }
         return result;
     }
     private static void performOperations(int columns, int rows, int[] array) {
         for (int value : array) {
             System.out.println("Value: " + value);
         }
         if (columns > 0 && rows > 0) {
             System.out.println("Valid dimensions.");
         } else {
             System.out.println("Invalid dimensions.");
         }
     }
     private static String generateAndEncryptString(int length, int shift) {
        Random randomString = generateRandomString(length);
        // encrypt the string using caesar cipher
        StringBuilder encryptedString = new StringBuilder();
        for (int i = 0; i < randomString.length(); i++) {
            char originalChar = randomString.charAt(i);
            char encryptedChar = (char) ((originalChar - 'A' + shift) % 26 + 'A'); // caesar cipher shift
            encryptedString.append(encryptedChar);
        }
    
        return encryptedString.toString();
    }
    private static Random generateRandomString(int length) {
        StringBuilder randomString = new StringBuilder();
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            char randomChar = (char) ('A' + random.nextInt(26)); // generate random uppercase letter
            randomString.append(randomChar);
        }
        return randomString.toString();
    }
 }