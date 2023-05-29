"""Healper function to translate actual name to proper name"""
def translate_category_name(category_name):
    """
    Translate the 20 group names to proper name using a dictionary
    """
    translation_dict = {
        'alt.atheism': 'Atheism',
        'comp.graphics': 'Computer Graphics',
        'comp.os.ms-windows.misc': 'MS Windows OS Miscellaneous',
        'comp.sys.ibm.pc.hardware': 'IBM PC Hardware',
        'comp.sys.mac.hardware': 'Macintosh Hardware',
        'comp.windows.x': 'Windows X (X Window System)',
        'misc.forsale': 'Miscellaneous Items for Sale',
        'rec.autos': 'Automobiles',
        'rec.motorcycles': 'Motorcycles',
        'rec.sport.baseball': 'Baseball',
        'rec.sport.hockey': 'Hockey',
        'sci.crypt': 'Cryptography',
        'sci.electronics': 'Electronics',
        'sci.med': 'Medicine',
        'sci.space': 'Space Exploration',
        'soc.religion.christian': 'Christianity',
        'talk.politics.guns': 'Political Discussions on Guns',
        'talk.politics.mideast': 'Political Discussions on the Middle East',
        'talk.politics.misc': 'Miscellaneous Political Discussions',
        'talk.religion.misc': 'Miscellaneous Religious Discussions'
    }

    return translation_dict.get(category_name, category_name)