# First fit heuristic for bin packing.

# Strategy:
# 1. Open a bin
# 2. Pick first item not yet placed.
# 3. Check if it fits in the first bin.
#      yes: place it, go to 2.
#      no: go to next open bin, go to 3.
# 4. If still not placed: open a new bin, place item, go to 2.


def first_fit(item_list, bin_capacity):
    """
    First fit heuristic for the bin packing problem.
    Input:
        item_list, a list of item sizes
        bin_capacity, a number representing the size of each empty box
    Output:
        List of what each bin contains.
    """
    # Start with one empty bin
    bins = [0]
    
    # Loop over the remaining items
    for item in item_list:
        
        # print(f'Checking the next item...')
        
        # Loop over the open bins
        for i in range(len(bins)):
            
            # print(f'Remaining bin capacity: {bin_capacity - bins[i]}')
            
            # Does it fit?
            if item <= bin_capacity - bins[i]:
                # print(f'The item fits')
                # print(f'Old bin list: {bins}')
                bins[i] = bins[i] + item
                # print(f'New value of b: {bins[i]}')
                # print(f'New bin list: {bins}')
                break
        
        else:
            # We have not placed the item, open new bin
            bins.append(item)
    
    return bins

    

# Test
item_list = [20] * 5
bin_capacity = 50
print(first_fit(item_list, bin_capacity))
# Expected result: [40, 40, 20]