from utils.curve_handling import plot, complete_curves
from some_library import read_png

if __name__ == "__main__":
    input_path = 'dataset/path_to_image.png'  # Adjust the path accordingly
    paths_XYs = read_png(input_path)
    completed_curves = complete_curves(paths_XYs)
    plot(completed_curves, 'output/completed_curves.png')
