def letterhead(title):
    len_title = len(title)
    
    astrik = '*'
    num_top_bar = (2*astrik) * len_title +
    middle_bar = '*  ' + title + '  *'

    print(num_top_bar)
    print(middle_bar)
    print(num_top_bar)

    return None
