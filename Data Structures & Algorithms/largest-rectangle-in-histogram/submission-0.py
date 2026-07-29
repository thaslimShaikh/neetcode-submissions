class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            left = i 
            while left > 0 and heights[left-1]>=heights[i]:
                left -= 1 
            right = i 
            while right<len(heights)-1 and heights[right+1]>=heights[i]:
                right +=1
            width = right-left+1
            area=heights[i]*width
            maxArea = max(area, maxArea)
        return maxArea