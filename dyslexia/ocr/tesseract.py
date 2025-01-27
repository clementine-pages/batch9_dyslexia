import pytesseract

def extract_text_from_image(img, lang='fra'):
    """Retrieves the text on an image using the
    tesseract backend.

    tesseract must be installed

    Parameters
    ----------
    img : array like or Image
        Source image
    lang: str, default 'fra'
        Language to use

    Returns
    -------
    str:
        Result of the ``pytesseract.image_to_string()`` 
        method
    """
    
    res = pytesseract.image_to_string(img, lang=lang)
    
    return res