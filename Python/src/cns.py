protocols = {
    "transfer": 1,
    "request": 2
}

def get_name(label):
    # returns a protocol integer represented by a label for the header generation
    label = label.lower()
    for lbl, value in protocols:
        if label == lbl:return value
        else:return None