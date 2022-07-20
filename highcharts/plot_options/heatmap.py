from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.plot_options.series import SeriesOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern


class HeatmapOptions(SeriesOptions):
    """General options to apply to all Heatmap series types.

    A heatmap is a graphical representation of data where the individual values
    contained in a matrix are represented as colors.

    .. warning::

      Heatmaps require that ``modules/heatmap`` is loaded client-side.

    .. figure:: _static/heatmap-example.png
      :alt: Heatmap Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._border_radius = None
        self._colsize = None
        self._null_color = None
        self._point_padding = None
        self._rowsize = None

        self.border_radius = kwargs.pop('border_radius', None)
        self.colsize = kwargs.pop('colsize', None)
        self.null_color = kwargs.pop('null_color', None)
        self.point_padding = kwargs.pop('point_padding', None)
        self.rowsize = kwargs.pop('rowsize', None)

        super().__init__(**kwargs)

    @property
    def border_radius(self) -> Optional[int | float | Decimal]:
        """The border radius for each heatmap item. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def colsize(self) -> Optional[int]:
        """The column size - how many X axis units each column in the heatmap should span.
        Defaults to ``1``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._colsize

    @colsize.setter
    def colsize(self, value):
        self._colsize = validators.integer(value,
                                           allow_empty = True,
                                           minimum = 1)

    @property
    def null_color(self) -> Optional[str | Gradient | Pattern]:
        """The color applied to null points. Defaults to ``'#f7f7f7'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._null_color

    @null_color.setter
    def null_color(self, value):
        if not value:
            self._null_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._null_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._null_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._null_color = Gradient.from_dict(value)
                else:
                    self._null_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._null_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._null_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._null_color = Pattern.from_dict(value)
                else:
                    self._null_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._null_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to an '
                                              f'EnforcedNullType, string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def point_padding(self) -> Optional[int | float | Decimal]:
        """Padding between the points in the heatmap. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_padding

    @point_padding.setter
    def point_padding(self, value):
        self._point_padding = validators.numeric(value, allow_empty = True)

    @property
    def rowsize(self) -> Optional[int]:
        """The row size - how many Y axis units each heatmap row should span. Defaults to
        ``1``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._rowsize

    @rowsize.setter
    def rowsize(self, value):
        self._rowsize = validators.integer(value,
                                           allow_empty = True,
                                           minimum = 1)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'allow_point_select': as_dict.pop('allowPointSelect', False),
            'animation': as_dict.pop('animation', None),
            'class_name': as_dict.pop('className', None),
            'clip': as_dict.pop('clip', True),
            'color': as_dict.pop('color', None),
            'cursor': as_dict.pop('cursor', None),
            'custom': as_dict.pop('custom', None),
            'dash_style': as_dict.pop('dashStyle', None),
            'data_labels': as_dict.pop('dataLabels', None),
            'description': as_dict.pop('description', None),
            'enable_mouse_tracking': as_dict.pop('enableMouseTracking', True),
            'events': as_dict.pop('events', None),
            'include_in_data_export': as_dict.pop('includeInDataExport', None),
            'keys': as_dict.pop('keys', None),
            'label': as_dict.pop('label', None),
            'linked_to': as_dict.pop('linkedTo', None),
            'marker': as_dict.pop('marker', None),
            'on_point': as_dict.pop('onPoint', None),
            'opacity': as_dict.pop('opacity', None),
            'point': as_dict.pop('point', None),
            'point_description_formatter': as_dict.pop('pointDescriptionFormatter', None),
            'selected': as_dict.pop('selected', False),
            'show_checkbox': as_dict.pop('showCheckbox', False),
            'show_in_legend': as_dict.pop('showInLegend', None),
            'skip_keyboard_navigation': as_dict.pop('skipKeyboardNavigation', None),
            'states': as_dict.pop('states', None),
            'threshold': as_dict.pop('threshold', None),
            'tooltip': as_dict.pop('tooltip', None),
            'turbo_threshold': as_dict.pop('turboThreshold', None),
            'visible': as_dict.pop('visible', True),

            'animation_limit': as_dict.pop('animationLimit', None),
            'boost_blending': as_dict.pop('boostBlending', None),
            'boost_threshold': as_dict.pop('boostThreshold', 5000),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_index': as_dict.pop('colorIndex', None),
            'color_key': as_dict.pop('colorKey', None),
            'connect_ends': as_dict.pop('connectEnds', None),
            'connect_nulls': as_dict.pop('connectNulls', False),
            'crisp': as_dict.pop('crisp', True),
            'crop_threshold': as_dict.pop('cropThreshold', 300),
            'data_sorting': as_dict.pop('dataSorting', None),
            'drag_drop': as_dict.pop('dragDrop', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'linecap': as_dict.pop('linecap', 'round'),
            'line_width': as_dict.pop('lineWidth', 2),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', 1),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_placement': as_dict.pop('pointPlacement', None),
            'point_start': as_dict.pop('pointStart', 0),
            'relative_x_value': as_dict.pop('relativeXValue', False),
            'shadow': as_dict.pop('shadow', False),
            'soft_threshold': as_dict.pop('softThreshold', True),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', 'y'),
            'zones': as_dict.pop('zones', None),

            'border_radius': as_dict.pop('borderRadius', None),
            'colsize': as_dict.pop('colsize', None),
            'null_color': as_dict.pop('nullColor', None),
            'point_padding': as_dict.pop('pointPadding', None),
            'rowsize': as_dict.pop('rowsize', None)
        }

        return kwargs

    def to_dict(self) -> Optional[dict]:
        untrimmed = {
            'borderRadius': self.border_radius,
            'colsize': self.colsize,
            'nullColor': self.null_color,
            'pointPadding': self.point_padding,
            'rowsize': self.rowsize
        }

        parent_as_dict = super().to_dict()
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)
