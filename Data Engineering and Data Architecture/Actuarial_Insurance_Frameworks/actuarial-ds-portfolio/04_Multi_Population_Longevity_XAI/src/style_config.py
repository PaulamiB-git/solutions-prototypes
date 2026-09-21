import matplotlib.pyplot as plt
import seaborn as sns
import os


# Paper-optimized font sizes (legible on A4 at 0.8\textwidth)
_STYLE_CONFIG = {
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "sans-serif"],
    "axes.titlesize": 20,
    "axes.titleweight": "normal",
    "axes.titlelocation": "center",
    "axes.titlepad": 20,
    "axes.labelsize": 16,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "legend.fontsize": 13,
    "figure.figsize": (10, 6),
    "figure.dpi": 300,
    "axes.grid": True,
    "grid.alpha": 0.15,
    "grid.linestyle": "-",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
    "lines.linewidth": 1.8,
    "savefig.dpi": 300,
    "savefig.bbox": "tight"
}


def set_style():
    """
    Sets the global aesthetic standard for the project.
    Font sizes are optimized for A4 paper legibility at 0.8 textwidth.
    Palette: Viridis (perceptually uniform, colorblind-friendly).
    Typography: Helvetica.
    """
    plt.rcParams.update(_STYLE_CONFIG)

    COUNTRIES = {
        'CHE': 'Switzerland',
        'SWE': 'Sweden',
        'NOR': 'Norway',
        'DEUTW': 'West Germany',
        'NLD': 'Netherlands',
        'JPN': 'Japan'
    }

    sns.set_palette(sns.color_palette("viridis", len(COUNTRIES)))

    print("Configuration complete using central style.")
    return COUNTRIES


def save_dual(fig, save_path, paper_dir="../latex/figures"):
    """
    Saves a figure twice:
    1. Full resolution with title for the notebook (save_path)
    2. Without title, resized for LaTeX/Overleaf (paper_dir)
    """
    # Save full resolution for notebook (with title)
    fig.savefig(save_path)

    # Save paper version: remove title, save, then restore title
    os.makedirs(paper_dir, exist_ok=True)
    filename = os.path.basename(save_path)
    paper_path = os.path.join(paper_dir, filename)

    # Remove titles from all axes
    titles = {}
    for ax in fig.get_axes():
        titles[id(ax)] = ax.get_title()
        ax.set_title("")

    # Save without title to a temporary path
    temp_path = save_path + ".paper_tmp.png"
    fig.savefig(temp_path)

    # Restore titles so the notebook display keeps them
    for ax in fig.get_axes():
        ax.set_title(titles[id(ax)])

    # Resize for Overleaf
    from PIL import Image
    img = Image.open(temp_path)
    w, h = img.size
    max_width = 1200
    if w > max_width:
        ratio = max_width / w
        img = img.resize((max_width, int(h * ratio)), Image.LANCZOS)
    img.save(paper_path, 'PNG', optimize=True)

    # Clean up temp file
    os.remove(temp_path)
