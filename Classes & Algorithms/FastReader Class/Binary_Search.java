public class Binary_Search {
    public static void main(String[] args) {
        
        int binary_search(int arr[], int size, int key) {

            int low = 0, high = size - 1, mid;
         
            while (low <= high) {
         
               mid = (low + high) >> 1;
         
               if (key = arr[mid]) return mid;
         
               else if (key > arr[mid]) low = mid + 1;
         
               else high = mid - 1;
         
            }
         
            return -1; // not found
         
         }
         
         // Complexity: O ( log2 ( N ) )
    }
}