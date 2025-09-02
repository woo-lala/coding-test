import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        
        int before = 0;
        int cnt = 0;
        Arrays.sort(targets, (o1, o2) -> o1[1] - o2[1]);
        
        for(int [] target: targets) {
            if (target[0] >= before){
                before = target[1];
                cnt++;
            }
        }
        
        return cnt;
    }
}