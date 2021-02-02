def get_road(road_id: str, road_id_map: dict):
    get_info = road_id_map.get(road_id)
    return get_info


def get_road_dis(road_id: str, road_id_map: dict):
    get_info = road_id_map.get(road_id)
    return get_info[0]


def get_road_state(road_id: str, road_id_map: dict):
    get_info = road_id_map.get(road_id)
    return get_info[1]


def get_road_began(road_id: str, road_id_map: dict):
    get_info = road_id_map.get(road_id)
    return get_info[2]


def get_road_end(road_id: str, road_id_map: dict):
    get_info = road_id_map.get(road_id)
    return get_info[3]


def get_road_info(road_id: str, road_id_map: dict):
    get_info = road_id_map.get(road_id)
    return get_info[4]
