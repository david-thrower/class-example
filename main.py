
from tea.tea import Tea

# Tea

TANNIN_CONTENT_TEA = 2
NAME_TEA = 'my tea'
COLOR_TEA = 'black'
FLAVOR_TEA = 'slightly bitter'

# Green tea:

THEANNINE_CONTENT_GREEN_TEA = 0.7
TANNIN_CONTENT_GREN_TEA = 0.5
NAME_GREEN_TEA = 'My favorite tea!'
COLOR_GREEN_TEA = 'green'
FLAVOR_GREEN_TEA = 'fruity'

if __name__ == "__main__":
    my_tea = Tea(tannin_content_percent=TANNIN_CONTENT_TEA,
                 name=NAME_TEA,
                 color=COLOR_TEA,
                 flavor=FLAVOR_TEA)
    my_tea.print_summary()

    # Recommended tutorial: Uncomment and make this pass
    # my_green_tea = GreenTea(l_theannine_content_percent=THEANNINE_CONTENT_GREEN_TEA,
    #                         tannin_content_percent=TANNIN_CONTENT_GREN_TEA,
    #                         name=NAME_GREEN_TEA,
    #                         color=COLOR_GREEN_TEA,
    #                         flavor=FLAVOR_GREEN_TEA)
