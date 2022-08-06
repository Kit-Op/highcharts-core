from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts import constants, errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.metaclasses import HighchartsMeta
from highcharts.legend.accessibility import LegendAccessibilityOptions
from highcharts.legend.navigation import LegendNavigation
from highcharts.legend.bubble_legend import BubbleLegend
from highcharts.legend.title import LegendTitle
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.shadows import ShadowOptions
from highcharts.utility_classes.javascript_functions import CallbackFunction


class Legend(HighchartsMeta):
    """The legend is a box containing a symbol and name for each series item or point
    item in the chart. Each series (or points in case of pie charts) is represented by
    a symbol and its name in the legend.

    .. seealso::

      It is possible to override the symbol creator function and create
      `custom legend symbols <https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/studies/legend-custom-symbol/>`_.

    """

    def __init__(self, **kwargs):
        self._accessibility = None
        self._align = None
        self._align_columns = None
        self._background_color = None
        self._border_color = None
        self._border_width = None
        self._border_radius = None
        self._bubble_legend = None
        self._class_name = None
        self._enabled = None
        self._floating = None
        self._item_checkbox_style = None
        self._item_distance = None
        self._item_hidden_style = None
        self._item_hover_style = None
        self._item_margin_bottom = None
        self._item_margin_top = None
        self._item_style = None
        self._item_width = None
        self._label_format = None
        self._label_formatter = None
        self._layout = None
        self._margin = None
        self._max_height = None
        self._navigation = None
        self._padding = None
        self._reversed = None
        self._rtl = None
        self._shadow = None
        self._square_symbol = None
        self._symbol_height = None
        self._symbol_padding = None
        self._symbol_radius = None
        self._symbol_width = None
        self._title = None
        self._use_html = None
        self._vertical_align = None
        self._width = None
        self._x = None
        self._y = None

        self.accessibility = kwargs.pop('accessibility', None)
        self.align = kwargs.pop('align', None)
        self.align_columns = kwargs.pop('align_columns', None)
        self.background_color = kwargs.pop('background_color', None)
        self.border_color = kwargs.pop('border_color', None)
        self.border_width = kwargs.pop('border_width', None)
        self.border_radius = kwargs.pop('border_radius', None)
        self.bubble_legend = kwargs.pop('bubble_legend', None)
        self.class_name = kwargs.pop('class_name', None)
        self.enabled = kwargs.pop('enabled', None)
        self.floating = kwargs.pop('floating', None)
        self.item_checkbox_style = kwargs.pop('item_checkbox_style', None)
        self.item_distance = kwargs.pop('item_distance', None)
        self.item_hidden_style = kwargs.pop('item_hidden_style', None)
        self.item_hover_style = kwargs.pop('item_hover_style', None)
        self.item_margin_bottom = kwargs.pop('item_margin_bottom', None)
        self.item_margin_top = kwargs.pop('item_margin_top', None)
        self.item_style = kwargs.pop('item_style', None)
        self.item_width = kwargs.pop('item_width', None)
        self.label_format = kwargs.pop('label_format', None)
        self.label_formatter = kwargs.pop('label_formatter', None)
        self.layout = kwargs.pop('layout', None)
        self.margin = kwargs.pop('margin', None)
        self.max_height = kwargs.pop('max_height', None)
        self.navigation = kwargs.pop('navigation', None)
        self.padding = kwargs.pop('padding', None)
        self.reversed = kwargs.pop('reversed', None)
        self.rtl = kwargs.pop('rtl', None)
        self.shadow = kwargs.pop('shadow', None)
        self.square_symbol = kwargs.pop('square_symbol', None)
        self.symbol_height = kwargs.pop('symbol_height', None)
        self.symbol_padding = kwargs.pop('symbol_padding', None)
        self.symbol_radius = kwargs.pop('symbol_radius', None)
        self.symbol_width = kwargs.pop('symbol_width', None)
        self.title = kwargs.pop('title', None)
        self.use_html = kwargs.pop('use_html', None)
        self.vertical_align = kwargs.pop('vertical_align', None)
        self.width = kwargs.pop('width', None)
        self.x = kwargs.pop('x', None)
        self.y = kwargs.pop('y', None)

    @property
    def accessibility(self) -> Optional[LegendAccessibilityOptions]:
        """Accessibility options for the legend.

        .. note::

          Requires the Accessibility module.

        :rtype: :class:`LegendAccessibilityOptions` or :obj:`None <python:None>`
        """
        return self._accessibility

    @accessibility.setter
    @class_sensitive(LegendAccessibilityOptions)
    def accessibility(self, value):
        self._accessibility = value

    @property
    def align(self) -> Optional[str]:
        f"""The horizontal alignment of the legend box within the chart area. Defaults to
        ``'{constants.DEFAULT_LEGEND.get('align')}'``.

        Valid values are:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        In the case that the legend is aligned in a corner position, the
        :meth:`Legend.layout` setting will determine whether to place it above/below or on
        the side of the plot area.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._align

    @align.setter
    def align(self, value):
        if not value:
            self._align = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['left', 'center', 'right']:
                raise errors.HighchartsValueError(f'align must be either "left", "center"'
                                                  f', or "right". Was: "{value}"')
            self._align = value

    @property
    def align_columns(self) -> Optional[bool]:
        """If the layout is horizontal and the legend items span over two lines or more,
        if the value is ``True`` will align the items into vertical columns.

        Setting this to ``False`` makes room for more items, but will look more messy.

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>
        """
        return self._align_columns

    @align_columns.setter
    def align_columns(self, value):
        if value is None:
            self._align_columns = None
        else:
            self._align_columns = bool(value)

    @property
    def background_color(self) -> Optional[str | Gradient | Pattern]:
        f"""The background color or gradient for the legend. Defaults to
        :obj:`None <python:None>`.

        :returns: The backgorund color for the legend..
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        if not value:
            self._background_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._background_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._background_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Gradient.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._background_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._background_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._background_color = Pattern.from_dict(value)
                else:
                    self._background_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._background_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to a string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def border_color(self) -> Optional[str | Gradient | Pattern]:
        f"""The border color drawn around the legend. Defaults to
        ``'{constants.DEFAULT_LEGEND.get('border_color')}'``.

        :returns: The color of the legend border.
        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

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
    def border_radius(self) -> Optional[int | float | Decimal]:
        f"""The border radius (in pixels) applied to the legend border. Defaults to
        ``{constants.DEFAULT_LEGEND.get('border_radius')}``.

        :returns: The border radius to apply to the legend border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = validators.numeric(value, allow_empty = True)

    @property
    def border_width(self) -> Optional[int | float | Decimal]:
        f"""The border width (in pixels) applied to the legend border. Defaults to
        ``{constants.DEFAULT_LEGEND.get('border_width')}``.

        :returns: The border width to apply to the legend border.
        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        self._border_width = validators.numeric(value, allow_empty = True)

    @property
    def bubble_legend(self) -> Optional[BubbleLegend]:
        """The bubble legend is an additional element in legend which presents the scale
        of the bubble series.

        Individual bubble ranges can be defined by user or calculated from series. In the
        case of automatically calculated ranges, a 1px margin of error is permitted.

        :rtype: :class:`BubbleLegend` or :obj:`None <python:None>`
        """
        return self._bubble_legend

    @bubble_legend.setter
    @class_sensitive(BubbleLegend)
    def bubble_legend(self, value):
        self._bubble_legend = value

    @property
    def class_name(self) -> Optional[str]:
        """A classname to apply styling using CSS.

        :returns: The classname to apply to enable styling via CSS.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        f"""If ``True``, displays the legend. If ``False``, hides the legend. Defaults to
        ``{constants.DEFAULT_LEGEND.get('enabled')}``.

        .. note::

          There is also a series-specific option,
          :meth:`PlotOptions.series.show_in_legend`, that can hide the series from the
          legend. In some series types this is ``False`` by default, so it must set to
          ``True`` in order to show the legend for the series.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def floating(self) -> Optional[bool]:
        f"""If ``True``, the plot area ignores the legend and can be rendered below the
        legend. If ``False``, the legend is rendered visually distinct (not overlapping)
        the plot area. Defaults to ``{constants.DEFAULT_LEGEND.get('floating')}``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>
        """
        return self._floating

    @floating.setter
    def floating(self, value):
        if value is None:
            self._floating = None
        else:
            self._floating = bool(value)

    @property
    def item_checkbox_style(self) -> Optional[str]:
        f"""Default styling for the checkbox next to a legend item when
        :meth:`Legend.show_checkbox` is ``True``. Defaults to:
        ``'{constants.DEFAULT_LEGEND.get('item_checkbox_style')}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._item_checkbox_style

    @item_checkbox_style.setter
    def item_checkbox_style(self, value):
        self._item_checkbox_style = validators.string(value, allow_empty = True)

    @property
    def item_distance(self) -> Optional[int | float | Decimal]:
        f"""In a legend with horizontal layout, the itemDistance defines the pixel distance
        between each item. Defaults to ``{constants.DEFAULT_LEGEND.get('item_distance')}.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._item_distance

    @item_distance.setter
    def item_distance(self, value):
        self._item_distance = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def item_hidden_style(self) -> Optional[str]:
        f"""Default styling for the legend item when the corresponding series or data
        point is hidden. Defaults to:
        ``'{constants.DEFAULT_LEGEND.get('item_hidden_style')}'``.

        .. warning::

          Only a subset of CSS is supported, notably those options related to text.

        .. note::

          Properties are inherited from :meth:`Legend.style` unless overridden here.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._item_hidden_style

    @item_hidden_style.setter
    def item_hidden_style(self, value):
        self._item_hidden_style = validators.string(value, allow_empty = True)

    @property
    def item_hover_style(self) -> Optional[str]:
        f"""Default styling for the legend item when the corresponding series or data
        point is in a hover state. Defaults to:
        ``'{constants.DEFAULT_LEGEND.get('item_hover_style')}'``.

        .. warning::

          Only a subset of CSS is supported, notably those options related to text.

        .. note::

          Properties are inherited from :meth:`Legend.style` unless overridden here.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._item_hover_style

    @item_hover_style.setter
    def item_hover_style(self, value):
        self._item_hover_style = validators.string(value, allow_empty = True)

    @property
    def item_margin_bottom(self) -> Optional[int | float | Decimal]:
        f"""The bottom margin expressed in pixels for each legend item. Defaults to
        ``{constants.DEFAULT_LEGEND.get('item_margin_bottom')}.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._item_margin_bottom

    @item_margin_bottom.setter
    def item_margin_bottom(self, value):
        self._item_margin_bottom = validators.numeric(value,
                                                      allow_empty = True,
                                                      minimum = 0)

    @property
    def item_margin_top(self) -> Optional[int | float | Decimal]:
        f"""The top margin expressed in pixels for each legend item. Defaults to
        ``{constants.DEFAULT_LEGEND.get('item_margin_top')}.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._item_margin_top

    @item_margin_top.setter
    def item_margin_top(self, value):
        self._item_margin_top = validators.numeric(value,
                                                      allow_empty = True,
                                                      minimum = 0)

    @property
    def item_style(self) -> Optional[str]:
        f"""Default styling for each legend item. Defaults to:
        ``'{constants.DEFAULT_LEGEND.get('item_style')}'``.

        .. warning::

          Only a subset of CSS is supported, notably those options related to text.
          However, a ``"width"`` property can be added to control the text width.

        .. note::

          The default ``"textOverflow"`` property makes long texts truncate. Set it to
          ``undefined`` to wrap text instead.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._item_style

    @item_style.setter
    def item_style(self, value):
        self._item_style = validators.string(value, allow_empty = True)

    @property
    def item_width(self) -> Optional[int | float | Decimal]:
        f"""The width for each legend item, expressed in pixels. Defaults to
        ``{constants.DEFAULT_LEGEND.get('item_width')}.

        By default, the items are laid out successively. In a horizontal layout, if the
        items are laid out across two rows or more, they will be vertically aligned
        depending on the :meth:`Legend.align_columns` setting.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._item_width

    @item_width.setter
    def item_width(self, value):
        self._item_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def label_format(self) -> Optional[str]:
        f"""A format string for each legend label. Defaults to:
        ``'{constants.DEFAULT_LEGEND.get('label_format')}'``.

        .. note::

          Available variables relate to properties on the ``{{series}}``, or the
          ``{{point}}`` in the case of pie charts.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._label_format

    @label_format.setter
    def label_format(self, value):
        self._label_format = validators.string(value, allow_empty = True)

    @property
    def label_formatter(self) -> Optional[CallbackFunction]:
        """A JavaScript callback function that formats each of the series' labels.

        .. note::

          The (JavaScript) ``this`` keyword refers to the series object for most chart
          types, and refers to the point object for pie charts.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._label_formatter

    @label_formatter.setter
    @class_sensitive(CallbackFunction)
    def label_formatter(self, value):
        self._label_formatter = value

    @property
    def layout(self) -> Optional[str]:
        f"""The layout of the legend items. Defaults to
        ``'{constants.DEFAULT_LEGEND.get('layout')}'``.

        Accepts:

          * ``'horizontal'``
          * ``'vertical'``
          * ``'proximate'``

        When proximate, the legend items will be placed as close as possible to the graphs
        they're representing, except in inverted charts or when the legend position does
        not allow it.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>
        """
        return self._layout

    @layout.setter
    def layout(self, value):
        if not value:
            self._layout = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['horizontal', 'vertical', 'proximate']:
                raise errors.HighchartsValueError(f'layout must be either "horizontal", '
                                                  f', "vertical", or "proximate". Was: '
                                                  f'"{value}"')
            self._layout = value

    @property
    def margin(self) -> Optional[int | float | Decimal]:
        f"""If the plot area sized is calculated automatically and the legend is not
        floating, the legend margin is the space between the legend and the axis labels or
        plot area. Defaults to ``{constants.DEFAULT_LEGEND.get('margin')}.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin

    @margin.setter
    def margin(self, value):
        self._margin = validators.numeric(value,
                                          allow_empty = True)

    @property
    def max_height(self) -> Optional[int | float | Decimal]:
        f"""The maximum height for the legend, expressed in pixels. Defaults to
        ``{constants.DEFAULT_LEGEND.get('max_height')}.

        When the maximum height is extended, navigation will show.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_height

    @max_height.setter
    def max_height(self, value):
        self._max_height = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def navigation(self) -> Optional[LegendNavigation]:
        """Options for paging or navigation within the legend when the legend overflows
        the available space.

        .. hint::

          Navigation works well on screen, but not in static exported images. One way of
          working around that is to increase the chart height in export.

        :rtype: :class:`LegendNavigation` or :obj:`None <python:None>`
        """
        return self._navigation

    @navigation.setter
    @class_sensitive(LegendNavigation)
    def navigation(self, value):
        self._navigation = value

    @property
    def padding(self) -> Optional[int | float | Decimal]:
        f"""The inner padding of the legend box. Defaults to
        ``{constants.DEFAULT_LEGEND.get('padding')}.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._padding

    @padding.setter
    def padding(self, value):
        self._padding = validators.numeric(value, allow_empty = True)

    @property
    def reversed(self) -> Optional[bool]:
        f"""If ``True``, reverses the order of the legend items compared to the order of
        series/points as defined in the configuration object.
        Defaults to ``{constants.DEFAULT_LEGEND.get('reversed')}``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>
        """
        return self._reversed

    @reversed.setter
    def reversed(self, value):
        if value is None:
            self._reversed = None
        else:
            self._reversed = bool(value)

    @property
    def rtl(self) -> Optional[bool]:
        f"""If ``True``, displays the symbol on the right side of the text rather than
        the left (this is common in RTL languages like Arabic or Hebrew). Defaults to
        ``{constants.DEFAULT_LEGEND.get('rtl')}``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>
        """
        return self._rtl

    @rtl.setter
    def rtl(self, value):
        if value is None:
            self._rtl = None
        else:
            self._rtl = bool(value)

    @property
    def shadow(self) -> Optional[bool | ShadowOptions]:
        """Configuration of a drop shadow applied to the legend box. Accepts either
        a boolean value of ``False`` which disables any shadow, or a
        :class:`ShadowOptions` instance with the applicable configuration.

        Defaults to ``False``.

        .. warning::

          Requires that :meth:`Legend.background_color` be set.

        :rtype: :class:`bool <python:bool>` or :class:`ShadowOptions` or
          :obj:`None <python:None>`
        """
        return self._shadow

    @shadow.setter
    def shadow(self, value):
        if value is None:
            self._shadow = None
        elif value is False:
            self._shadow = False
        else:
            value = validate_types(value,
                                   types = ShadowOptions,
                                   allow_none = False)
            self._shadow = value

    @property
    def square_symbol(self) -> Optional[bool]:
        f"""If ``True``, the legend symbol width will be the same as the symbol height,
        which in turn defaults to the font size of the legend items. Defaults to
        ``{constants.DEFAULT_LEGEND.get('square_symbol')}``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>
        """
        return self._square_symbol

    @square_symbol.setter
    def square_symbol(self, value):
        if value is None:
            self._square_symbol = None
        else:
            self._square_symbol = bool(value)

    @property
    def symbol_height(self) -> Optional[int | float | Decimal]:
        """The height of the symbol (in pixels) for series types that use a rectangle in
        the legend. Defaults to the font size of legend items.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._symbol_height

    @symbol_height.setter
    def symbol_height(self, value):
        self._symbol_height = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def symbol_padding(self) -> Optional[int | float | Decimal]:
        f"""The pixel padding between the legend item symbol and the item text. Defaults
        to ``{constants.DEFAULT_LEGEND.get('symbol_padding')}.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._symbol_padding

    @symbol_padding.setter
    def symbol_padding(self, value):
        self._symbol_padding = validators.numeric(value, allow_empty = True)

    @property
    def symbol_radius(self) -> Optional[int | float | Decimal]:
        """The border radius of symbol for series types that use a rectangle in the
        legend. Defaults to one half of the :class:`Legend.symbol_height`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._symbol_radius

    @symbol_radius.setter
    def symbol_radius(self, value):
        self._symbol_radius = validators.numeric(value, allow_empty = True)

    @property
    def symbol_width(self) -> Optional[int | float | Decimal]:
        """The width of the legend item symbol (in pixels). When
        :meth:`Legend.square_symbol` is ``True``, this defaults to the
        :meth:`Legend.symbol_height`, otherwise ``16``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._symbol_width

    @symbol_width.setter
    def symbol_width(self, value):
        self._symbol_width = validators.numeric(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def title(self) -> Optional[LegendTitle]:
        """A title to be added on top of the legend.

        :rtype: :class:`LegendTitle` or :obj:`None <python:None>`
        """
        return self._title

    @title.setter
    @class_sensitive(LegendTitle)
    def title(self, value):
        self._title = value

    @property
    def use_html(self) -> Optional[bool]:
        """If ``True``, will use HTML to render the legend item texts. If ``False``, will
        use SVG or WebGL as applicable.

        Defaults to ``False``.

        :returns: Flag indicating whether to render annotation labels using HTML.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>
        """
        return self._use_html

    @use_html.setter
    def use_html(self, value):
        if value is None:
            self._use_html = None
        else:
            self._use_html = bool(value)

    @property
    def vertical_align(self) -> Optional[str]:
        f"""The vertical alignment of the legend box. Defaults to
        ``'{constants.DEFAULT_LEGEND.get('vertical_align')}'``.

        Accepts:

          * ``'bottom'``
          * ``'middle'``
          * ``'top'``

        .. hint::

          Vertical position can be further determined by the :meth:`Legend.y` option.

        .. note::

          If the legend is aligned in a corner position, the :meth:`Legend.layout` setting
          will determine whether to place it above/below or on the side of the plot area.

          When the layout option is ``'proximate'``, the ``vertical_align`` option
          does not apply.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_align

    @vertical_align.setter
    def vertical_align(self, value):
        if not value:
            self._vertical_align = None
        else:
            value = validators.string(value, allow_empty = True)
            value = value.lower()
            if value not in ['bottom', 'middle', 'top']:
                raise errors.HighchartsValueError(f'vertical_align expects either "top", '
                                                  f'"middle", or "bottom". Was: {value}')
            self._vertical_align = value

    @property
    def width(self) -> Optional[str | int | float | Decimal]:
        """The width of the legend box. If expressed as a numeric value, the value is in
        pixels. If as a :str:class:`str <python:str>`, then accepts a value expressed as a
        percentage of the chart area (e.g. ``'40%'``).

        If :obj:`None <python:None>`, then defaults to the full chart width if above or
        below the chart and half the chart width aligned to the left or right of the
        chart.

        Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        if not value:
            self._width = None
        else:
            try:
                self._width = validators.string(value)
            except ValueError:
                self._width = validators.numeric(value,
                                                 minimum = 0)

    @property
    def x(self) -> Optional[int]:
        f"""The x position offset of the legend relative to its horizontal alignment
        (:meth:`Legend.align`) within :meth:`Chart.spacing_left` and
        :meth:`Chart.spacing_right`. Defaults to ``{constants.DEFAULT_LEGEND.get('x')}``.

        .. note::

          Negative values move it to the left, positive values move it to the right.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        value = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int]:
        f"""The y position offset of the legend relative to its vertical alignment
        (:meth:`Legend.vertical_align`) within :meth:`Chart.spacing_top` and
        :meth:`Chart.spacing_bottom`. Defaults to ``{constants.DEFAULT_LEGEND.get('y')}``.

        .. note::

          Negative values move it up, positive values move it down.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        value = validators.numeric(value, allow_empty = True)

    @classmethod
    def from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.pop('accessibility', None),
            'align': as_dict.pop('align', None),
            'align_columns': as_dict.pop('alignColumns', None),
            'background_color': as_dict.pop('backgroundColor', None),
            'border_color': as_dict.pop('borderColor', None),
            'border_width': as_dict.pop('borderWidth', None),
            'border_radius': as_dict.pop('borderRadius', None),
            'bubble_legend': as_dict.pop('bubbleLegend', None),
            'class_name': as_dict.pop('className', None),
            'enabled': as_dict.pop('enabled', None),
            'floating': as_dict.pop('floating', None),
            'item_checkbox_style': as_dict.pop('itemCheckboxStyle', None),
            'item_distance': as_dict.pop('itemDistance', None),
            'item_hidden_style': as_dict.pop('itemHiddenStyle', None),
            'item_hover_style': as_dict.pop('itemHoverStyle', None),
            'item_margin_bottom': as_dict.pop('itemMarginBottom', None),
            'item_margin_top': as_dict.pop('itemMarginTop', None),
            'item_style': as_dict.pop('itemStyle', None),
            'item_width': as_dict.pop('itemWidth', None),
            'label_format': as_dict.pop('labelFormat', None),
            'label_formatter': as_dict.pop('labelFormatter', None),
            'layout': as_dict.pop('layout', None),
            'margin': as_dict.pop('margin', None),
            'max_height': as_dict.pop('maxHeight', None),
            'navigation': as_dict.pop('navigation', None),
            'padding': as_dict.pop('padding', None),
            'reversed': as_dict.pop('reversed', None),
            'rtl': as_dict.pop('rtl', None),
            'shadow': as_dict.pop('shadow', None),
            'square_symbol': as_dict.pop('squareSymbol', None),
            'symbol_height': as_dict.pop('symbolHeight', None),
            'symbol_padding': as_dict.pop('symbolPadding', None),
            'symbol_radius': as_dict.pop('symbolRadius', None),
            'symbol_width': as_dict.pop('symbolWidth', None),
            'title': as_dict.pop('title', None),
            'use_html': as_dict.pop('useHTML', None),
            'vertical_align': as_dict.pop('verticalAlign', None),
            'width': as_dict.pop('width', None),
            'x': as_dict.pop('x', None),
            'y': as_dict.pop('y', None),
        }

        return cls(**kwargs)

    def _to_untrimmed_dict(self) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'align': self.align,
            'alignColumns': self.align_columns,
            'backgroundColor': self.background_color,
            'borderColor': self.border_color,
            'borderWidth': self.border_width,
            'borderRadius': self.border_radius,
            'bubbleLegend': self.bubble_legend,
            'className': self.class_name,
            'enabled': self.enabled,
            'floating': self.floating,
            'itemCheckboxStyle': self.item_checkbox_style,
            'itemDistance': self.item_distance,
            'itemHiddenStyle': self.item_hidden_style,
            'itemHoverStyle': self.item_hover_style,
            'itemMarginBottom': self.item_margin_bottom,
            'itemMarginTop': self.item_margin_top,
            'itemStyle': self.item_style,
            'itemWidth': self.item_width,
            'labelFormat': self.label_format,
            'labelFormatter': self.label_formatter,
            'layout': self.layout,
            'margin': self.margin,
            'maxHeight': self.max_height,
            'navigation': self.navigation,
            'padding': self.padding,
            'reversed': self.reversed,
            'rtl': self.rtl,
            'shadow': self.shadow,
            'squareSymbol': self.square_symbol,
            'symbolHeight': self.symbol_height,
            'symbolPadding': self.symbol_padding,
            'symbolRadius': self.symbol_radius,
            'symbolWidth': self.symbol_width,
            'title': self.title,
            'useHTML': self.use_html,
            'verticalAlign': self.vertical_align,
            'width': self.width,
            'x': self.x,
            'y': self.y
        }

        return untrimmed
