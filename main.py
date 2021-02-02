# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import redisFactory
import readFileUtil
import stringFacory
import UCS as ucs
import pointIdUtil
if __name__ == '__main__':
    roadId_map = readFileUtil.read_city_util("city.txt")
    pointId_map = readFileUtil.read_topo_util("Topology.txt")
    # r1 = "109.003387,34.446017","109.0,34.446114"
    # r2 = "109.003471,34.448046", "109.0,34.446114"
    ucs.use_it("109.003387,34.446017",  "109.0,34.446114", pointId_map, roadId_map)

