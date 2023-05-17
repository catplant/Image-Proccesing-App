from PIL import Image
import os


# function for opening an image from a list
def list_open(file_list):
    # filter the list to include only image files
    image_list = [file for file in file_list if file.endswith('.jpg') or file.endswith('.png')]

    # print the list of image files
    print('Image Files:')
    for i, file in enumerate(image_list):
        print(i+1, file)

    # ask the user to select a file
    while True:
        try:
            user_selected_file = int(input('Enter the number of the file to open: '))
            if user_selected_file not in range(1, len(image_list) + 1):
                raise ValueError
            break
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    # open the selected file
    selected_image = Image.open(image_list[user_selected_file - 1])

    return selected_image


def channel_swap(image):
    # split the image into its Red, Green, and Blue component channels
    r, g, b = image.split()

    # swap the channels
    swapped_image = Image.merge('RGB', (g, b, r))

    # return the swapped image
    return swapped_image


def pixelate(image, pixel_size):
    # calculate the new dimensions for the pixelated image
    resized_image = image.resize((pixel_size, pixel_size))

    # resize the image to the new dimensions using the NEAREST resampling filter
    pixelated_image = resized_image.resize(image.size, Image.NEAREST)

    # return the pixelated image
    return pixelated_image


def save_image(image):
    # ask the user for a filename
    while True:
        filename = input('Enter a filename for the saved image: ')
        if not filename:
            print('Invalid filename. Please try again.')
        else:
            break

    # ask the user for the file format
    while True:
        file_format = input('Enter the file format (JPG, PNG): ')
        if file_format.upper() in ('JPG', 'PNG'):
            break
        else:
            print("Invalid file format. Please enter 'JPG', 'PNG'.")

    # save the image as a new file with the specified filename and format
    file_ext = file_format.lower()
    if file_ext == 'jpg':
        file_ext = 'jpeg'
    image.save(f'{filename}.{file_ext}', format=file_format)

    print(f'{filename}.{file_format} saved successfully.')


def main():
    # list all files in the current directory
    file_list = os.listdir()

    # call the list_open function with the file list to open an image
    selected_image = list_open(file_list)

    while True:
        # display menu options
        print('\nMENU')
        print('1. Show the original image')
        print('2. Swap the image channels')
        print('3. Pixelate the image')
        print('4. Save the current image')
        print('5. Exit the program')

        # ask the user to select an option
        while True:
            try:
                selected_option = int(input('Enter an option: '))
                if selected_option not in range(1, 6):
                    raise ValueError
                break
            except ValueError:
                print('Invalid input. Please enter a valid number.')

        if selected_option == 1:
            # show the original image
            selected_image.show()

        elif selected_option == 2:
            # swap the channels of the image
            swapped_image = channel_swap(selected_image)
            swapped_image.show()
            selected_image = swapped_image

        elif selected_option == 3:
            # pixelate the image
            while True:
                try:
                    pixel_size = int(input('Enter the pixel size (integer value): '))
                    if pixel_size <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print('Invalid input. Please enter a positive integer.')
            pixelated_image = pixelate(selected_image, pixel_size)
            pixelated_image.show()
            selected_image = pixelated_image

        elif selected_option == 4:
            save_image(selected_image)

        elif selected_option == 5:
            exit()


main()
