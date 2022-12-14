# Standard modules
from __future__ import annotations
from typing import TYPE_CHECKING
import logging

# External modules
import pygame as pg

# Local modules
if TYPE_CHECKING:
    from .window import Window
from .vector2d import Vec


class Scene:
    """Scene class"""

    def __init__(self, window: Window, args: dict = None) -> None:

        # Window and arguments
        self.window: Window = window
        self.args: dict = {} if args is None else args

        # Screen cache system
        self.screen_cache: bool = False
        self._screen: pg.Surface | None = None

    # PROPERTIES

    @property
    def screen(self) -> pg.Surface:
        return self._screen if self.screen_cache else self.window.screen

    @property
    def logger(self) -> logging.Logger:
        return self.window.app.logger

    @property
    def width(self) -> int:
        return self.window.screen.get_width()

    @property
    def height(self) -> int:
        return self.window.screen.get_height()

    @property
    def dimension(self) -> Vec:
        return Vec(self.window.screen.get_width(), self.window.screen.get_height())

    @property
    def dt(self) -> float:
        return self.window.clock.delta_time

    # ABSTRACT METHODS

    def init(self) -> None:
        """Startup tasks

        *Called after is initialized -
        Don't call this method manually*
        """

        pass

    def event(self, event: pg.event.Event) -> None:
        """Handle pygame event

        *Called when event is fired*
        """

        pass

    def render(self) -> None:
        """Render screen

        *Called every frame*
        """

        pass

    def early_update(self) -> None:
        """Early update tasks

        *Called every frame before event handling*
        """

        pass

    def update(self) -> None:
        """Normal update tasks

        *Called every frame before rendering*
        """

        pass

    def late_update(self) -> None:
        """Late update tasks

        *Called every frame after rendering*
        """

        pass

    def quit(self) -> None:
        """Shutdown tasks

        *Called before exiting scene -
        Don't call this method manually*
        """

        pass
