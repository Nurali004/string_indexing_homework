def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if len(s)>=5:
        return len(s)*'*'   
    else:
        return false     
s="dsjhdshdjhd"
print(main(s))