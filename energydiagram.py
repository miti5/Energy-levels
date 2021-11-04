import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from .box_notation import plot_orbital_boxes


class ED:
    def __init__(self, aspect='equal'):
        # plot parameters
        self.ratio = 1.6181
        self.dimension = 'auto'
        self.space = 'auto'
        self.offset = 'auto'
        self.offset_ratio = 0.02
        self.color_bottom_text = 'black'
        self.aspect = aspect
        # data
        self.pos_number = 0
        self.energies = []
        self.positions = []
        self.colors = []
        self.top_texts = []
        self.bottom_texts = []
        self.left_texts = []
        self.right_texts = []
        self.links = []
        self.arrows = []
        self.electons_boxes = []
        # matplotlib fiugre handlers
        self.fig = None
        self.ax = None

    def add_level(self, energy, bottom_text='', position=None, color='b',
                  top_text='', right_text='', left_text=''):
        '''
        Method of ED class
        This method add a new energy level to the plot.

        Parameters
        ----------
        energy : int
                The energy of the level in eV
        bottom_text  : str
                The text on the bottom of the level (label of the level)
                (default '')
        right_text  : str
                The text on the right of the level (default '')
        left_text  : str
                The text on the left of the level (default '')
        position  : str
                The position of the level in the plot. Keep it empty to add
                the level on the right of the previous level use 'last' as
                argument for adding the level to the last position used
                for the level before.
                An integer can be used for adding the level to an arbitrary
                position.
                (default  None)
        color  : str
                Color of the level  (default  'k')
        top_text  : str
                Text on the top of the level. By default it will print the
                energy of the level. (default  'Energy')



        Returns
        -------
        Append to the class data all the informations regarding the level added
        '''

        if position is None:
            position = self.pos_number + 1
            self.pos_number += 1
        elif isinstance(position, (int, float)):
            pass
        elif position == 'last' or position == 'l':
            position = self.pos_number
        else:
            raise ValueError(
                "Position must be None or 'last' (abrv. 'l') or in case an integer or float specifing the position. It was: %s" % position)
        if top_text == 'Energy':
            top_text = energy

        link = []
        self.colors.append(color)
        self.positions.append(position)
        self.energies.append(energy)
        self.top_texts.append(top_text)
        self.bottom_texts.append(bottom_text)
        self.left_texts.append(left_text)
        self.right_texts.append(right_text)
        self.links.append(link)
        self.arrows.append([])

    def add_arrow(self, start_level_id, end_level_id):
        '''
        Method of ED class
        Add a arrow between two energy levels using IDs of the level. Use
        self.plot(show_index=True) to show the IDs of the levels.

      


  
       
       




