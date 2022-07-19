from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.metaclasses import HighchartsMeta
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class Zone(HighchartsMeta):
    """A zone defined within a series.

    Zones can be applied to the X axis, Y axis or Z axis for bubbles, according to the
    :meth:`zone_axis <AreaOptions.zone_axis>` option.

    """

    def __init__(self, **kwargs):
        self._class_name = None
        self._color = None
        self._dash_style = None
        self._fill_color = None
        self._value = None

        self.class_name = kwargs.pop('class_name', None)
        self.color = kwargs.pop('color', None)
        self.dash_style = kwargs.pop('dash_style', None)
        self.fill_color = kwargs.pop('fill_color', None)
        self.value = kwargs.pop('value', None)

    @property
    def class_name(self) -> Optional[str]:
        """A custom class name for the zone.

        .. warning::

          Supported in :term:`styled mode` only.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """Defines the color of the series. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
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
    def dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the graph, or for some series types the
        outline of each shape. Defaults to :obj:`None <python:None>`.

        Accepts one of the following values:

          * 'Dash',
          * 'DashDot',
          * 'Dot',
          * 'LongDash',
          * 'LongDashDot',
          * 'LongDashDotDot',
          * 'ShortDash',
          * 'ShortDashDot',
          * 'ShortDashDotDot',
          * 'ShortDot',
          * 'Solid'

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._dash_style

    @dash_style.setter
    def dash_style(self, value):
        if not value:
            self._dash_style = None
        else:
            value = validators.string(value)
            if value not in constants.SUPPORTED_DASH_STYLE_VALUES:
                raise errors.HighchartsValueError(f'dash_style expects a recognized value'
                                                  f', but received: {value}')
            self._dash_style = value

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern]:
        """Fill color or gradient for the area.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        if not value:
            self._fill_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._fill_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._fill_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill_color = Gradient.from_dict(value)
                else:
                    self._fill_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._fill_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._fill_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._fill_color = Pattern.from_dict(value)
                else:
                    self._fill_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._fill_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def value(self) -> Optional[int | float | Decimal]:
        """The value up to where the zone extends. If :obj:`None <python:None>`, the zone
        stretches to the last value in the series. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._value

    @value.setter
    def value(self, value_):
        self._value = validators.numeric(value_, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.pop('className', None),
            'color': as_dict.pop('color', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'fill_color': as_dict.pop('fillColor', None),
            'value': as_dict.pop('value', None)
        }

        return cls(**kwargs)

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'className': self.class_name,
            'color': self.color,
            'dashStyle': self.dash_style,
            'fillColor': self.fill_color,
            'value': self.value
        }

        return self.trim_dict(untrimmed)