# EPyT_C - EPyT_C - Developed by Abhijith & Avi 
# ---------------------------------------------
# Functions
import numpy as np
import math

class node_connectivity():
    def incoming_links(num1, arr1):
        # num1 - node number; arr1 - matrix of end node indices
        links_connecting_to_node = []
        if arr1.count(num1 + 1) > 0:
            arr = np.array(arr1)
            bool_arr = (arr == num1 + 1)
            links_connecting_to_node = np.where(bool_arr)[0]
        return links_connecting_to_node
    
    def outgoing_links(num1, arr1):
        # num1 - node number; arr1 - matrix of start node indices
        links_connecting_from_node = []
        if arr1.count(num1 + 1) > 0:
            arr = np.array(arr1)
            bool_arr = (arr == num1 + 1)
            links_connecting_from_node = np.where(bool_arr)[0]
        return links_connecting_from_node

class missing_info():
    # Minimum length to be specified for links (pumps and valves)
    def minimum_link_length(num1, num2, num3, arr1):
        # num1 - total time steps in the filtered hydraulic report; num2 - water quality time step; num3 - tolerable flow velocity considered; arr1 - velocity array
        min_vel = []
        for h in range(num1):
            min_val = np.min(arr1[h])
            min_vel.append(min_val)
        minimum_flow_velocity = np.min(min_vel)
        if minimum_flow_velocity < num3:
            minimum_flow_velocity = num3
        minimum_link_length = minimum_flow_velocity * num2
        return minimum_link_length
    
    # Minimum diameter to be specified for links (pumps and valves)
    def minimum_link_diameter(num1, num2, num3, arr1):
        # num1 - number of links; num2 - number of pumps; num3 - number of valves; arr1 - diameter array
        min_val = np.min(arr1)
        if min_val == 0:
            arr2 = arr1[0: num1 - (num2 + num3)]
            min_val = np.min(arr2)
            minimum_link_diameter = min_val
        else:
            minimum_link_diameter = min_val
        return minimum_link_diameter
    
class hydraulic_data_interpret():
    def sync_time(d, H, num1, num2, num3, num4, num5, num6, num7, num8, arr1, arr2):
        # num1 = wq_time; num2 = total_h_steps_expected
        # num3 = base_time_cycle_s; num4 = h_sim_time_step_s;
        # num5 = time_cycle_count; num6 = base_time_cycle_day; num7 = wq_sim_time_step_s
        # num8 = h_step_expected
        # arr1 = sync_option; arr2 = reservoir_pattern
        if arr1 == 'steady':
            if num1 == 0:
                h_step_expected = math.floor(num2 - (num3/ num4)) - 1
                h_step = h_step_expected
                reservoir_pattern_step = injection_pattern_step = 0
            else:
                h_step_expected = num8
                wq_time_cycle = num1 - (num5 - 1) * num6 * 24 * 3600
                wq_time_hydraulic_report = wq_time_cycle + (int(d.getTimeSimulationDuration()) - num3)
                for x in range(num8, num2):
                    if wq_time_hydraulic_report <= H.Time[x]:
                        h_step = math.floor(x)
                        break
                reservoir_pattern_step = injection_pattern_step = len(arr2[0]) - (num2 - h_step) + 1
        elif arr1 == 'dynamic':
            if num1 == 0:
                h_step_expected = 0; h_step = h_step_expected
                reservoir_pattern_step = injection_pattern_step = 0
            else:
                h_step_expected = num8
                wq_time_cycle = num1
                wq_time_hydraulic_report = wq_time_cycle
                for x in range(num8, num2):
                    if wq_time_hydraulic_report <= H.Time[x]:
                        h_step = math.floor(x)
                        break
                reservoir_pattern_step = injection_pattern_step = h_step - int((num5 - 1) * (num6 * 24 * 3600/ num7))
        out = [h_step, h_step_expected, reservoir_pattern_step, injection_pattern_step]
        return out
        
    
    def time_filter(H, num1, num2, num3):
        filtered_steps = []
        if num1 > 1:
            print("Filtering hydraulic analysis report.")
            for s in range(num2):
                if H.Time[s] % num3 != 0:
                    filtered_steps.append(s)
        return filtered_steps
    
    def time_data(arr1, arr2):
        arr2 = np.array(arr2)
        if len(arr2) > 0:
            out = np.delete(arr1, arr2, 0)
        else:
            out = arr1
        return out
    
    def velocity_data(arr1, arr2, str1):
        arr2 = np.array(arr2)
        if len(arr2) > 0:
            out = np.delete(arr1, arr2, 0)
        else:
            out = arr1
        if str1 == 'GPM':
            out = np.multiply(out, 0.3048)
        return out
    
    def demand_data(arr1, arr2, str1):
        arr2 = np.array(arr2)
        if len(arr2) > 0:
            out = np.delete(arr1, arr2, 0)
        else:
            out = arr1
        if str1 == 'GPM':
            out = np.multiply(out, 6.3e-5)
        elif str1 == 'LPS':
            out = np.multiply(out, 1e-3)
        elif str1 == 'LPM':
            out = np.multiply(out, 1.67e-5)
        elif str1 == 'CMH':
            out = np.multiply(out, (1/3600))
        return out
    
    def flow_data(arr1, arr2, str1):
        arr2 = np.array(arr2)
        if len(arr2) > 0:
            out = np.delete(arr1, arr2, 0)
        else:
            out = arr1
        if str1 == 'GPM':
            out = np.multiply(out, 6.3e-5)
        elif str1 == 'LPS':
            out = np.multiply(out, 1e-3)
        elif str1 == 'LPM':
            out = np.multiply(out, 1.67e-5)
        elif str1 == 'CMH':
            out = np.multiply(out, (1/3600))
        return out
    
    def tank_volume_data(arr1, arr2, str1):
        arr2 = np.array(arr2)
        if len(arr2) > 0:
            out = np.delete(arr1, arr2, 0)
        else:
            out = arr1
        if str1 == 'GPM':
            out = np.multiply(out, 0.0283)
        return out
    
    def maximum_segments(num1, num2, arr1, arr2):
        # num1 - tolerable minimum velocity (m/s); num2 - water quality time step (s)
        # arr1 - matrix of length links; arr2 - array of link flow velocity
        arr2[arr2 < num1] = 0
        arr2[arr2 == 0] = 100
        min_vel = np.min(arr2)
        index = np.where(arr2 == min_vel)
        len_min_vel_pipe = arr1[index[1][0]]
        max_segments = math.ceil(len_min_vel_pipe/ (num1 * num2)) + 1
        return max_segments
        
class display():
    def reservoir_names(num1, arr1, arr2):
        for x in range(num1):
            print("Reservoir %d: %s" % (x + 1, arr1[arr2[x] - 1]))
            
    def tank_names(num1, arr1, arr2):
        for x in range(num1):
            print("Tank %d: %s" % (x + 1, arr1[arr2[x] - 1]))
    
    def pump_names(num1, num2, arr1):
        if num1 > 0:
            for x in range(num1):
                print("Pump %d: %s" % (x + 1, arr1[len(arr1) - num2 - (num1 - x)]))
                
    def valve_names(num1, arr1):
        if num1 > 0:
            for x in range(num1):
                print("Valve %d: %s" % (x + 1, arr1[len(arr1) - (num1 - x)]))
                
    def simulation_info(num1, num2, num3, num4):
        print("Number of iterations: %d" % (num1))
        print("Number of days for which water quality is simulated: %d" % (num2))
        print("Time period for water quality simulation: %d seconds" % (num3))
        print("Number of water quality simulation steps: %d" % (num4))
        
    def msrt_info(num1, num2, num3):
        print("Number of water quality parameters in the MSRT model: %d" % (num1))
        print("Number of bulk phase water quality paraneters: %d" % (num2))
        print("Number of wall phase water quality paraneters: %d" % (num3))
        
    def omitted_nodes(num1, arr1, arr2):
        if num1 > 0:
            print("Number of nodes omitted for analysis: %d" % (num1))
            for x in range(num1):
                print("Omitted Node %d: %s" % (x + 1, arr1[arr2[x]]))
                
    def omitted_links(num1, arr1, arr2):
        if num1 > 0:
            print("Number of links omitted for analysis: %d" % (num1))
            for x in range(num1):
                print("Omitted Link %d: %s" % (x + 1, arr1[arr2[x]]))
            