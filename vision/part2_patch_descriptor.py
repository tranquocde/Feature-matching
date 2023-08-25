#!/usr/bin/python3

import numpy as np


def compute_normalized_patch_descriptors(
    image_bw: np.ndarray, X: np.ndarray, Y: np.ndarray, feature_width: int
) -> np.ndarray:
    """Create local features using normalized patches.

    Normalize image intensities in a local window centered at keypoint to a
    feature vector with unit norm. This local feature is simple to code and
    works OK.

    Choose the top-left option of the 4 possible choices for center of a square
    window.

    Args:
        image_bw: array of shape (M,N) representing grayscale image
        X: array of shape (K,) representing x-coordinate of keypoints
        Y: array of shape (K,) representing y-coordinate of keypoints
        feature_width: size of the square window

    Returns:
        fvs: array of shape (K,D) representing feature descriptors
    """

    ###########################################################################
    # TODO: YOUR CODE HERE                                                    #
    ###########################################################################
    fvs = np.zeros((len(X), feature_width ** 2))
    # padding the image with pad_size = feature_width/2
    padded_image = np.pad(image_bw, feature_width // 2, 'constant', constant_values=(0,))
    new_X, new_Y = Y + feature_width // 2, X + feature_width // 2

    for count, (i, j) in enumerate(zip(new_X, new_Y)):
        if feature_width % 2 == 0:
            start_i, start_j = i - (feature_width // 2 - 1), j - (feature_width // 2 - 1)
        else:
            start_i, start_j = i - feature_width // 2 , j - feature_width // 2
        # retrieve the image patch
        image_patch = padded_image[start_i:start_i+feature_width, start_j:start_j+feature_width]
        #normalize the patch 
        image_norm = image_patch / np.linalg.norm(image_patch)
        #The np.ravel() function in NumPy is used to flatten a multi-dimensional
        #array into a 1D array. It returns a flattened view of the input array,
        #which means that any modifications made to the flattened array will 
        #affect the original array as w
        fvs[count] = image_norm.ravel() # flatten the norm image patch and add to fvs

    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return fvs
