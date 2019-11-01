import numpy as np

def msd(N, replicates):

    """
    Calculates the mean square displacement for a particle as a function of time.

    Arguments:
    ----------
    N : int
        Number of random walk steps to complete.
    replicates : int
        Number of particle replicates that will be sampled.

    Returns:
    --------
    msd : array-like, 1D
        Mean square replacement as a function of random walk steps.

    """

    displacements = []

    for rep in range(replicates):

        # create new particle, execute random walk and compute distances over the trajectory
        particle = Particle()
        particle.random_walk(N)
        displaced = np.sqrt(particle.trajectory[:,0]**2 + particle.trajectory[:,1]**2)

        displacements.append(displaced)

    # compute mean square displacement by averaging over replicates
    msd = np.average(displacements, axis=0)

    return msd
