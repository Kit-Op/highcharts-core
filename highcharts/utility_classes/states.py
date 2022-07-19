from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.animation import AnimationOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class HoverState(HighchartsMeta):
    """Options for the hovered point/series."""

    def __init__(self, **kwargs):
        self._animation = None
        self._border_color = None
        self._brightness = 0.1
        self._color = None
        self._enabled = True

        self.animation = kwargs.pop('animation', None)
        self.border_color = kwargs.pop('border_color', None)
        self.brightness = kwargs.pop('brightness', 0.1)
        self.color = kwargs.pop('color', None)
        self.enabled = kwargs.pop('enabled', True)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Animation setting for hovering the graph in line-type series.

        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnimationOptions)
    def animation(self, value):
        self._animation = value

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """A specific border color for the hovered point. If :obj:`None <python:None>`,
        defaults to inherit the normal state border color.

        :returns: The border color for the hovered point.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def brightness(self) -> Optional[int | float | Decimal]:
        """How much to brighten the point on interaction. Defaults to ``0.1``.

        Requires the main color to be defined in hex or rgb(a) format.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = validators.numeric(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """A specific color for the hovered point.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern`, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def color(self) -> Optional[str]:
        """A specific color for the hovered point.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """Enable separate styles for the hovered series to visualize that the user hovers
        either the series itself or the legend. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.pop('animation', None),
            'border_color': as_dict.pop('borderColor', None),
            'brightness': as_dict.pop('brightness', 0.1),
            'color': as_dict.pop('color', None),
            'enabled': as_dict.pop('enabled', True)
        }

        return cls(**kwargs)

    def to_dict(self) -> dict:
        untrimmed = {
            'animation': self.animation,
            'borderColor': self.border_color,
            'brightness': self.brightness,
            'color': self.color,
            'enabled': self.enabled
        }

        return self.trim_dict(untrimmed)


class InactiveState(HighchartsMeta):
    """Options for the oppositive of a hovered point/series."""

    def __init__(self, **kwargs):
        self._animation = None
        self._enabled = True
        self._opacity = 0.2

        self.animation = kwargs.pop('animation', None)
        self.enabled = kwargs.pop('enabled', True)
        self.opacity = kwargs.pop('opacity', 0.2)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Animation setting when not hovering over the marker.

        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnimationOptions)
    def animation(self, value):
        self._animation = value

    @property
    def enabled(self) -> Optional[bool]:
        """Enable or disable the inactive state for the series. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def opacity(self) -> Optional[int | float | Decimal]:
        """Opacity of series elements (dataLabels, line, area). Defaults to ``0.2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        self._opacity = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.pop('animation', None),
            'enabled': as_dict.pop('enabled', True),
            'opacity': as_dict.pop('opacity', 0.2)
        }

        return cls(**kwargs)

    def to_dict(self) -> dict:
        untrimmed = {
            'animation': self.animation,
            'enabled': self.enabled,
            'opacity': self.opacity
        }

        return self.trim_dict(untrimmed)


class NormalState(HighchartsMeta):
    """Options for returning to a normal state after hovering"""

    def __init__(self, **kwargs):
        self._animation = None

        self.animation = kwargs.pop('animation', None)

    @property
    def animation(self) -> Optional[bool | AnimationOptions]:
        """Animation setting when returning to a normal state after hovering. Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :class:`AnimationOptions` or
          :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    def animation(self, value):
        if isinstance(value, bool):
            self._animation = value
        else:
            self._animation = validate_types(value,
                                             types = AnimationOptions)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.pop('animation', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> dict:
        untrimmed = {
            'animation': self.animation
        }

        return self.trim_dict(untrimmed)


class SelectState(HighchartsMeta):
    """Options for the selected point. These settings override the normal state options
    when a point is selected."""

    def __init__(self, **kwargs):
        self._animation = None
        self._border_color = None
        self._color = None
        self._enabled = True

        self.animation = kwargs.pop('animation', None)
        self.border_color = kwargs.pop('border_color', '#000000')
        self.color = kwargs.pop('color', '#cccccc')
        self.enabled = kwargs.pop('enabled', True)

    @property
    def animation(self) -> Optional[AnimationOptions]:
        """Animation setting for hovering the graph in line-type series.

        :rtype: :class:`AnimationOptions` or :obj:`None <python:None>`
        """
        return self._animation

    @animation.setter
    @class_sensitive(AnimationOptions)
    def animation(self, value):
        self._animation = value

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        """A specific border color for the selected point. Defaults to ``'#000000'``.

        :returns: The border color for the hovered point.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        if not value:
            self._border_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._border_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._border_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Gradient.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._border_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._border_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._border_color = Pattern.from_dict(value)
                else:
                    self._border_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._border_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """A specific color for the selected point. Defaults to ``'#cccccc'``.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern`, or
          :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Gradient.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._color = Pattern.from_dict(value)
                else:
                    self._color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def color(self) -> Optional[str]:
        """A specific color for the hovered point.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """Enable separate styles for the hovered series to visualize that the user hovers
        either the series itself or the legend. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.pop('animation', None),
            'border_color': as_dict.pop('borderColor', '#000000'),
            'color': as_dict.pop('color', '#cccccc'),
            'enabled': as_dict.pop('enabled', True)
        }

        return cls(**kwargs)

    def to_dict(self) -> dict:
        untrimmed = {
            'animation': self.animation,
            'borderColor': self.border_color,
            'color': self.color,
            'enabled': self.enabled
        }

        return self.trim_dict(untrimmed)


class States(HighchartsMeta):
    """Collection of state configuration settings that can be applied to series or
    markers."""

    def __init__(self, **kwargs):
        self._hover = None
        self._inactive = None
        self._normal = None
        self._select = None

        self.hover = kwargs.pop('hover', None)
        self.inactive = kwargs.pop('inactive', None)
        self.normal = kwargs.pop('normal', None)
        self.select = kwargs.pop('select', None)

    @property
    def hover(self) -> Optional[HoverState]:
        """Options for the hovered point/series.

        .. note::

          These settings override the normal state  options when a point/series is moused
          over or touched.

        :rtype: :class:`HoverState` or :obj:`None <python:None>`
        """
        return self._hover

    @hover.setter
    @class_sensitive(HoverState)
    def hover(self, value):
        self._hover = value

    @property
    def inactive(self) -> Optional[InactiveState]:
        """The opposite state of a hover for a series/point.

        :rtype: :class:`InactiveState` or :obj:`None <python:None>`
        """
        return self._inactive

    @inactive.setter
    @class_sensitive(InactiveState)
    def inactive(self, value):
        self._inactive = value

    @property
    def normal(self) -> Optional[NormalState]:
        """The normal state of a series, or for point items in column, pie and similar
        series.

        Currently only used for setting animation when returning to normal state from
        hover.

        :rtype: :class:`NormalState` or :obj:`None <python:None>`
        """
        return self._normal

    @normal.setter
    @class_sensitive(NormalState)
    def normal(self, value):
        self._normal = value

    @property
    def select(self) -> Optional[SelectState]:
        """Options for the selected point.

        These settings override the normal state options when a point is selected.

        :rtype: :class:`SelectState` or :obj:`None <python:None>`
        """
        return self._select

    @select.setter
    @class_sensitive(SelectState)
    def select(self, value):
        self._select = value

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'hover': as_dict.pop('hover', None),
            'inactive': as_dict.pop('inactive', None),
            'normal': as_dict.pop('normal', None),
            'select': as_dict.pop('select', None)
        }

        return cls(**kwargs)

    def to_dict(self):
        untrimmed = {
            'hover': self.hover,
            'inactive': self.inactive,
            'normal': self.normal,
            'select': self.select
        }

        return self.trim_dict(untrimmed)