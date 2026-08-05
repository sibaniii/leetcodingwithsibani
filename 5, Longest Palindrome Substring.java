class Solution {
    public String longestPalindrome(String s) {
        String ans = "";
        int n = s.length();

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {

                String sub = s.substring(i, j);

                int left = 0;
                int right = sub.length() - 1;
                boolean isPal = true;

                while (left < right) {
                    if (sub.charAt(left) != sub.charAt(right)) {
                        isPal = false;
                        break;
                    }
                    left++;
                    right--;
                }

                if (isPal && sub.length() > ans.length()) {
                    ans = sub;
                }
            }
        }

        return ans;
    }
}
