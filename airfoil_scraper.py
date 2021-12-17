import requests
import matplotlib.pyplot as plt


def get_airfoil_coords(airfoil: str) -> tuple:
    """
    Get airfoil coords from UIUC website
    https://m-selig.ae.illinois.edu/ads/coord/__.dat
    :param airfoil: str of airfoil types
    :return: tuple of ([x coords], [y coords], plot_title)
    """
    url = 'https://m-selig.ae.illinois.edu/ads/coord/{}.dat'.format(airfoil.lower())

    response_text = requests.get(url).text

    if 'Not Found' in response_text:
        raise NameError('{} not found in UIUC database.'.format(airfoil))

    all_text = response_text.split('\n')
    x_coordinates, y_coordinates = [], []
    plot_title = ''

    for index, line in enumerate(all_text):
        if index == 0:
            plot_title = line.strip()
        else:
            try:
                line = line.strip()
                x, y = line.strip('' * line.count(' '))
                x = float(x.strip())
                y = float(y.strip())
                if x <= 1.0 and y <= 1.0:
                    x_coordinates.append(x)
                    y_coordinates.append(y)
            except ValueError:
                continue

    return x_coordinates, y_coordinates, plot_title


def plot_airfoil(x_coordinates: list, y_coordinates: list, plot_title: str) -> None:
    """
    Plot the airfoil coordinates given the list of coordinates

    :param x_coordinates: list of airfoil's x coordinates
    :param y_coordinates: list of airfoil's y coordinates
    :param plot_title: str to title as the plot's title
    :return: None
    """
    plt.plot(x_coordinates, y_coordinates, 'k-')

    plt.title('{} airfoil'.format(plot_title))
    plt.style.use('default')
    plt.xlim(-0.50, 1.25)
    plt.ylim(-1, 1)
    plt.show()


air_foil = 'naca2412'
try:
    x_values, y_values, title = get_airfoil_coords(air_foil)
    plot_airfoil(x_values, y_values, title)
except NameError:
    print('{} not in UIUC database, try again!'.format(air_foil))