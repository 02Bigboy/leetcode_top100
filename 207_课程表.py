# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

# 这个代码写的挺好的
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 有向无环图，只能选入度为0 的课
        from collections import defaultdict
        from collections import deque
        # 入度数组(列表，保存所有课程的依赖课程总数)
        in_degree_list = [0] * numCourses
        # 关系表(字典，保存所有课程与依赖课程的关系)
        relation_dict = defaultdict(list)
        for i in prerequisites:
            # 保存课程初始入度值
            in_degree_list[i[0]] += 1
            # 添加依赖它的后续课程
            relation_dict[i[1]].append(i[0])
        queue = deque()
        for i in range(len(in_degree_list)):
            # 入度为0的课程入列
            if in_degree_list[i] == 0:
                queue.append(i)
        # 队列只存储入度为0的课程，也就是可以直接选修的课程
        while queue:
            current = queue.popleft()
            # 选修课程-1
            numCourses -= 1
            relation_list = relation_dict[current]
            # 如果有依赖此课程的后续课程则更新入度
            if relation_list:
                for i in relation_list:
                    in_degree_list[i] -= 1   # 有依赖则更新入度
                    # 后续课程除去当前课程无其他依赖课程则丢入队列
                    if in_degree_list[i] == 0:
                        queue.append(i)
        return numCourses == 0
    

class Solve:
    '''
    思想：就是将课的关系弄成图额关系---有向无环图
    每次只能选入度为0的课，选了课之后需要更新一下与选的课相关的其他课的入度
    '''
    def canfinish(numCourses, prerequisites):
        from collections import defaultdict
        from collections import deque      # 双端队列
        input_degree = [0] * numCourses
        relation_list = defaultdict(list)
        for i in prerequisites:
            input_degree[i[0]] += 1
            relation_list[i[1]].append(i[0])
        queue = deque()
        for i in range(len(input_degree)):
            # 入度为0 的课程如列
            if input_degree[i] == 0:
                queue.append(i)
        while queue:
            cur_sourse = queue.popleft()
            numCourses -= 1  # 选修课减1
            relation = relation_list[cur_sourse]
            if relation:
                for i in relation:
                    input_degree[i] -= 1
                    if input_degree[i] == 0:
                        queue.append(i)
        return numCourses == 0



