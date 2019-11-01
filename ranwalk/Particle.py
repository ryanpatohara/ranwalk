import numpy as np

class Particle:

    """Object than undergoes a 2-dimensional lattice random walk."""

    def __init__(self):

        """Constructor for the Particle class."""

        self.position = (0,0)
        self.trajectory = np.array([self.position])

    def random_walk(self, N):

        """
        Executes a 2-dimensional lattice random walk for N-steps.

        Arguments:
        ----------
        N : int
            Number random walk steps.

        """

        walk_coords = []

        for i in range(N):

            # Random selection of next move: right, up, left, or down.
            xy = np.random.randint(2)
            direction = np.random.randint(2)*2 - 1

            # Update the current position and store trajectory.
            move_x = xy * direction
            move_y = (1-xy) * direction

            x = self.position[0]
            y = self.position[1]

            self.position = (x + move_x, y + move_y)
            walk_coords.append(self.position)

        # Append latest random walk to the instance trajectory attribute.
        self.trajectory = np.concatenate((self.trajectory, np.array(walk_coords)))
