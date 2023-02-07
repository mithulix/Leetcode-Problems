class Solution {
    public int totalFruit(int[] fruits) {
        int max = 0;
        int start = 0, end = 0;
        Map<Integer,Integer> map = new HashMap<>();
        while(end<fruits.length) {
            if(map.size() == 2 && !map.containsKey(fruits[end])) {
                while(map.size()== 2) {
                map.put(fruits[start],map.get(fruits[start])-1);
                    if(map.get(fruits[start]) == 0)
                        map.remove(fruits[start]);
                    start++;
                }
                map.put(fruits[end],map.getOrDefault(fruits[end],0)+1);
            }else 
                map.put(fruits[end],map.getOrDefault(fruits[end],0)+1);
            end++;
            max=Math.max(max,end-start);
            }
        return max;
    }
}