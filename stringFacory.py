def analysis_city(s: str):
    base_string = s.split(";")
    city_id = base_string[0].split()
    city_state = base_string[1]
    city_where = base_string[2]
    city_where = city_where.replace("\t", '').replace("、", ' ').split()
    return [city_id, city_state, city_where]


def analysis_topo_road(s: str):
    all_element = [s.replace("|", " ").split()]
    list0 = all_element[0][0]
    list0 = list0.split(",")
    # print(all_element)
    # 获取路段id
    road_id = list0[0]
    road_began = list0[1]+","+list0[2]
    road_end = list0[3]+","+list0[4]
    # 路段起始处连接的其他路径id
    list1 = all_element[0][1]
    began_conn_id = list1[list1.rfind(':') + 1:].split(",")
    # 路段终点处连接的其他路径id
    list2 = all_element[0][2]
    end_conn_id = list2[list2.rfind(':') + 1:].split(",")
    return [road_id, road_began, began_conn_id, road_end, end_conn_id]


def analysis_point(l: list):
    point1 = l[1]
    # 处理空路段
    if l[2][0]:
        ele1 = l[2] + [l[0]]
    else:
        ele1 = [l[0]]
    point2 = l[3]
    if l[4][0]:
        ele2 = l[4] + [l[0]]
    else:
        ele2 = [l[0]]
    return [point1, ele1, point2, ele2]


def str_to_coordinate(s: str):
    split = s.split(",")
    return [split[0], split[1]]
