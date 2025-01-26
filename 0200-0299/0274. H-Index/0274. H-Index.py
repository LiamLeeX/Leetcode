class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # Create a counting array to store the frequency of citations
        # We only need to count up to n+1 because h-index can't be larger than n
        count = [0] * (n + 1)

        # Count the frequency of citations
        # If citation count is greater than n, we count it as n
        for citation in citations:
            if citation >= n:
                count[n] += 1
            else:
                count[citation] += 1

        # Start from the highest possible h-index (n)
        # and accumulate the count of papers
        total = 0
        for i in range(n, -1, -1):
            total += count[i]
            # If we find h papers with at least h citations
            if total >= i:
                return i

        return 0

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = [0] * (len(citations)+1) # count存储的是index引用数上有个value篇论文
        for citation in citations:
            count[min(len(citations),citation)] +=1
        total = 0
        for i in range(len(citations),-1,1):
            total += count[i] # 这里的total是论文数目
            if total >=i:
                return i