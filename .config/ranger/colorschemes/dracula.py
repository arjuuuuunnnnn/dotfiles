# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.
# This theme was inspired by "RougarouTheme" for ranger and modified for a hacker-style look
# Original: https://github.com/RougarouTheme/ranger

from __future__ import absolute_import, division, print_function

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import (
    black, blue, cyan, magenta, red, white, yellow, default,
    normal, bold, reverse, default_colors,
)

class HackerDracula(ColorScheme):
    progress_bar_color = 99  # Bright magenta

    def verify_browser(self, context, fg, bg, attr):
        if context.selected:
            attr = reverse
        else:
            attr = normal
        if context.empty or context.error:
            bg = 52  # Dark red
            fg = 15  # Bright white
        if context.border:
            fg = 39  # Cyan
            attr |= bold
        if context.document:
            attr |= normal
            fg = 123  # Light cyan
        if context.media:
            if context.image:
                attr |= normal
                fg = 141  # Light purple
            elif context.video:
                fg = 161  # Light red
            elif context.audio:
                fg = 49  # Cyan
            else:
                fg = 85  # Light green
        if context.container:
            attr |= bold
            fg = 208  # Orange
        if context.directory:
            attr |= bold
            fg = 39  # Cyan
        elif context.executable and not any(
            (context.media, context.container, context.fifo, context.socket)
        ):
            attr |= bold
            fg = 118  # Light green
        if context.socket:
            fg = 170  # Pink
            attr |= bold
        if context.fifo or context.device:
            fg = 214  # Orange
            if context.device:
                attr |= bold
        if context.link:
            fg = 51 if context.good else 161  # Cyan if good, light red if bad
        if context.tag_marker and not context.selected:
            attr |= bold
            fg = 161  # Light red
        if not context.selected and (context.cut or context.copied):
            fg = 243  # Gray
            attr |= bold
        if context.main_column:
            if context.selected:
                attr |= bold
            if context.marked:
                attr |= bold
                fg = 226  # Yellow
        if context.badinfo:
            if attr & reverse:
                bg = 161  # Light red
            else:
                fg = 161  # Light red

        if context.inactive_pane:
            fg = 60  # Dark cyan

        return fg, bg, attr

    def verify_titlebar(self, context, fg, bg, attr):
        attr |= bold
        if context.hostname:
            fg = 161 if context.bad else 118  # Light red if bad, light green if good
        elif context.directory:
            fg = 39  # Cyan
        elif context.tab:
            if context.good:
                bg = 118  # Light green
        elif context.link:
            fg = 51  # Cyan

        return fg, bg, attr

    def verify_statusbar(self, context, fg, bg, attr):
        if context.permissions:
            if context.good:
                fg = 118  # Light green
            elif context.bad:
                bg = 161  # Light red
                fg = 15  # Bright white
        if context.marked:
            attr |= bold | reverse
            fg = 226  # Yellow
        if context.frozen:
            attr |= bold | reverse
            fg = 51  # Cyan
        if context.message:
            if context.bad:
                attr |= bold
                fg = 161  # Light red
        if context.loaded:
            bg = self.progress_bar_color
        if context.vcsinfo:
            fg = 39  # Cyan
            attr &= ~bold
        if context.vcscommit:
            fg = 226  # Yellow
            attr &= ~bold
        if context.vcsdate:
            fg = 51  # Cyan
            attr &= ~bold

        return fg, bg, attr

    def verify_taskview(self, context, fg, bg, attr):
        if context.title:
            fg = 39  # Cyan

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
            fg = 161  # Light red
        elif context.vcschanged:
            fg = 214  # Orange
        elif context.vcsunknown:
            fg = 208  # Dark orange
        elif context.vcsstaged:
            fg = 118  # Light green
        elif context.vcssync:
            fg = 85  # Dark cyan
        elif context.vcsignored:
            fg = 240  # Dark gray

        return fg, bg, attr

    def verify_vcsremote(self, context, fg, bg, attr):
        attr &= ~bold
        if context.vcssync or context.vcsnone:
            fg = 85  # Dark cyan
        elif context.vcsbehind:
            fg = 161  # Light red
        elif context.vcsahead:
            fg = 118  # Light green
        elif context.vcsdiverged:
            fg = 208  # Orange
        elif context.vcsunknown:
            fg = 161  # Light red

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
