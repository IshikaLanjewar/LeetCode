import java.util.*;

public class p2 {
    public static List<Integer> findDuplicates(List<Integer> list) {
        Set<Integer> seen = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();

        for (int num : list) {
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }

        return new ArrayList<>(duplicates);
    }

    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 2, 3, 4, 4, 5);
        System.out.println(findDuplicates(numbers));
    }
}
