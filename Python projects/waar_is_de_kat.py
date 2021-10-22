import random

def print_box_line(num_boxes, opened=0, cat=False):
    """Print a line with boxes, optionally with one open and with a cat

    Args:
        num_boxes (int): number of boxes to draw
        opened (int, optional): which box has been opened. Defaults to 0, not opening any box.
        cat (bool, optional): was there a cat in the box. Defaults to False.
    """
    if (opened == 0):
        line_open = ""
        line_box = " [ ] "*num_boxes
        line_nums = ""
        for i in range(1,num_boxes+1):
            line_nums = f"{line_nums}  {i}  "
    elif not cat:
        line_open = "     "*(opened-1)
        line_open = line_open + "\   /"
        line_box = " [ ] "*num_boxes
        line_nums = ""
        for i in range(1,num_boxes+1):
            line_nums = f"{line_nums}  {i}  "
    else:
        line_open = "     "*(opened-1)
        line_open = line_open + "\ :3/"
        line_box = " [ ] "*num_boxes
        line_nums = ""
        for i in range(1,num_boxes+1):
            line_nums = f"{line_nums}  {i}  "
    
    print(line_open)
    print(line_box)
    print(line_nums)
    

def waar_is_kat(aantal_dozen):
    """Interactive game where the user chooses from a number of boxes, to find the one the cat is in. 
    The cat move to adjecent boxes if not found that found. 

    Args:
        aantal_dozen (int): number of boxes to play with
    """
    cat_box = random.randint(1,aantal_dozen)

    num_tries = 1

    print(cat_box)

    print_box_line(aantal_dozen)

    inp_num = ""
    while inp_num != "/q":
        inp_num = input("Choose a box to check: ")
        if inp_num == "/q":
            break
        if not inp_num.isdigit():
            print(f"Input must be integer, not '{inp_num}'. Try again.")
            continue
        
        inp_num = int(inp_num)
        if (inp_num > aantal_dozen):
            print(f"Input must be less than the total number of boxes! Try again.")
            continue
        
        if inp_num == cat_box:
            print_box_line(aantal_dozen, inp_num, True)
            print(f"The cat has been found in {num_tries} rounds! Congr-cats!")
            break
        else: 
            if cat_box == aantal_dozen:
                cat_box -= 1
            elif cat_box == 1:
                cat_box += 1
            else:
                cat_box = random.choice([cat_box-1, cat_box+1])
            print_box_line(aantal_dozen, inp_num, False)
            print("The cat wasn't there. Try again!")
            num_tries += 1
    
    print("I hope you liked the game!")

if __name__ == "__main__":

    numbox = input("How many boxes you want to play with? >")
    waar_is_kat(int(numbox))
