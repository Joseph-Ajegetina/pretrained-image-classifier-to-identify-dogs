
import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser( description="Process commands from user running the program" )
    
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument("--dir", help="Image Folder with default value 'pet_images'", type=str, default='pet_images')
    parser.add_argument("--arch", help="CNN Model Architecture with default value 'vgg'", type=str, default='vgg')
    parser.add_argument("--dogfile", help="Text File with Dog Names with default value 'dognames.txt'", type=str, default='dognames.txt')

    return parser.parse_args()
