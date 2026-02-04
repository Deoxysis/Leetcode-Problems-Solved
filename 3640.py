class Solution {
    public long maxSumTrionic(int[] nums) {
        int n = nums.length;
        int i = 0;
        List<int[]> list = new ArrayList<>();

        while (i < n - 1) {
            int A = i;

            // first increasing
            if (nums[i] >= nums[i + 1]) {
                i++;
                continue;
            }
            while (i + 1 < n && nums[i] < nums[i + 1])
                i++;
            int B = i;

            // decreasing
            if (i + 1 >= n || nums[i] <= nums[i + 1]) {
                i = B;
                continue;
            }
            while (i + 1 < n && nums[i] > nums[i + 1])
                i++;
            int C = i;

            // second increasing
            if (i + 1 >= n || nums[i] >= nums[i + 1]) {
                i = C;
                continue;
            }
            while (i + 1 < n && nums[i] < nums[i + 1])
                i++;
            int D = i;

            // found maximal trionic block
            list.add(new int[] { A, B, C, D });

            // IMPORTANT: jump to start of 3rd segment
            i = C;
        }
        //print_list(list);
        return find_greatest(nums, list);
    }

    public static long find_greatest(int[] nums, List<int[]> list) {
        long maxx = Long.MIN_VALUE;
        for (int[] arr : list) {
            int a = arr[0];
            int b = arr[1];
            long suma = 0;
            long maxsuma= 0;
            for(int i = b - 2; i >= a; i--){
                suma += nums[i];
                if (suma > maxsuma){
                    maxsuma = suma;
                }
            }
            int c = arr[2];
            int d = arr[3];
            long sumc = 0;
            long maxsumc = 0;
            for(int i = c + 2; i <= d; i++){
                sumc += nums[i];
                if (sumc > maxsumc){
                    maxsumc = sumc;
                }
            }
            
            long sum = 0;
            for(int i = b - 1; i <= c+1; i++)
            {
                sum += nums[i];
            }
            
            maxx= Math.max(maxx, maxsuma + maxsumc + sum);
        }
        return maxx;
    }

    public void print_list(List<int[]> list) {
        for (int[] arr : list) {
            for (int num : arr) {
                System.out.print(num + ",");
            }
            System.out.println();
        }
    }
}
