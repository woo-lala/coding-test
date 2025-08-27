import java.util.*;

class Solution {
    
    static boolean visited[];
    static List<Integer> possible = new ArrayList<>();
    static int[][] edges;
    static int[] info;

    public int solution(int[] info, int[][] edges) {
        Solution.edges = edges;
        Solution.info = info;
        visited = new boolean[info.length];
        
        visited[0] = true;
        if (info[0] == 0) {
            backTrack(1, 0);
        } else {
            backTrack(0, 1);
        }
        
        return Collections.max(possible);
    }
    
    public void backTrack(int sheepCnt, int wolfCnt) {
        if (sheepCnt > wolfCnt) {
            possible.add(sheepCnt);
        } else {
            return;
        }
        
        for (int[] edge: edges) {
            int s = edge[0];
            int e = edge[1];
            if (visited[s] && !visited[e]) {
                visited[e] = true;
                if (info[e] == 0) {
                    backTrack(sheepCnt + 1, wolfCnt);
                } else {
                    backTrack(sheepCnt, wolfCnt + 1);
                }
                visited[e] = false;
            }
        }
        
        
        
    }
}