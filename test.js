var findAnagrams = function (s, p) {
    const chars = new Array(26).fill(0), res = [];
    
    for(let i = 0; i < p.length; i++) {
        chars[p.charCodeAt(i) - 97]--;
    }
    
    main:
    for(let i = 0; i < s.length; i++){
        chars[s.charCodeAt(i) - 97]++;

        if(i < p.length - 1) continue;
        if(i > p.length - 1) chars[s.charCodeAt(i - p.length) - 97]--;

        for(let j = 0; j < 26; j++){
            if(chars[j]) continue main;
        }
        
        res.push(i - p.length + 1);
    }
    
    return res;
};