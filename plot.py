#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:59:26 2019

@author: rain
"""
######## plot box-plot  http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
## combine these different collections into a list  
sensitivity_to_plot = [cm_Cortex1_DroNc, cm_Cortex1_sci, cm_Cortex1_10x, cm_Cortex1_Smart_seq2]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)
# Create the boxplot
#bp = ax.boxplot(sensitivity_to_plot)


bp = ax.boxplot(sensitivity_to_plot, patch_artist=True)

## change outline color, fill color and linewidth of the boxes  
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

## Custom x-axis labels
ax.set_xticklabels(['DroNc-seq', 'sci-RNA-seq', '10x-Chromium-v2', 'Smart-seq2'])



################################## plot  https://blog.csdn.net/Site1997/article/details/79180384
# plot 画出随着cell个数增加时被读出gene个数的变化曲线
plot_list = [cm_Cortex1_DroNc, cm_Cortex1_sci, cm_Cortex1_10x, cm_Cortex1_Smart_seq2]
y = [plot(x) for x in plot_list]    
import matplotlib.pyplot as plt

#开始画图
plt.plot((range(1, len(y[0])+1)), y[0], color='yellow', label='DroNc-seq')
plt.plot((range(1, len(y[1])+1)), y[1], color='skyblue', label='sci-RNA-seq')
plt.plot((range(1, len(y[2])+1)), y[2],  color='#b2df8a', label='10x-Chromium-v2')
plt.plot((range(1, len(y[3])+1)), y[3], color='#e7298a', label='Smart-seq2')
plt.legend() # 显示图例
plt.title('relation between number of cells and number of genes detected')
plt.xlabel('the number of cells considered')
plt.ylabel('the number of genes detected')
plt.show()