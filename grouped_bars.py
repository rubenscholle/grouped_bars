from matplotlib import pyplot as plt

# =============================================================================
# Begin of Code for the Figures

def plot_bar(for_con1, for_con2, for_con3,
             bac_con1, bac_con2, bac_con3,
             for_err_con1, for_err_con2, for_err_con3,
             bac_err_con1, bac_err_con2, bac_err_con3):
    n_bars = len(for_con1)
    n_sets = 3
    width = 0.8
    x_range = range(n_bars)
    
    n_set = 1
    x_values_bar1 = [x*n_sets + width*n_set for x in x_range]
    n_set = 2
    x_values_bar2 = [x*n_sets + width*n_set for x in x_range]
    n_set = 3
    x_values_bar3 = [x*n_sets + width*n_set for x in x_range]
    
    plt.figure(dpi=300)
    
    ax1 = plt.subplot(2, 1, 1)
    plt.bar(x_values_bar1, for_con1,
            yerr=[err/2 for err in for_err_con1],
            width=width, color=(0.0, 0.45, 0.7))
    plt.bar(x_values_bar2, for_con2,
            yerr=[err/2 for err in for_err_con2],
            width=width, color=(0.9, 0.6, 0.0))
    plt.bar(x_values_bar3, for_con3,
            yerr=[err/2 for err in for_err_con3],
            width=width, color=(0.0, 0.6, 0.5))
    plt.legend(["PRED", "RAND", "ARBI"], loc=6, bbox_to_anchor=(1.0, 0.5))
    
    ax1.set_title("Forward connections")
    ax1.set_xticks(x_values_bar2)
    ax1.set_xticklabels(["V1 to V5", "V5 to PPC", "V5 to FEF"])
    ax1.set_yticks([0.0, 1.0])
    ax1.set_ylabel("Rate of change [Hz]", labelpad=9)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    
    ax2 = plt.subplot(2, 1, 2)
    plt.bar(x_values_bar1, bac_con1, yerr=[err/2 for err in bac_err_con1],
            width=width, color=(0.0, 0.45, 0.7))
    plt.bar(x_values_bar2, bac_con2, yerr=[err/2 for err in bac_err_con2],
            width=width, color=(0.9, 0.6, 0.0))
    plt.bar(x_values_bar3, bac_con3, yerr=[err/2 for err in bac_err_con3],
            width=width, color=(0.0, 0.6, 0.5))
    plt.legend(["PRED", "RAND", "ARBI"], loc=6, bbox_to_anchor=(1.0, 0.5))
    
    ax2.set_title("Backward connections")
    ax2.set_xticks(x_values_bar2)
    ax2.set_xticklabels(["V5 to V1", "PPC to V5", "FEF to V5"])
    ax2.set_yticks([-1.0, 0.0, 1.0])
    ax2.set_ylabel("Rate of change [Hz]", labelpad=1)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    
    plt.subplots_adjust(hspace=0.75)
    plt.show()

# =============================================================================
# Values for healthy controls (POOL2)
for_con1 = [0.462611044382322, -0.0211679643100743, 0.0456064492956654]
for_con2 = [0.724209642541496, -0.00635609213418158, 0.0786755766677362]
for_con3 = [0.832748046264946, 0.0164991447823063, 0.132841050942860]
 
bac_con1 = [-0.852949171436513, 0.324399096354887, -0.169963989483023]
bac_con2 = [-0.892966249463560, -0.0369482344125263, -0.191977102332139]
bac_con3 = [-0.793548720662410, 0.0511087624340343, -0.357279206019969]
 
for_err_con1 = [0.504733102217789, 0.247847729622880, 0.224386532145722]
for_err_con2 = [0.501835640406907, 0.230568100819341, 0.234988526817661]
for_err_con3 = [0.677684495090921, 0.218263799941919, 0.215960820324218]
 
bac_err_con1 = [0.982570179764665, 0.903199004387901, 0.787099815077565]
bac_err_con2 = [0.952867903249435, 0.733087882591047, 0.885656154430710]
bac_err_con3 = [0.864343397292572, 0.838504583055098, 0.727783819285207]
 
print("Plotting values for healthy controls (POOL2)")
plot_bar(for_con1, for_con2, for_con3,
             bac_con1, bac_con2, bac_con3,
             for_err_con1, for_err_con2, for_err_con3,
             bac_err_con1, bac_err_con2, bac_err_con3)
# =============================================================================

# =============================================================================
# Values for patients (POOL2)
for_con1 = [0.618460829328757, 0.0845034602686620, 0.0757894011657502]
for_con2 = [0.817094062326293, 0.109697511826589, 0.0978061707147773]
for_con3 = [0.878239716076582, 0.0917928750713414, 0.0984316608376399]

bac_con1 = [-0.758743536594845, -0.231702993473162, -0.109992090394867]
bac_con2 = [-0.714516384740644, -0.367440809526225, 0.0318306977801803]
bac_con3 = [-0.812342626099541, -0.490545406924227, -0.125563036471298]

for_err_con1 = [0.930191127856646, 0.361255948575289, 0.344494040821136]
for_err_con2 = [1.24693000533589, 0.289069592318661, 0.311988392048325]
for_err_con3 = [1.09164825116615, 0.236910359789663, 0.252633588422554]

bac_err_con1 = [1.18816747570060, 1.44424124112124, 0.773100768193135]
bac_err_con2 = [1.13979426806352, 1.27309865627586, 0.532624886675957]
bac_err_con3 = [1.08994772063479, 1.02298194748518, 0.912595418409581]

print("Plotting values for patients (POOL2)")
plot_bar(for_con1, for_con2, for_con3,
             bac_con1, bac_con2, bac_con3,
             for_err_con1, for_err_con2, for_err_con3,
             bac_err_con1, bac_err_con2, bac_err_con3)
# =============================================================================
 
# Values for healthy controls (POOL1)
for_con1 = [0.416535952886009, 0.498769488030948, 0.396837509406708]
for_con2 = [0.702360126248481, 0.526869817768569, 0.412988824552684]
for_con3 = [0.850014111600964, 0.523993175074803, 0.437276233150160]

bac_con1 = [-1.32881676119526, 0.258023155549792, -0.0829519545689855]
bac_con2 = [-1.05499573020505, -0.215626041594924, -0.229110978900047]
bac_con3 = [-0.893483573311752, -0.165107327882384, -0.0891506266605288]

for_err_con1 = [0.417830565567551, 0.477506976747285, 0.252810644115165]
for_err_con2 = [0.518461410224177, 0.379571670938628, 0.245260252432994]
for_err_con3 = [0.628322814275160, 0.320930511960236, 0.249401739396062]
 
bac_err_con1 = [1.35386635929210, 0.737002935283998, 0.648012349955031]
bac_err_con2 = [1.29937268424005, 0.677143104888199, 0.675295682207789]
bac_err_con3 = [1.10538348781958, 0.589930329281642, 0.677387188601557]

print("Plotting values for healthy controls (POOL1)")
plot_bar(for_con1, for_con2, for_con3,
             bac_con1, bac_con2, bac_con3,
             for_err_con1, for_err_con2, for_err_con3,
             bac_err_con1, bac_err_con2, bac_err_con3)