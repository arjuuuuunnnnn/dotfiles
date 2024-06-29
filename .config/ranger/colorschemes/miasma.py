# Transparent Miasma color scheme for ranger

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Miasma(ColorScheme):
    def __init__(self):
        # Color palette based on the Miasma screenshot, with transparent background
        self.foreground = 187  # Light grayish green
        self.bright_yellow = 221 # Bright yellow for "Neovim" text
        self.muted_yellow = 180 # Muted yellow for some text
        self.orange = 173      # Orange for some highlights
        self.green = 107       # Green for directories and some text
        self.bright_green = 149 # Brighter green for highlights
        self.blue = 67         # Blue for some UI elements
        self.purple = 103      # Purple for some text
        self.red = 174         # Red for errors or warnings
        self.gray = 240        # Dark gray for less important text

    def use(self, context):
        fg, bg, attr = self.foreground, default, normal

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr |= reverse
            if context.empty or context.error:
                fg = self.red
            if context.border:
                fg = self.gray
            if context.media:
                fg = self.purple
            if context.container:
                fg = self.blue
            if context.directory:
                fg = self.green
                attr |= bold
            elif context.executable and not any((context.media, context.container,
                                                 context.fifo, context.socket)):
                fg = self.bright_yellow
                attr |= bold
            if context.socket:
                fg = self.orange
                attr |= bold
            if context.fifo or context.device:
                fg = self.blue
                attr |= bold
            if context.link:
                fg = self.bright_green if context.good else self.red
            if context.tag_marker and not context.selected:
                attr |= bold
                fg = self.bright_yellow
            if not context.selected and (context.cut or context.copied):
                fg = self.gray
                attr |= bold
            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    fg = self.bright_yellow

        elif context.in_titlebar:
            fg = self.green if context.hostname else self.bright_yellow
            if context.directory:
                fg = self.green
            elif context.tab:
                fg = self.foreground if context.good else self.bright_yellow
            elif context.link:
                fg = self.bright_green

        elif context.in_statusbar:
            fg = self.foreground
            if context.permissions:
                if context.good:
                    fg = self.green
                elif context.bad:
                    fg = self.red
            if context.marked:
                attr |= bold | reverse
                fg = self.bright_yellow
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = self.red
            if context.loaded:
                fg = self.orange

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = self.blue
            if context.selected:
                attr |= reverse
            if context.loaded:
                if context.selected:
                    fg = self.orange
                else:
                    fg = self.green

        return fg, bg, attr
