# devim akarer / term project / part-3
# electronic tacheometry computation

import math

print("Program for Electrometric Tacheometry Computation")
print("-------------------------------------------------------")

# input part

sta_t_ID = input("Enter the stationary traverse ID                 : ")
ref_t_ID = input("Enter the referenced traverse ID                 : ")
y_coord_1 = float(input("Enter the Y coordinates of {} (m)              : " .format(ref_t_ID)))
x_coord_1 = float(input("Enter the X coordinates of {} (m)              : " .format(ref_t_ID)))
height_1 = float(input("Enter the height of {}        (m)              : " .format(ref_t_ID)))
y_coord_2 = float(input("Enter the Y coordinates of {} (m)              : " .format(sta_t_ID)))
x_coord_2 = float(input("Enter the X coordinates of {} (m)              : " .format(sta_t_ID)))
height_2 = float(input("Enter the height of {}        (m)              : " .format(sta_t_ID)))
det_point = input("Enter the point ID of detail point               : ")
horizon = float(input("Enter the horizontal direction of point {} (grad) : " .format(det_point)))
ver_angle = float(input("Enter the verticle angle of point {} (grad)       : " .format(det_point)))
slope = float(input("Enter the slope distance between {} and {} (m)  : ".format(sta_t_ID, det_point)))
height_inst = float(input("Enter the height of instrument (m)               : "))
height_refl = float(input("Enter the height of reflector  (m)               : "))

# calculations

h_distance = slope * math.sin(ver_angle * math.pi / 200)
delta_H = h_distance * math.cos(ver_angle * math.pi / 200) - (height_inst - height_refl)
elevation = height_2 + delta_H
delta_y = (y_coord_2 - y_coord_1)
delta_x = (x_coord_2 - x_coord_1)
# this part to avoid ZeroDivisionError:
azimuth = 0
if delta_x != 0 and delta_y != 0:
    azimuth = (math.atan(abs(delta_y) / abs(delta_x))) * (200 / math.pi)
elif delta_x == 0:
    if delta_y > 0:
        azimuth = 100
    elif delta_y < 0:
        azimuth = 300
elif delta_y == 0:
    if delta_x > 0:
        azimuth = 0
    elif delta_x < 0:
        azimuth = 200

dev = azimuth + horizon
# conditions of next azimuth angle:
if dev < 200:
    dev = dev + 200
elif 200 < dev < 600:
    dev = dev - 200
elif dev > 600:
    dev = dev - 600
# calculations of coordinates x and y:
coordinate_x = x_coord_2 + h_distance * (math.cos(dev * math.pi / 200))
coordinate_y = y_coord_2 + h_distance * (math.sin(dev * math.pi / 200))

# output

print("\n")
print(format("Point ID", "<15"), format("Point ID", "<15"), format("Hor. Dist.", "<15"), format("Delta H", "<15"),
      format("Elevation", "<15"), format("Coord.(Y)", "<15s"), format("Coord.(X)", "<15s"))
print("----------------------------------------------------------------------------------------------------------------------------------")
print(format(sta_t_ID, "<15"), format(det_point, "<15"), format(format(h_distance, ".3f"), "<15"),
      format(format(delta_H, ".3f"), "<15"), format(format(elevation, ".3f"), "<15"),
      format(format(coordinate_y, ".3f"), "<15"), format(coordinate_x, ".3f"))
print("----------------------------------------------------------------------------------------------------------------------------------")
