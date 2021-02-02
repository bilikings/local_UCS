import pointIdUtil
import roadIdUtil
import stringFacory
from queue import PriorityQueue as PQ

path_map = {}
path_point = []
path_road = []


# 定义一个可比较对象
class QueueCompare:
    def __init__(self, priority, point_name):
        # print(type(priority))
        self.priority = priority
        self.point_name = point_name

    def __lt__(self, other):
        return self.priority < other.priority


def search(began: str, end: str, point_map: dict, road_id_map: dict):
    new_distance_from_began = PQ()
    # 队列中放置的数据类型是QueueCompare(distance, cur_point_name)
    new_distance_from_began.put(QueueCompare(0, began))
    global path_map
    visit_point = set()
    while not new_distance_from_began.empty():  # 若优先队列不为空就继续
        # 获取pq的第一个元素，为最优
        task = new_distance_from_began.get()
        point_name = task.point_name
        # 若找到了，直接返回终点所在的点
        if point_name == end:
            return task.point_name
        # 记录这个点已经遍历过了
        visit_point.add(point_name)
        dis = task.priority
        print_road_list = pointIdUtil.get_point_list(point_name, point_map)
        for road in print_road_list:
            # print(road+" road")
            # print(roadIdUtil.get_road(road, road_id_map))
            road_state = roadIdUtil.get_road_state(road, road_id_map)
            neighbor_point = roadIdUtil.get_road_end(road, road_id_map)
            road_dis = roadIdUtil.get_road_dis(road, road_id_map)
            # 这个if-else是用来判断单向和双向路的，要是单向路逆行，就不再加入队列
            # 把当前节点的邻接节点加入队列
            # print(type(road_dis + dis))
            # print(road_dis + dis)
            # print(type(road_dis))
            # print(type(dis))
            if road_state == "01":
                # 放进去的值是路的距离QueueCompare(dis,[cur_point,parent_point])的对象
                if neighbor_point not in visit_point:
                    new_distance_from_began.put(QueueCompare(road_dis + dis, neighbor_point))
                    path_map[neighbor_point] = [point_name, road]
            elif road_state == "02":
                if point_name == roadIdUtil.get_road_began(road, road_id_map):
                    if neighbor_point not in visit_point:
                        new_distance_from_began.put(QueueCompare(road_dis + dis, neighbor_point))
                        path_map[neighbor_point] = [point_name, road]
                # print({neighbor_point: [point_name, road]})
    return end


def get_path(began: str, point_cur: str):
    global path_point
    global path_road
    # print(point_cur)
    while point_cur != began:
        path_info = path_map.get(point_cur)
        point_cur = path_info[0]
        path_road.append(path_info[1])
    return path_road[::-1]  # 返回翻转之后的数组


def print_road(path: list, road_id_map: dict):
    all_point = []
    for road in path:
        road_point = roadIdUtil.get_road_info(road, road_id_map)
        # print(road_point)
        # print(type(road_point))
        # all_point = all_point.extend(road_point)
        for point in road_point:
            # print(point)
            all_point.append(point)
        # for point in road_point:
        # print(all_point)
        #     all_point.append(point)
    return all_point


def use_it(began: str, end: str, point_map: dict, road_id_map: dict):
    found = search(began, end, point_map, road_id_map)
    # print(path_map)
    path = get_path(began, found)
    # print(path)
    road = print_road(path, road_id_map)
    print("began( %s ) to end ( %s )" % (began, end))
    print("road id is: %s" % path)
    print("road point is : %s" % str(road))
