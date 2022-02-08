public class App {
    //Do not edit this method ---------------------------------------------------
    public static void main(String[] args) throws Exception {
        int[] myUnsortedNumbers = {1,2,3,4,5,6,5,4,5,4,5,6,7,7,8,1,2,5,3,1,0,7,4,2};

        System.out.println("Run sort...");
        int[] completeNumbers = Sort(myUnsortedNumbers);
        System.out.println("...Sort complete");

        System.out.println("Validating...");
        boolean validationResponse = Validate(completeNumbers);
        if(validationResponse) {
            System.out.println("...Success!");
        }
        else {
            System.out.println("...sorry, try again!");
        }

        //Wait for enter to exit
        System.in.read();
    }
    //-------------------------------------------------------------------------

    // Create sorting method(s) here -------------------------------------------
    public static int[] Sort(int[] unsortedNumbers) {
        
        
        int[] mySortedNumbers = unsortedNumbers;
        return mySortedNumbers;
    }
    //-------------------------------------------------------------------------

    //Do not edit this method ---------------------------------------------------
    public static boolean Validate(int[] numbers) {
        int[] testNumbers = {0,1,1,1,2,2,2,3,3,4,4,4,4,5,5,5,5,6,6,7,7,7,8};

        if(testNumbers.length != numbers.length) {
            return false;
        }

        //It would be nice to use a sort here, but would give the game away!
        for(int i = 0; i <= numbers.length - 1; i++) {
            if(testNumbers[i] != numbers[i]) {
                return false;
            }
        }

        return true;
    }
    //-------------------------------------------------------------------------
}
