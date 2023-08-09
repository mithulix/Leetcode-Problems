// dynamic programming
function soupServings(n: number): number {
    if (n >= 5000) return 1.0; // If n is large, the probability is close to 1.0
  
    n = Math.ceil(n / 25); // Convert to multiples of 25 for easier calculations
    const dp: number[][] = new Array(n + 1).fill(0).map(() => new Array(n + 1).fill(0));
  
    dp[0][0] = 0.5; // Initial probability of reaching state (0, 0) is 0.5
  
    for (let i = 1; i <= n; i++) {
      dp[i][0] = 0; // Probability of reaching state (i, 0) is 0 (B can't be empty first)
      dp[0][i] = 1; // Probability of reaching state (0, i) is 1 (A is empty first)
    }
  
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= n; j++) {
        dp[i][j] = 0.25 * (dp[Math.max(i - 4, 0)][j] + dp[Math.max(i - 3, 0)][Math.max(j - 1, 0)] + dp[Math.max(i - 2, 0)][Math.max(j - 2, 0)] + dp[Math.max(i - 1, 0)][Math.max(j - 3, 0)]);
      }
    }
  
    let result = dp[n][n]; // Probability of reaching state (n, n)
    for (let i = 1; i <= n; i++) {
      result += dp[Math.max(0, n - i)][0]; // Probability of reaching state (n-i, 0)
    }
  
    return result;
  }
  
  // Example usage:
  console.log(soupServings(50)); // Output: 0.62500
  console.log(soupServings(100)); // Output: 0.71875
  