public class SimpleJava {
    public static int sumArray(int[] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        return sum;
    }

    public static boolean isEven(int number){
        return number%2 ==0;
    }

    public static void printOdds(int max){
        for (int i=1;i<=max;i++){
            if(i%2==1){
                System.out.println(i);
            }
        }
    }

    public static void main(String[] args) {
        int[] sampleArray = {1, 2, 3, 4, 5};
        System.out.println("Sum: " + sumArray(sampleArray));
        System.out.println("Is 4 even? " + isEven(4));
        printOdds(10);
    }
}
