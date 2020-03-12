def __call__(self, *args, **kwargs):
    """Calling a Tag like a function is the same as calling its
    find_all() method. Eg. tag('a') returns a list of all the A tags
    found within this tag."""
    return self.find_all(*args, **kwargs)
