# By Timothy Edmonds
# Apollolian Gasket Creator
# 8/06/2026

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_fractal_fig(circle_type, letter, num_generations, seed=None):
    rng = np.random.default_rng(seed)
    
    if circle_type == "Letter":
        if letter == "L":
            init_circles = 6
            num_first_gen_circles = 8
        elif letter == "O":
            init_circles = 8
            num_first_gen_circles = 12
        elif letter == "U":
            init_circles = 5
            num_first_gen_circles = 6
        num_circles = int(init_circles + num_first_gen_circles*(1-3**(num_generations-1))/(1-3))
        # total number of circles = inital number + number in first generation
        # (note that the initial number is the 0th generation in this)
        # + number in first generation * 3 (this is the second gen)
        # + number in first generation * 3^2 (this is the third gen)
        # + number in first generation * 3^3 (this is the fourth gen)
        # etc.
        # this formula can be written using the sum of a geometric series to be
        # total number = init_num + 3*(1-3^(num_gen)/(1-3)
        circle_parents = np.zeros([num_circles,3],dtype=np.int32)
        curv_array = np.zeros(num_circles)
        x_pos_array = np.zeros(num_circles)
        y_pos_array = np.zeros(num_circles)
        
        
        if letter == "L":
            # This is for the Letter "L"
            curv_array[0] = -1
            curv_array[1:4] = [1 + math.sqrt(2)] * 3
            x_pos_array[0] = 0.0
            y_pos_array[0] = 0.0
            x_pos_array[[1,2]] = 1/(1+math.sqrt(2))
            x_pos_array[[3]] = -1/(1+math.sqrt(2))
            y_pos_array[[1,3]] = 1/(1+math.sqrt(2))
            y_pos_array[[2]] = -1/(1+math.sqrt(2))
            
            # For the letter L, adding another circle for symmetry 
            curv_array[4] = 1 + math.sqrt(2)
            x_pos_array[4] = -1/(1+math.sqrt(2))
            y_pos_array[4] = -1/(1+math.sqrt(2))
            curv_array[5] = 3 + 2*math.sqrt(2)
            x_pos_array[5] = 0.0
            y_pos_array[5] = 0.0
            
            circle_parents[6,:] = [0,1,2]
            circle_parents[7,:] = [0,1,3]
            circle_parents[8,:] = [0,2,4]
            circle_parents[9,:] = [0,3,4]
            circle_parents[10,:] = [1,2,5]
            circle_parents[11,:] = [1,3,5]
            circle_parents[12,:] = [2,4,5]
            circle_parents[13,:] = [3,4,5]
        
        elif letter == "O":
            # This is for the Letter "O"
            curv_array[0] = -1
            curv_array[1:4] = 3
            x_pos_array[[0,1]] = 0.0
            y_pos_array[[0,1]] = 0.0
            x_pos_array[2] = 2/3
            y_pos_array[2] = 0.0
            x_pos_array[3] = 1/3
            y_pos_array[3] = 1/math.sqrt(3)
            
            # For the letter O adding another
            # 4 circles around the centre circle for symmetry
            curv_array[4:8] = 3
            x_pos_array[4] = -1/3
            y_pos_array[4] = 1/math.sqrt(3)
            x_pos_array[5] = -2/3
            y_pos_array[5] = 0
            x_pos_array[6] = -1/3
            y_pos_array[6] = -1/math.sqrt(3)
            x_pos_array[7] = 1/3
            y_pos_array[7] = -1/math.sqrt(3)
            circle_parents[8,:] = [0,2,3]
            circle_parents[9,:] = [0,2,7]
            circle_parents[10,:] = [0,3,4]
            circle_parents[11,:] = [0,4,5]
            circle_parents[12,:] = [0,5,6]
            circle_parents[13,:] = [0,6,7]
            circle_parents[14,:] = [1,2,3]
            circle_parents[15,:] = [1,2,7]
            circle_parents[16,:] = [1,3,4]
            circle_parents[17,:] = [1,4,5]
            circle_parents[18,:] = [1,5,6]
            circle_parents[19,:] = [1,6,7]
        
        elif letter == "U":
            # This is for the Letter "U"
            curv_array[0] = -1
            curv_array[1] = 3/2
            curv_array[2] = 3
            curv_array[3] = 7/2
            x_pos_array[0:2] = 0
            y_pos_array[0] = 0
            y_pos_array[1] = 1/3
            y_pos_array[2] = -2/3
            x_pos_array[3] = 4/7
            y_pos_array[3] = -3/7
            
            # For the letter U adding another circle for symmetry
            curv_array[4] = 7/2
            x_pos_array[4] = -4/7
            y_pos_array[4] = -3/7
            circle_parents[5,:] = [0,1,3]
            circle_parents[6,:] = [0,1,4]
            circle_parents[7,:] = [0,2,3]
            circle_parents[8,:] = [0,2,4]
            circle_parents[9,:] = [1,2,3]
            circle_parents[10,:] = [1,2,4]
        
        bends_times_centers_array = np.multiply(curv_array, x_pos_array + 1j*y_pos_array)
        
    else:
        init_circles = 4
        num_first_gen_circles = 4
        num_circles = int(init_circles + num_first_gen_circles*(1-3**(num_generations-1))/(1-3))
        circle_parents = np.zeros([num_circles,3],dtype=np.int32)
        curv_array = np.zeros(num_circles)
        x_pos_array = np.zeros(num_circles)
        y_pos_array = np.zeros(num_circles)

        z_init_pos_array = np.zeros(4) + 1j*np.zeros(4)
        
        curv_array[1] = 1/np.sqrt(rng.random())
        curv_array[2] = 1/np.sqrt(rng.random())
        curv_array[3] = 1/np.sqrt(rng.random())
        
        curv_array[0] = curv_array[1] + curv_array[2] + curv_array[3] - 2*np.sqrt(curv_array[1]*curv_array[2] + curv_array[2]*curv_array[3] + curv_array[1]*curv_array[3])
        curv_array[0:4] /= np.sign(curv_array[0])*curv_array[0]
        r_array = 1/curv_array[0:4]
        alpha = np.arccos(((r_array[1]+r_array[2])**2 + (r_array[1]+r_array[3])**2 - (r_array[2] + r_array[3])**2)/(2*(r_array[1]+r_array[2])*(r_array[1]+r_array[3])))
        z_init_pos_array[1] = 0 + 1j*0
        z_init_pos_array[2] = z_init_pos_array[1] + r_array[1] + r_array[2]
        z_init_pos_array[3] = z_init_pos_array[1] + np.exp(1j*alpha)*(r_array[1] + r_array[3])
        
        z_init_pos_array[0] = circle_overlap_test([curv_array[1],curv_array[2],curv_array[3]], np.multiply(curv_array[1:4],z_init_pos_array[1:4]), curv_array[0])
        
        #z_init_pos_array[0] = z_init_pos_array[2]*curv_array[2] + z_init_pos_array[3]*curv_array[3] - 2*np.sqrt(z_init_pos_array[2]*curv_array[2]*z_init_pos_array[3]*curv_array[3])
        z_init_pos_array[0] /= curv_array[0]
        z_init_pos_array -= z_init_pos_array[0]
        
        z_init_pos_array *= np.exp(1j*rng.random()*2*np.pi)
        
        for ii in range(0,init_circles):
            x_pos_array[ii] = z_init_pos_array[ii].real
            y_pos_array[ii] = z_init_pos_array[ii].imag
        
        # plt.figure(1)
        # for ii in range(0,4):
        #     r_ii = 1/curv_array[ii]
        #     x_ii = x_pos_array[ii]
        #     y_ii = y_pos_array[ii]
        #     theta_range = np.linspace(0,2*math.pi,max(200 - math.floor(1/r_ii),100))
        #     plt.text(x_ii+0.02*rng.random(), y_ii+0.02*rng.random(), str(ii), fontsize=12, color="black", ha='left', va='bottom')
        #     #plt.text(x_ii*curv_array[ii], y_ii*curv_array[ii], str(ii), fontsize=12, color="black", ha='left', va='bottom')
        #     x_range = x_ii + r_ii*np.cos(theta_range)
        #     y_range = y_ii + r_ii*np.sin(theta_range)
        #     if abs(r_ii) > 0.0025:
        #         plt.plot(x_range,y_range,'k','linewidth', 0.01)
        #         #plt.plot(x_range*curv_array[ii],y_range*curv_array[ii],'k','linewidth', 0.01)
        #     else:
        #         pass
        # plt.xlim(-1.1,1.1)
        # plt.ylim(-1.1,1.1)
        # plt.axis('equal')
        # plt.axis('off')
        # plt.title('Initial circles')
        
        bends_times_centers_array = np.multiply(curv_array, x_pos_array + 1j*y_pos_array)
        
        none_flipped = False
        while not(none_flipped):
            none_flipped = True
            for ii in [0,1,2,3]:
                values_array = np.setdiff1d(np.array([0,1,2,3]), ii)
                c_0 = curv_array[values_array[0]]
                c_1 = curv_array[values_array[1]]
                c_2 = curv_array[values_array[2]]
                c_ii_flip = 2*(c_0 + c_1 + c_2) - curv_array[ii]
                #print('beep')
                #print(ii)
                #print(c_ii_flip)
                #print(curv_array[ii])
                if c_ii_flip < curv_array[ii]:
                    none_flipped = False
                    #print('flipped')
                    curv_array[ii] = c_ii_flip
                    z_0 = z_init_pos_array[values_array[0]]
                    z_1 = z_init_pos_array[values_array[1]]
                    z_2 = z_init_pos_array[values_array[2]]
                    bends_times_centers_array[ii] = 2*(z_0*c_0 + z_1*c_1 + z_2*c_2) - bends_times_centers_array[ii]
                    z_init_pos_array[ii] = bends_times_centers_array[ii] / curv_array[ii]
            
        for ii in range(0,init_circles):
            x_pos_array[ii] = z_init_pos_array[ii].real
            y_pos_array[ii] = z_init_pos_array[ii].imag
        
        circle_parents[4,:] = [0,1,2]
        circle_parents[5,:] = [0,1,3]
        circle_parents[6,:] = [0,2,3]
        circle_parents[7,:] = [1,2,3]
        
        # plt.figure(2)
        # for ii in range(0,4):
        #     r_ii = 1/curv_array[ii]
        #     x_ii = x_pos_array[ii]
        #     y_ii = y_pos_array[ii]
        #     theta_range = np.linspace(0,2*math.pi,max(200 - math.floor(1/r_ii),100))
        #     plt.text(x_ii+0.02*rng.random(), y_ii+0.02*rng.random(), str(ii), fontsize=12, color="black", ha='left', va='bottom')
        #     #plt.text(x_ii*curv_array[ii], y_ii*curv_array[ii], str(ii), fontsize=12, color="black", ha='left', va='bottom')
        #     x_range = x_ii + r_ii*np.cos(theta_range)
        #     y_range = y_ii + r_ii*np.sin(theta_range)
        #     if abs(r_ii) > 0.0025:
        #         plt.plot(x_range,y_range,'k','linewidth', 0.01)
        #         #plt.plot(x_range*curv_array[ii],y_range*curv_array[ii],'k','linewidth', 0.01)
        #     else:
        #         pass
        # plt.xlim(-1.1,1.1)
        # plt.ylim(-1.1,1.1)
        # plt.axis('equal')
        # plt.axis('off')
        # plt.title('After flipping')
        
    # Let's calculate the curvatures for the first generation of children
        
    for ii in range(init_circles, init_circles+num_first_gen_circles):
        curv_0 = curv_array[circle_parents[ii,0]]
        curv_1 = curv_array[circle_parents[ii,1]]
        curv_2 = curv_array[circle_parents[ii,2]]
        btc_0 = bends_times_centers_array[circle_parents[ii,0]]
        btc_1 = bends_times_centers_array[circle_parents[ii,1]]
        btc_2 = bends_times_centers_array[circle_parents[ii,2]]
        z_0 = x_pos_array[circle_parents[ii,0]] + 1j*y_pos_array[circle_parents[ii,0]]
        z_1 = x_pos_array[circle_parents[ii,1]] + 1j*y_pos_array[circle_parents[ii,1]]
        z_2 = x_pos_array[circle_parents[ii,2]] + 1j*y_pos_array[circle_parents[ii,2]]
        curv_array[ii] = curv_0 + curv_1 + curv_2 + 2*np.sqrt(curv_0*(curv_1 + curv_2) + curv_1*curv_2)
        #bends_times_centers_array[ii] = z_0*curv_0 + z_1*curv_1 + z_2*curv_2 + 2*np.sqrt(curv_0*curv_1*z_0*z_1 + curv_0*curv_2*z_0*z_2 + curv_1*curv_2*z_1*z_2)
        bends_times_centers_array[ii] = circle_overlap_test([curv_0,curv_1,curv_2], [btc_0,btc_1,btc_2], curv_array[ii])
        z_pos = bends_times_centers_array[ii] / curv_array[ii]
        x_pos_array[ii] = z_pos.real
        y_pos_array[ii] = z_pos.imag
        

    # Now we initialise the second generation of circles (children created from the
    # children initialised above)

    for ii in range(2,num_generations):
        beginning_pos_parents = int(init_circles + num_first_gen_circles*(1-3**(ii-2))/(1-3))
        ending_pos_parents = int(init_circles + num_first_gen_circles*(1-3**(ii-1))/(1-3) - 1)
        beginning_pos_children = int(init_circles + num_first_gen_circles*(1-3**(ii-1))/(1-3))
        for jj in range(0, ending_pos_parents-beginning_pos_parents+1):
            for kk in range(0,3):
                new_triplet = [int(ll) for ll in circle_parents[beginning_pos_parents+jj,:]]
                new_triplet[kk] = beginning_pos_parents + jj
                child_pos = beginning_pos_children + jj*3 + kk
                circle_parents[child_pos] = [qq for qq in new_triplet]
                curv_0 = curv_array[new_triplet[0]]
                curv_1 = curv_array[new_triplet[1]]
                curv_2 = curv_array[new_triplet[2]]
                btc_0 = bends_times_centers_array[new_triplet[0]]
                btc_1 = bends_times_centers_array[new_triplet[1]]
                btc_2 = bends_times_centers_array[new_triplet[2]]
                curv_array[child_pos] = curv_0 + curv_1 + curv_2 + 2*np.sqrt(curv_0*(curv_1 + curv_2) + curv_1*curv_2)
                bends_times_centers_array[child_pos] = circle_overlap_test([curv_0,curv_1,curv_2], [btc_0,btc_1,btc_2], curv_array[child_pos])
                z_pos = bends_times_centers_array[child_pos] / curv_array[child_pos]
                x_pos_array[child_pos] = z_pos.real
                y_pos_array[child_pos] = z_pos.imag
                
    if circle_type == "Letter":
        if circle_type == "L":
            filled_circles = [2,3,4]
        elif circle_type == "O":        
            filled_circles = [2,3,4,5,6,7]
        else: # circle_type == "U"
            filled_circles = [2,3,4,5,6,13,16,46,37,109,136]
    else:
        filled_circles = []
        
    fig, ax = plt.subplots()

    for ii in range(0,num_circles):
        r_ii = 1/curv_array[ii]
        x_ii = x_pos_array[ii]
        y_ii = y_pos_array[ii]
        theta_range = np.linspace(0,2*math.pi,max(200 - math.floor(1/r_ii),25))
        #plt.text(x_ii+0.02*rng.random(), y_ii+0.02*rng.random(), str(ii), fontsize=12, color="black", ha='left', va='bottom')
        #plt.text(x_ii*curv_array[ii], y_ii*curv_array[ii], str(ii), fontsize=12, color="black", ha='left', va='bottom')
        x_range = x_ii + r_ii*np.cos(theta_range)
        y_range = y_ii + r_ii*np.sin(theta_range)
        if ii in filled_circles:
            circle = patches.Circle((x_ii, y_ii), r_ii, color=[0.2,0.2,0.2], linewidth=0.001)
            plt.plot(x_range,y_range,'k','linewidth', 0.01)
            ax.add_patch(circle)
        else:
            if abs(r_ii) > 0.005:
                plt.plot(x_range,y_range,'k','linewidth', 0.01)
                #plt.plot(x_range*curv_array[ii],y_range*curv_array[ii],'k','linewidth', 0.01)
            else:
                pass
        
    return fig, ax

def circle_overlap_test(c_vec, btc_vec, c):
    b_0 = btc_vec[0]
    b_1 = btc_vec[1]
    b_2 = btc_vec[2]
    delta = b_0*(b_1 + b_2) + b_1*b_2
    b_3_pos = 2*np.sqrt(delta) + b_0 + b_1 + b_2
    b_3_neg = -2*np.sqrt(delta) + b_0 + b_1 + b_2
    pos_overstepping = 0
    neg_overstepping = 0
    for ii in range(0,3):
        if c_vec[ii] > 0:
            z_pos = b_3_pos/c
            z_neg = b_3_neg/c
            z_ii = btc_vec[ii] / c_vec[ii]
            pos_overstepping += np.abs(np.abs(z_pos - z_ii) - (1/c + 1/c_vec[ii]))
            neg_overstepping += np.abs(np.abs(z_neg - z_ii) - (1/c + 1/c_vec[ii]))
    if pos_overstepping > neg_overstepping:
        b_3 = b_3_neg
    else:
        b_3 = b_3_pos
    
    return b_3

###########################

my_circle_type = "NA" # change  this variable to make different circles
my_letter = "NA"
num_generations = 12
my_seed = None

myfig, myax = generate_fractal_fig(my_circle_type, my_letter, num_generations, my_seed)

myfig.tight_layout()
myfig.set_size_inches(18, 12)
myax.set_xlim(-1.65,1.65)
myax.set_ylim(-1.1,1.1)
myax.set_aspect('equal')
myax.set_axis_off()

myfig.savefig(my_circle_type + "_fig.png", bbox_inches='tight', dpi=500)