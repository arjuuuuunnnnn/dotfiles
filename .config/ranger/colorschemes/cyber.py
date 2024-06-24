# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.
# CyberHack theme: A dark, neon-accented color scheme for the hacker aesthetic

from __future__ import absolute_import, division, print_function

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import (
    black, blue, cyan, green, magenta, red, white, yellow, default,
    normal, bold, reverse, default_colors,
)

class CyberHack(ColorScheme):
    progress_bar_color = 40  # Neon green

    def verify_browser(self, context, fg, bg, attr):
        if context.selected:
            attr = reverse
        else:
            attr = normal
        if context.empty or context.error:
            bg = 16  # Black
            fg = 196  # Bright red
        if context.border:
            fg = 240  # Dark gray
        if context.document:
            attr |= normal
            fg = 15  # Bright white
        if context.media:
            if context.image:
                fg = 13  # Neon pink
            elif context.video:
                fg = 208  # Neon orange
            elif context.audio:
                fg = 14  # Cyan
            else:
                fg = 81  # Light blue
        if context.container:
            attr |= bold
            fg = 201  # Magenta
        if context.directory:
            attr |= bold
            fg = 40  # Neon green
        elif context.executable and not any(
            (context.media, context.container, context.fifo, context.socket)
        ):
            attr |= bold
            fg = 82  # Bright green
        if context.socket:
            fg = 14  # Cyan
            attr |= bold
        if context.fifo or context.device:
            fg = 11  # Yellow
            if context.device:
                attr |= bold
        if context.link:
            fg = 45 if context.good else 196  # Cyan if good, red if bad
        if context.tag_marker and not context.selected:
            attr |= bold
            fg = 196  # Red
        if not context.selected and (context.cut or context.copied):
            fg = 233  # Very dark gray
            attr |= bold
        if context.main_column:
            if context.selected:
                attr |= bold
            if context.marked:
                attr |= bold
                fg = 11  # Yellow
        if context.badinfo:
            if attr & reverse:
                bg = 196  # Red
            else:
                fg = 196  # Red

        if context.inactive_pane:
            fg = 242  # Dark gray

        return fg, bg, attr

    def verify_titlebar(self, context, fg, bg, attr):
        attr |= bold
        if context.hostname:
            fg = 196 if context.bad else 40  # Red if bad, green if good
        elif context.directory:
            fg = 45  # Cyan
        elif context.tab:
            if context.good:
                bg = 40  # Green
        elif context.link:
            fg = 45  # Cyan

        return fg, bg, attr

    def verify_statusbar(self, context, fg, bg, attr):
        if context.permissions:
            if context.good:
                fg = 40  # Green
            elif context.bad:
                fg = 196  # Red
        if context.marked:
            attr |= bold | reverse
            fg = 11  # Yellow
        if context.frozen:
            attr |= bold | reverse
            fg = 45  # Cyan
        if context.message:
            if context.bad:
                attr |= bold
                fg = 196  # Red
        if context.loaded:
            bg = self.progress_bar_color
        if context.vcsinfo:
            fg = 45  # Cyan
            attr &= ~bold
        if context.vcscommit:
            fg = 11  # Yellow
            attr &= ~bold
        if context.vcsdate:
            fg = 45  # Cyan
            attr &= ~bold

        return fg, bg, attr

    def verify_taskview(self, context, fg, bg, attr):
        if context.title:
            fg = 45  # Cyan

        if context.selected:
            attr |= reverse

        if context.loaded:
            if context.selected:
                fg = self.progress_bar_color
            else:
                bg = self.progress_bar_color

        return fg, bg, attr

    def verify_vcsfile(self, context, fg, bg, attr):
        attr &= ~bold
        if context.vcsconflict:
            fg = 196  # Red
        elif context.vcschanged:
            fg = 214  # Orange
        elif context.vcsunknown:
            fg = 245  # Light gray
        elif context.vcsstaged:
            fg = 40  # Green
        elif context.vcssync:
            fg = 45  # Cyan
        elif context.vcsignored:
            fg = 240  # Dark gray

        return fg, bg, attr

    def verify_vcsremote(self, context, fg, bg, attr):
        attr &= ~bold
        if context.vcssync or context.vcsnone:
            fg = 45  # Cyan
        elif context.vcsbehind:
            fg = 196  # Red
        elif context.vcsahead:
            fg = 40  # Green
        elif context.vcsdiverged:
            fg = 214  # Orange
        elif context.vcsunknown:
            fg = 245  # Light gray

        return fg, bg, attr

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            fg, bg, attr = self.verify_browser(context, fg, bg, attr)

        elif context.in_titlebar:
            fg, bg, attr = self.verify_titlebar(context, fg, bg, attr)

        elif context.in_statusbar:
            fg, bg, attr = self.verify_statusbar(context, fg, bg, attr)

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            fg, bg, attr = self.verify_taskview(context, fg, bg, attr)

        if context.vcsfile and not context.selected:
            fg, bg, attr = self.verify_vcsfile(context, fg, bg, attr)

        elif context.vcsremote and not context.selected:
            fg, bg, attr = self.verify_vcsremote(context, fg, bg, attr)

        return fg, bg, attr
