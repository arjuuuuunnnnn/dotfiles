# Everforest-inspired color scheme for ranger (greener version with transparent background)

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Everforest(ColorScheme):
    def __init__(self):
        # Everforest palette (adjusted for more green emphasis)
        self.fg = 187        # #d3c6aa
        self.green = 108     # #a7c080
        self.light_green = 142 # #b8bb26
        self.dark_green = 72  # #98971a
        self.aqua = 109      # #83c092
        self.yellow = 178    # #dbbc7f
        self.blue = 110      # #7fbbb3
        self.purple = 175    # #d699b6
        self.orange = 208    # #e69875
        self.red = 167       # #e67e80
        self.grey = 243      # #7a8478

        self.progress_bar_color = self.green

    def use(self, context):
        fg, bg, attr = self.fg, default, normal

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            if context.empty or context.error:
                fg = self.red
            if context.border:
                fg = self.grey
            if context.media:
                if context.image:
                    fg = self.yellow
                else:
                    fg = self.purple
            if context.container:
                fg = self.blue
            if context.directory:
                fg = self.green
                attr |= bold
            elif context.executable and not any((context.media, context.container,
                                                 context.fifo, context.socket)):
                fg = self.light_green
                attr |= bold
            if context.socket:
                fg = self.purple
                attr |= bold
            if context.fifo or context.device:
                fg = self.orange
                if context.device:
                    attr |= bold
            if context.link:
                fg = self.aqua if context.good else self.red
            if context.tag_marker and not context.selected:
                attr |= bold
                fg = self.dark_green
            if not context.selected and (context.cut or context.copied):
                fg = self.grey
                attr |= bold
            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    fg = self.yellow
            if context.badinfo:
                fg = self.red

        elif context.in_titlebar:
            attr |= bold
            if context.hostname:
                fg = self.green if context.good else self.red
            elif context.directory:
                fg = self.light_green
            elif context.tab:
                if context.good:
                    fg = self.dark_green
            elif context.link:
                fg = self.aqua

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = self.green
                elif context.bad:
                    fg = self.red
            if context.marked:
                attr |= bold | reverse
                fg = self.yellow
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = self.red
            if context.loaded:
                fg = self.progress_bar_color
            if context.vcsinfo:
                fg = self.aqua
                attr &= ~bold
            if context.vcscommit:
                fg = self.yellow
                attr &= ~bold

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = self.aqua

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    fg = self.green

        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = self.red
            elif context.vcschanged:
                fg = self.orange
            elif context.vcsunknown:
                fg = self.red
            elif context.vcsstaged:
                fg = self.green
            elif context.vcssync:
                fg = self.green
            elif context.vcsignored:
                fg = self.grey

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync or context.vcsnone:
                fg = self.green
            elif context.vcsbehind:
                fg = self.orange
            elif context.vcsahead:
                fg = self.blue
            elif context.vcsdiverged:
                fg = self.red
            elif context.vcsunknown:
                fg = self.red

        return fg, bg, attr
