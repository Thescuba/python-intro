def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        print(i,i + size)

sq_iterator = (x**2 for x in range(10)) 
for i in sq_iterator:
    print(i)