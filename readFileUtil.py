import stringFacory as sf
import redisFactory
import roadDistance as rd


def read_city_util(file_name: str):
    f = open(file=file_name, mode="r", encoding="utf-8")
    print("开始读取city.txt文件")
    res = {}
    for line in f:
        analysis_city = sf.analysis_city(line)
        dis = rd.road_distance(analysis_city[2])
        value_path = analysis_city[2]
        began_point = analysis_city[2][0]
        end_point = analysis_city[2][-1]
        value_state_dis = [dis, analysis_city[1], began_point, end_point, value_path]
        res[analysis_city[0][0]] = value_state_dis
    f.close()
    print("读取完成city.txt文件")
    return res


def read_topo_util(file_name: str):
    f = open(file=file_name, mode="r", encoding="utf-8")
    print("开始读取Topologe.txt文件")
    res = {}
    for line in f:
        analysis_city = sf.analysis_topo_road(line)
        point = sf.analysis_point(analysis_city)
        # print(point)
        res[point[0]] = point[1]
        res[point[2]] = point[3]
        # redis 只接受string等类型，不接受list，只能以后读下来再切割了
        # r.set(point[0], ",".join(point[1]))
        # r.set(point[2], ",".join(point[3]))
    f.close()
    # print(res)
    print("读取完成Topologe.txt文件")
    return res
