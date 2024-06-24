# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.
# SubtleHack theme: A darker, less bright color scheme with border-only selection

from __future__ import absolute_import, division, print_function

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import (
    black, blue, cyan, green, magenta, red, white, yellow, default,
    normal, bold, reverse, underline, default_colors,
)

class SubtleHack(ColorScheme):
    progress_bar_color = 22  # Dark green

    def verify_browser(self, context, fg, bg, attr):
        if context.selected:
            attr = underline | bold
            fg = 7  # Light gray
        else:
            attr = normal
        if context.empty or context.error:
            fg = 1  # Dark red
        if context.border:
            fg = 240  # Dark gray
        if context.document:
            attr |= normal
            fg = 252  # Light gray
        if context.media:
            if context.image:
                fg = 5  # Dark magenta
            elif context.video:
                fg = 1  # Dark red
            elif context.audio:
                fg = 6  # Dark cyan
            else:
                fg = 2  # Dark green
        if context.container:
            fg = 5  # Dark magenta
        if context.directory:
            attr |= bold
            fg = 4  # Dark blue
        elif context.executable and not any(
            (context.media, context.container, context.fifo, context.socket)
        ):
            attr |= bold
            fg = 2  # Dark green
        if context.socket:
            fg = 5  # Dark magenta
        if context.fifo or context.device:
            fg = 3  # Dark yellow
            if context.device:
                attr |= bold
        if context.link:
            fg = 6 if context.good else 1  # Dark cyan if good, dark red if bad
        if context.tag_marker and not context.selected:
            attr |= bold
            fg = 1  # Dark red
        if not context.selected and (context.cut or context.copied):
            fg = 234  # Darker gray
            attr |= bold
        if context.main_column:
            if context.selected:
                attr |= underline
            if context.marked:
                attr |= underline
                fg = 3  # Dark yellow
        if context.badinfo:
            fg = 1  # Dark red

        if context.inactive_pane:
            fg = 242  # Dark gray

        return fg, bg, attr

    def verify_titlebar(self, context, fg, bg, attr):
        attr |= bold
        if context.hostname:
            fg = 1 if context.bad else 2  # Dark red if bad, dark green if good
        elif context.directory:
            fg = 4  # Dark blue
        elif context.tab:
            if context.good:
                fg = 2  # Dark green
        elif context.link:
            fg = 6  # Dark cyan

        return fg, bg, attr

    def verify_statusbar(self, context, fg, bg, attr):
        if context.permissions:
            if context.good:
                fg = 2  # Dark green
            elif context.bad:
                fg = 1  # Dark red
        if context.marked:
            attr |= bold | reverse
            fg = 3  # Dark yellow
        if context.frozen:
            attr |= bold | reverse
            fg = 6  # Dark cyan
        if context.message:
            if context.bad:
                attr |= bold
                fg = 1  # Dark red
        if context.loaded:
            bg = self.progress_bar_color
        if context.vcsinfo:
            fg = 4  # Dark blue
            attr &= ~bold
        if context.vcscommit:
            fg = 3  # Dark yellow
            attr &= ~bold

        return fg, bg, attr

    def verify_taskview(self, context, fg, bg, attr):
        if context.title:
            fg = 4  # Dark blue

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
            fg = 1  # Dark red
        elif context.vcschanged:
            fg = 3  # Dark yellow
        elif context.vcsunknown:
            fg = 245  # Light gray
        elif context.vcsstaged:
            fg = 2  # Dark green
        elif context.vcssync:
            fg = 4  # Dark blue
        elif context.vcsignored:
            fg = 240  # Dark gray

        return fg, bg, attr

    def verify_vcsremote(self, context, fg, bg, attr):
        attr &= ~bold
        if context.vcssync or context.vcsnone:
            fg = 4  # Dark blue
        elif context.vcsbehind:
            fg = 1  # Dark red
        elif context.vcsahead:
            fg = 2  # Dark green
        elif context.vcsdiverged:
            fg = 3  # Dark yellow
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
