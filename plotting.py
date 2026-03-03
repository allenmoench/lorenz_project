# plotting.py
"""Plotting utilities for Lorenz63 ensemble experiments."""
import numpy as np
import matplotlib.pyplot as plt


def plot_attractor(ax, model_evolution, color="steelblue", alpha=0.3, linewidth=0.5):
    """Plot a single Lorenz attractor trajectory in x-z phase space.

    Parameters
    ----------
    ax : matplotlib Axes
        The axes to plot on.
    trajectory : np.ndarray
        Trajectory array, shape (n_steps+1, 3). Columns are [x, y, z].
    color : str
        Line color.
    alpha : float
        Line transparency.
    linewidth : float
        Line width.

    Hint
    ----
    trajectory[:, 0] is x, trajectory[:, 2] is z.
    Use ax.plot(x, z, ...) for the butterfly view.
    """
    # TODO: plot x vs z

    # # Where does "ax" come in? This is the part I don't get... aren't we only plotting one attractor? I thought "ax" was for multiple sub-plots.
    # fig, ax = plt.subplots()
    x = model_evolution[:, 0]
    z = model_evolution[:, 2]
    ax.plot(x, z, color=color, alpha=0.3, linewidth=0.5)
    # ax.plot(x, z, color="steelblue", alpha=0.3, linewidth=0.5)




def plot_ensemble(ax, ensemble_trajectories, reference_trajectory=None,
                  ensemble_color="firebrick", ref_color="steelblue",
                  title=None):
    """Plot an ensemble of trajectories on a single axes.

    Parameters
    ----------
    ax : matplotlib Axes
        The axes to plot on.
    ensemble_trajectories : np.ndarray
        Shape (n_members, n_steps+1, 3).
    reference_trajectory : np.ndarray, optional
        A long reference trajectory, shape (n_ref_steps+1, 3), plotted
        lightly in the background to show the full attractor.
    ensemble_color : str
        Color for ensemble member lines.
    ref_color : str
        Color for the reference attractor.
    title : str, optional
        Panel title (e.g., "(a) Left lobe" or "(b) Saddle region").

    Hint
    ----
    1. If reference_trajectory is provided, call plot_attractor() for it
       with low alpha to draw the background butterfly.
    2. Loop over ensemble members: for i in range(ensemble_trajectories.shape[0]):
       and call plot_attractor() for each member with ensemble_color and higher alpha.
    3. Set title, labels, aspect ratio as desired.
    """
    # TODO: implement ensemble plotting

    if reference_trajectory is not None:
        plot_attractor(ax, reference_trajectory, color=ensemble_color, alpha=0.05, linewidth=0.5)

    for i in range (ensemble_trajectories.shape[0]):
        plot_attractor(ax, ensemble_trajectories[i], color=ref_color, alpha=0.3, linewidth=0.5)

    if title is not None:
        ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("z")
    ax.set_aspect("auto")

def plot_ensemble_panels(ensemble_list, reference_trajectory, titles,
                         figsize=(18, 5), save_path=None):
    """Create a multi-panel figure showing ensembles from different initial regions.

    Parameters
    ----------
    ensemble_list : list of np.ndarray
        List of ensemble arrays, each shape (n_members, n_steps+1, 3).
        One array per panel.
    reference_trajectory : np.ndarray
        Long reference trajectory for the background attractor.
    titles : list of str
        Title for each panel (e.g., ["(a) Left lobe", "(b) Saddle", "(c) Right lobe"]).
    figsize : tuple
        Figure size.
    save_path : str, optional
        If provided, save the figure to this path.

    Returns
    -------
    fig, axes

    Hint
    ----
    1. fig, axes = plt.subplots(1, len(ensemble_list), figsize=figsize)
    2. Loop: for ax, ensemble, title in zip(axes, ensemble_list, titles):
           call plot_ensemble(ax, ensemble, reference_trajectory, title=title)
    3. plt.tight_layout()
    4. If save_path: plt.savefig(save_path, dpi=150, bbox_inches='tight')
    """
    # TODO: implement multi-panel figure
    fig, axes = plt.subplots(1, len(ensemble_list), figsize=figsize)
    for ax, ensemble, title in zip(axes, ensemble_list, titles):
        print(ensemble.shape, ensemble[:20,:])
        # print(reference_trajectory.shape, reference_trajectory[:20,:])
        plot_ensemble(ax, ensemble, reference_trajectory, title=title)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    return fig, axes


if __name__ == "__main__":
    # ── Test your code! ──────────────────────────────────────────────
    # Run this file directly:  python -m lorenz_project.plotting
    # A plot window should pop up with a random walk trajectory.
    # If you see a line on the axes, your plot_attractor() works.

    fake_traj = np.cumsum(np.random.randn(500, 3) * 0.5, axis=0)
    fig, ax = plt.subplots()
    plot_attractor(ax, fake_traj)
    ax.set_title("plotting.py: visual test")
    plt.show()
    print("plotting.py: visual check — does the plot look reasonable?")
