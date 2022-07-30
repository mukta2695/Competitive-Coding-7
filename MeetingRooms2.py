import heapq as heap
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        '''
        1. First sort on the basis of the start time
        2. Maintain a min heap of end times
        3. Now traverse through the intervals and compare the start time of the new meeting with the end time of the on going meeting that is the heap root.
        4. If new start time >= old end time ---> pop the min end and push new end time (Allocate the same room)
        5. Else just push (Allocate different room)
        '''
        #Time Complexity: O(n logn) --> sorting
        #Space Complexity: O(n)
        #Edge case
        if len(intervals) ==0 :
            return 0
        #Sorting based on the start time
        intervals.sort(key= lambda x : x[0])
        
        minheap=[]
        heap.heappush(minheap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            currendtime=minheap[0]
            if intervals[i][0] >= currendtime:
                heap.heappop(minheap)
                heap.heappush(minheap, intervals[i][1])
            else:
                heap.heappush(minheap, intervals[i][1])
                
        return len(minheap)
