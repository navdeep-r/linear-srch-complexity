def calculatePrefixMaxSum(nums):
    n = len(nums) - 1
    prefixMaxSum = [0] * (n + 1)
    currentMax = nums[1]
    prefixMaxSum[1] = nums[1]

    for i in range(2, n + 1):
        currentMax = max(0, nums[i], currentMax + nums[i])
        prefixMaxSum[i] = currentMax

    return prefixMaxSum

def calculateSuffixMaxSum(nums):
    n = len(nums) - 1
    suffixMaxSum = [0] * (n + 1)
    currentMax = nums[n]
    suffixMaxSum[n] = nums[n]

    for i in range(n - 1, 0, -1):
        currentMax = max(0, nums[i], currentMax + nums[i])
        suffixMaxSum[i] = currentMax

    return suffixMaxSum

def maxTwoNonOverlappingSubarraysSum(nums):
    n = len(nums) - 1
    if n == 0:
        return 0

    prefixMaxSum = calculatePrefixMaxSum(nums)
    suffixMaxSum = calculateSuffixMaxSum(nums)

    maxPrefixSum = [0] * (n + 2)
    maxPrefixSum[1] = prefixMaxSum[1]
    for i in range(2, n + 1):
        maxPrefixSum[i] = max(maxPrefixSum[i - 1], prefixMaxSum[i])

    maxSuffixSum = [0] * (n + 2)
    maxSuffixSum[n] = suffixMaxSum[n]
    for i in range(n - 1, 0, -1):
        maxSuffixSum[i] = max(maxSuffixSum[i + 1], suffixMaxSum[i])

    maxSum = 0
    for i in range(n + 1):
        maxSum = max(maxSum, maxPrefixSum[i] + maxSuffixSum[i + 1])

    return maxSum

if __name__ == "__main__":
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    print("Maximum sum of two non-overlapping subarrays:", maxTwoNonOverlappingSubarraysSum(nums))
