import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

# Load neutral images (replace these file paths with your actual image files)
ukraine_war_image = mpimg.imread('ukraine_war_2021.png')
#covid_image = mpimg.imread('path/to/covid_image.jpg')

# Sample data (replace this with your actual data)
years = [2018, 2019, 2020, 2021, 2022, 2023]
yearly_totals = [88.8, 58.4, 67.4, 64.1, 10.6, 37.1]
monthly_totals_2021 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
monthly_totals_2022 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
monthly_totals_2023 = [-56.5, -32.8, 13.2, 13.3, 47.7, 54.6, 16.0, 6.8, 0.7, 14.2, -10.0, -30.0]
costs_1 = [-10.0, -5.0, -7.0, -4.0, -2.0, -8.0]
costs_2 = [-5.0, -3.0, -4.0, -6.0, -1.0, -4.5]

# Repeat the years for each month
months = list(range(1, 13))
years_repeated_2021 = [years[-3]] * 12
years_repeated_2022 = [years[-2]] * 12
years_repeated_2023 = [years[-1]] * 12

# Plotting the data
fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(10, 8))
# Set facecolor to 'none' and remove the edge color
fig.patch.set_facecolor('white')
fig.patch.set_edgecolor('white')

# Add a horizontal line at y=0
ax1.axhline(0, color='black', linestyle='-', linewidth=3)

# Plotting yearly totals
color = 'tab:blue'
ax1.set_xticks(years)
ax1.set_xticklabels(years, fontsize=16)
bars = ax1.bar(years, yearly_totals, color=color, alpha=0.7, label='Yearly Total', edgecolor='none', linewidth=0)
ax1.tick_params(axis='x', left=False, right=False, labelleft=False, labelright=False, length=0)
ax1.set_yticks([])

# Creating a secondary y-axis for monthly data
ax2 = ax1.twinx()
color = 'lightgrey'
ax2.tick_params(axis='y', left=False, right=False, labelleft=False, labelright=False)
ax2.set_yticks([])

# Adding yearly total labels
for year, total in zip(years, yearly_totals):
    rounded_total = round(total, 0)  # Round to zero digits
    ax1.text(year, rounded_total + 5, str(int(rounded_total)), ha='center', va='bottom', fontweight='bold', fontsize=16)

# Create a new subplot for the costs
ax3.bar(years, costs_1, color='tab:red', alpha=0.7, label='Cost 1', edgecolor='none', linewidth=0)
ax3.bar(years, costs_2, color='tab:orange', bottom=costs_1, alpha=0.7, label='Cost 2', edgecolor='none', linewidth=0)
ax3.axhline(0, color='black', linestyle='-', linewidth=3)  # Add a horizontal line at y=0
ax3.set_xticks(years)
ax3.set_xticklabels(years, fontsize=16)
ax3.set_xlabel('Year', fontweight='bold', fontsize=16)
ax3.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, borderaxespad=0.0, frameon=False)
ax3.set_title('Costs')

# Adding cost labels
for year, cost1, cost2 in zip(years, costs_1, costs_2):
    total_cost = cost1 + cost2
    ax3.text(year, total_cost - 5, str(int(total_cost)), ha='center', va='top', fontweight='bold', fontsize=16)

# Save the plot with both subplots as a PNG file
plt.suptitle('Yearly and Monthly Data with Costs', fontsize=18, y=1.02)
plt.savefig('cfgraph_combined.png', bbox_inches='tight', pad_inches=0)
plt.show()
