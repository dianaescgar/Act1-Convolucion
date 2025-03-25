import numpy as np
import cv2
import matplotlib.pyplot as plt
 
# Función que ayuda a realizar la convolución en un fragmento de la imagen
def conv_helper(fragment, kernel):
    f_row, f_col = fragment.shape  # Dimensiones del fragmento de imagen
    k_row, k_col = kernel.shape  # Dimensiones del kernel
    result = 0.0  # Inicializa el valor acumulativo de la convolución

    # Recorre cada píxel del fragmento, aplicando la multiplicación con el kernel
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row, col] * kernel[row, col]

    return result  # Resultado de la convolución en este fragmento

# Función que aplica la convolución a una imagen dada un kernel
def convolution(image, kernel):
    image_row, image_col = image.shape  # Dimensiones de la imagen
    kernel_row, kernel_col = kernel.shape  # Dimensiones del kernel

    output = np.zeros(image.shape) # Matriz de ceros del mismo tamaño que la imagen original

    # Recorre cada píxel de la imagen
    for row in range(image_row):
        for col in range(image_col):
            # Aplica la convolución en la región correspondiente de la imagen
            output[row, col] = conv_helper(
                image[row:row + kernel_row, col:col + kernel_col],  # Extrae un fragmento de la imagen
                kernel  # Aplica el kernel sobre el fragmento
            )

    # Muestra la imagen resultante en escala de grises
    plt.imshow(output, cmap='gray')
    plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col))
    plt.show()

    return output  # Devuelve la imagen ya con filtro aplicado