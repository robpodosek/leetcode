#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its list of prereqs
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        # Create a set of all visited course nodes
        visitedSet = set()

        def dfs(course):
            # Check base cases
            if course in visitedSet:
                return False
            if preMap == []:
                return True

            visitedSet.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visitedSet.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

# @lc code=end
