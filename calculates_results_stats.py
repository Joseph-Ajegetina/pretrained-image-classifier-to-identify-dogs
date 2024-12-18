def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    images = results_dic.keys()
    values = results_dic.values()
    n_imgs = len(images)
    n_dogs_img = 0
    match_count = 0
    correct_dogs_count = 0
    correct_breed_count = 0
    for img_index,value in enumerate(values):
        if value[3] == 1:
            n_dogs_img += 1
        if value[2] == 1:
            match_count += 1
        if value[3] == value[4] == 1:
            correct_dogs_count += 1
        if value[3] == value[4] == 1 and value[2] == 1:
            correct_breed_count += 1

    results_stats_dic = {
    'n_images': n_imgs,
    'n_dogs_img': n_dogs_img,
    'n_notdogs_img': n_imgs - n_dogs_img,
    'n_match': match_count,
    'n_correct_dogs': correct_dogs_count,
    'n_correct_notdogs': n_imgs - correct_dogs_count,
    'n_correct_breed': correct_breed_count,
    'pct_match': (match_count/n_imgs) * 100,
    'pct_correct_dogs': (correct_dogs_count/n_dogs_img) * 100,
    'pct_correct_breed': (correct_breed_count/n_dogs_img) * 100,
    'pct_correct_notdogs': 100 - (correct_dogs_count/n_dogs_img) * 100,
     }
    
    return results_stats_dic
