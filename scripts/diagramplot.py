import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_aws_environment_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))

    # Define properties for each environment layer
    environments = ["Development", "Testing", "Staging", "Production"]
    y_positions = [0.8, 0.6, 0.4, 0.2]
    colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

    # Draw rectangles for each environment
    for env, y, color in zip(environments, y_positions, colors):
        rect = patches.Rectangle((0.1, y), 0.8, 0.15, linewidth=2, edgecolor='black', facecolor=color, alpha=0.7)
        ax.add_patch(rect)
        ax.text(0.5, y + 0.075, env, horizontalalignment='center', verticalalignment='center', fontsize=14, color='black')

    # Draw shared services
    shared_services_rect = patches.Rectangle((0.1, 0.95), 0.8, 0.05, linewidth=2, edgecolor='black', facecolor='#a6d854', alpha=0.7)
    ax.add_patch(shared_services_rect)
    ax.text(0.5, 0.975, 'Shared Services (e.g., Logging, Monitoring, Backups)', horizontalalignment='center', verticalalignment='center', fontsize=12, color='black')

    # Add arrows to indicate flow
    for y in y_positions:
        ax.arrow(0.5, y + 0.15, 0, -0.03, head_width=0.02, head_length=0.02, fc='black', ec='black')

    # Set limits and labels
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Save the diagram as an image file
    plt.savefig("/mnt/data/aws_environment_management_diagram.png")
    plt.show()

# Generate the diagram
create_aws_environment_diagram()
