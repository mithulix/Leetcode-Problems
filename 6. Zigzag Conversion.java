class Solution {
    public String convert(String s, int n) {
        if(n == 1)
            return s ;
        String ans = "" ;
        int counter = 0 ;
        int direction = 0 ;
        char[][] arr = new char[n][1000];
        int pair = 0 ;
        l1:
        for(int i = 0 ; counter < s.length() ; i++ ) {
            if( direction == 0) {
                for(int j = 0 ; j < n && counter < s.length() ; j++) {
                    arr[j][i] = s.charAt(counter);
                    counter++ ;
                }
                direction = 1 ;
                pair += n-1 ;
                continue l1 ;
            } else {
                for(int j = n-2 ; j > 0 && counter < s.length(); j-- ) {
                    if( i + j == pair) {
                        arr[j][i] = s.charAt(counter);
                        counter++ ;
                        continue l1 ;
                    }
                }
                direction = 0 ;
                i-- ;
                continue l1 ;
            }
        }
        for(int i = 0 ; i < n ; i++) {
            for(char ch : arr[i]) {
                if(ch != '\u0000')
                    ans += ch ; 
            }
        }
        return ans ;
   }
}