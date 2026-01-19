import matplotlib.pyplot as plt
import numpy as np
import os

def setup_style():
    """Sets the visual style for the plots."""
    try:
        plt.style.use('seaborn-v0_8-darkgrid')
    except:
        plt.style.use('ggplot')

def create_visualizations():
    """Generates a combined dashboard of COVID-19 vaccine data."""
    
    # Create a 2x2 grid (we'll use 3 spots)
    fig, axes = plt.subplots(2, 2, figsize=(18, 14))
    fig.suptitle('Comprehensive COVID-19 Vaccine Analysis (2021-2025)', 
                 fontsize=20, fontweight='bold', y=0.98)

    # ---------------------------------------------------------
    # GRAPH 1: Effectiveness Over Time
    # ---------------------------------------------------------
    ax1 = axes[0, 0]
    weeks_inf = [4, 10, 20]
    eff_inf = [52.2, 32.6, 20.4]
    weeks_hosp = [4, 10, 24]
    eff_hosp = [66.8, 57.1, 39.2]

    ax1.plot(weeks_inf, eff_inf, marker='o', linewidth=3, label='Against Infection', color='#2E86AB')
    ax1.plot(weeks_hosp, eff_hosp, marker='s', linewidth=3, label='Against Hospitalization', color='#A23B72')
    ax1.axhline(y=64, color='#F18F01', linestyle='--', label='Against Death (6mo): 64%')

    ax1.set_title('Vaccine Effectiveness Waning Over Time', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Weeks Post-Vaccination')
    ax1.set_ylabel('Effectiveness (%)')
    ax1.set_ylim(0, 100)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # ---------------------------------------------------------
    # GRAPH 2: Effectiveness by Age Group (2024-2025)
    # ---------------------------------------------------------
    ax2 = axes[0, 1]
    age_groups = ['9mo-4yr', '5-17yr', '18-64yr', '65+ IC*', '65+ Comp*']
    eff_ed = [76, 56, 33, 0, 0]
    eff_hosp_age = [0, 0, 33, 45.5, 40]

    x = np.arange(len(age_groups))
    width = 0.35

    ax2.bar(x - width/2, eff_ed, width, label='ED/UC Visits', color='#06A77D', alpha=0.8)
    ax2.bar(x + width/2, eff_hosp_age, width, label='Hospitalization', color='#D62246', alpha=0.8)

    ax2.set_title('Effectiveness by Age Group (Latest Data)', fontsize=14, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(age_groups)
    ax2.set_ylabel('Effectiveness (%)')
    ax2.set_ylim(0, 100)
    ax2.legend()
    ax2.text(0.5, -0.15, '*IC: Immunocompetent, Comp: Immunocompromised', 
             transform=ax2.transAxes, ha='center', style='italic')

    # ---------------------------------------------------------
    # GRAPH 3: Side Effects vs Effectiveness by Dose
    # ---------------------------------------------------------
    ax3 = axes[1, 0]
    doses = ['Dose 1', 'Dose 2', 'Dose 3', 'Dose 4']
    local_react = [75, 80, 70, 65]
    syst_react = [55, 65, 60, 55]
    eff_by_dose = [90, 92, 52, 36.5]

    ax3_twin = ax3.twinx()
    x_doses = np.arange(len(doses))
    
    ax3.bar(x_doses - 0.15, local_react, 0.3, label='Local Reactions', color='#FFA69E')
    ax3.bar(x_doses + 0.15, syst_react, 0.3, label='Systemic Reactions', color='#FAE5A0')
    ax3_twin.plot(x_doses, eff_by_dose, marker='D', color='#2A9D8F', linewidth=3, label='Effectiveness')

    ax3.set_title('Side Effects vs. Effectiveness per Dose', fontsize=14, fontweight='bold')
    ax3.set_xticks(x_doses)
    ax3.set_xticklabels(doses)
    ax3.set_ylabel('Reaction Frequency (%)')
    ax3_twin.set_ylabel('Effectiveness Against Infection (%)', color='#2A9D8F')
    ax3.set_ylim(0, 100)
    ax3_twin.set_ylim(0, 100)
    
    # Combine legends
    lines, labels = ax3.get_legend_handles_labels()
    lines2, labels2 = ax3_twin.get_legend_handles_labels()
    ax3.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=9)

    # ---------------------------------------------------------
    # EMPTY SLOT (Bottom Right) - Info Text
    # ---------------------------------------------------------
    ax4 = axes[1, 1]
    ax4.axis('off')
    info_text = (
        "Key Findings:\n\n"
        "1. Protection against infection wanes quickly\n"
        "   (52% -> 20% in 5 months).\n"
        "2. Protection against severe disease remains\n"
        "   robust (>60%).\n"
        "3. Children (9mo-4yr) show highest initial\n"
        "   effectiveness (76%).\n"
        "4. Side effects peak at Dose 2 and decrease\n"
        "   with subsequent boosters."
    )
    ax4.text(0.1, 0.5, info_text, fontsize=14, va='center', fontweight='medium',
             bbox=dict(facecolor='white', alpha=0.5, boxstyle='round,pad=1'))

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    # Save output
    output_file = 'vaccine_analysis_dashboard.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Successfully generated: {os.path.abspath(output_file)}")
    plt.show()

if __name__ == "__main__":
    setup_style()
    create_visualizations()
