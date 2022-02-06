import numpy as np

from reconstruction.global_hits import global_fit, double_fit


def fit_data(
    hit_layers,
    n_hit_layers_x,
    n_hit_layers_y,
    xpos_xlayers,
    ypos_xlayers,
    xpos_ylayers,
    ypos_ylayers,
    vertical,
    slope_threshold,
):
    residuals_ts_x = None
    residuals_ts_y = None
    # hit_layers_ts_x = None
    # hit_layers_ts_y = None
    slope_ts_x = None
    slope_ts_y = None
    top_y_ylayer = None
    bottom_y_ylayer = None
    top_y_xlayer = None
    bottom_y_xlayer = None
    y_xlayer = None
    y_ylayer = None

    x = np.linspace(0, 200, 50)
    # global fit on x
    if n_hit_layers_x >= 3:  # if more than 2 layers hit on x:
        m_x, q_x = global_fit(xpos_xlayers, ypos_xlayers)  # calculate global fit
        y_xlayer = m_x * x + q_x
        get_residual = np.abs(m_x) >= slope_threshold if vertical else m_x
        if get_residual:
            # hit_layers_ts_x = hit_layers_x
            residuals_ts_x = (
                m_x * np.asarray(xpos_xlayers) + q_x - np.asarray(ypos_xlayers)
            )
            slope_ts_x = m_x
        # print(residuals_x)

    # global fit on y
    if n_hit_layers_y >= 3:
        m_y, q_y = global_fit(xpos_ylayers, ypos_ylayers)
        y_ylayer = m_y * x + q_y
        get_residual = np.abs(m_y) >= slope_threshold if vertical else m_y
        if get_residual:
            # hit_layers_ts_y = hit_layers_y
            residuals_ts_y = (
                m_y * np.asarray(xpos_ylayers) + q_y - np.asarray(ypos_ylayers)
            )
            slope_ts_y = m_y
        # print(residuals_y)

    # top and bottom fit x
    hit_layers = np.asarray(hit_layers)
    if len(np.unique(hit_layers[hit_layers >= 5])) >= 4:  # len(xpos_xlayers) >= 4:
        top_y_xlayer, bottom_y_xlayer = double_fit(
            x, xpos_xlayers, ypos_xlayers, separation=-2
        )

    # top and bottom fit y
    if len(np.unique(hit_layers[hit_layers < 5])) >= 4:  # len(xpos_ylayers) >= 4:
        top_y_ylayer, bottom_y_ylayer = double_fit(
            x, xpos_ylayers, ypos_ylayers, separation=-2
        )

    return (
        y_xlayer,
        y_ylayer,
        residuals_ts_x,
        residuals_ts_y,
        slope_ts_x,
        slope_ts_y,
        top_y_xlayer,
        bottom_y_xlayer,
        top_y_ylayer,
        bottom_y_ylayer,
    )
