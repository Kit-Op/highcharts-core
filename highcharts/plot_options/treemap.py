from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts import errors
from highcharts.decorators import class_sensitive, validate_types
from highcharts.plot_options.generic import GenericTypeOptions
from highcharts.plot_options.zones import Zone
from highcharts.plot_options.levels import TreemapLevelOptions
from highcharts.utility_classes.gradients import Gradient
from highcharts.utility_classes.patterns import Pattern
from highcharts.utility_classes.breadcrumbs import BreadcrumbOptions


class TreemapOptions(GenericTypeOptions):
    """General options to apply to all Treemap series types.

    A treemap displays hierarchical data using nested rectangles. The data can be laid
    out in varying ways depending on options.

    .. figure:: _static/treemap-example.png
      :alt: Treemap Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._animation_limit = None
        self._boost_blending = None
        self._boost_threshold = None
        self._border_radius = None
        self._color_axis = None
        self._color_key = None
        self._colors = None
        self._crop_threshold = None
        self._find_nearest_point_by = None
        self._get_extremes_for_all = None
        self._ignore_hidden_point = None
        self._linecap = None
        self._line_width = None
        self._negative_color = None
        self._point_interval = None
        self._point_interval_unit = None
        self._point_start = None
        self._relative_x_value = None
        self._soft_threshold = None
        self._stacking = None
        self._step = None
        self._zone_axis = None
        self._zones = None

        self._color_by_point = None
        self._color_index = None
        self._crisp = None
        self._allow_traversing_tree = None
        self._breadcrumbs = None
        self._level_is_constant = None
        self._levels = None

        self._alternate_starting_direction = None
        self._interact_by_leaf = None
        self._layout_algorithm = None
        self._layout_starting_direction = None
        self._sort_index = None

        self.animation_limit = kwargs.pop('animation_limit', None)
        self.boost_blending = kwargs.pop('boost_blending', None)
        self.boost_threshold = kwargs.pop('boost_threshold', 5000)
        self.color_axis = kwargs.pop('color_axis', None)
        self.color_key = kwargs.pop('color_key', None)
        self.colors = kwargs.pop('colors', None)
        self.crop_threshold = kwargs.pop('crop_threshold', 300)
        self.find_nearest_point_by = kwargs.pop('find_nearest_point_by', None)
        self.get_extremes_for_all = kwargs.pop('get_extremes_for_all', False)
        self.ignore_hidden_point = kwargs.pop('ignore_hidden_point', True)
        self.linecap = kwargs.pop('linecap', 'round')
        self.line_width = kwargs.pop('line_width', 2)
        self.negative_color = kwargs.pop('negative_color', None)
        self.point_interval = kwargs.pop('point_interval', 1)
        self.point_interval_unit = kwargs.pop('point_interval_unit', None)
        self.point_start = kwargs.pop('point_start', 0)
        self.relative_x_value = kwargs.pop('relative_x_value', False)
        self.soft_threshold = kwargs.pop('soft_threshold', True)
        self.stacking = kwargs.pop('stacking', None)
        self.step = kwargs.pop('step', None)
        self.zone_axis = kwargs.pop('zone_axis', 'y')
        self.zones = kwargs.pop('zones', None)

        self.color_index = kwargs.pop('color_index', None)
        self.crisp = kwargs.pop('crisp', None)
        self.allow_traversing_tree = kwargs.pop('allow_traversing_tree', None)
        self.breadcrumbs = kwargs.pop('breadcrumbs', None)
        self.color_by_point = kwargs.pop('color_by_point', None)
        self.level_is_constant = kwargs.pop('level_is_constant', None)
        self.levels = kwargs.pop('levels', None)

        self.alternate_starting_direction = kwargs.pop('alternate_starting_direction',
                                                       None)
        self.interact_by_leaf = kwargs.pop('interact_by_leaf', None)
        self.layout_algorithm = kwargs.pop('layout_algorithm', None)
        self.layout_starting_direction = kwargs.pop('layout_starting_direction', None)
        self.sort_index = kwargs.pop('sort_index', None)

        super().__init__(**kwargs)

    @property
    def allow_traversing_tree(self) -> Optional[bool]:
        """If ``True``, the user can click on a point which is a parent and zoom in on its
        children. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_traversing_tree

    @allow_traversing_tree.setter
    def allow_traversing_tree(self, value):
        if value is None:
            self._allow_traversing_tree = None
        else:
            self._allow_traversing_tree = bool(value)

    @property
    def alternate_starting_direction(self) -> Optional[bool]:
        """If ``True``, will make the treemap alternate the drawing direction between
        vertical and horizontal for each level. The next level's starting direction will
        always be the opposite of the previous. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._alternate_starting_direction

    @alternate_starting_direction.setter
    def alternate_starting_direction(self, value):
        if value is None:
            self._alternate_starting_direction = None
        else:
            self._alternate_starting_direction = bool(value)

    @property
    def animation_limit(self) -> Optional[int | float | Decimal]:
        """For some series, there is a limit that shuts down initial animation by default
        when the total number of points in the chart is too high. Defaults to
        :obj:`None <python:None>`.

        For example, for a column chart and its derivatives, animation does not run if
        there is more than 250 points totally. To disable this cap, set
        ``animation_limit`` to ``float("inf")`` (which represents infinity).

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._animation_limit

    @animation_limit.setter
    def animation_limit(self, value):
        if value == float('inf'):
            self._animation_limit = float('inf')
        else:
            self._animation_limit = validators.numeric(value,
                                                       allow_empty = True,
                                                       minimum = 0)

    @property
    def boost_blending(self) -> Optional[str]:
        """Sets the color blending in the boost module. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._boost_blending

    @boost_blending.setter
    def boost_blending(self, value):
        self._boost_blending = validators.string(value, allow_empty = True)

    @property
    def boost_threshold(self) -> Optional[int]:
        """Set the point threshold for when a series should enter boost mode. Defaults to
        ``5000``.

        Setting it to e.g. 2000 will cause the series to enter boost mode when there are
        2,000 or more points in the series.

        To disable boosting on the series, set the ``boost_threshold`` to ``0``. Setting
        it to ``1`` will force boosting.

        .. note::

          The :meth:`AreaOptions.crop_threshold` also affects this setting.

          When zooming in on a series that has fewer points than the ``crop_threshold``,
          all points are rendered although outside the visible plot area, and the
          ``boost_threshold`` won't take effect.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._boost_threshold

    @boost_threshold.setter
    def boost_threshold(self, value):
        self._boost_threshold = validators.integer(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def breadcrumbs(self) -> Optional[BreadcrumbOptions]:
        """Options for the breadcrumbs, the navigation at the top leading the way up
        through the traversed levels. Defaults to :obj:`None <python:None>`.

        """
        return self._breadcrumbs

    @breadcrumbs.setter
    @class_sensitive(BreadcrumbOptions)
    def breadcrumbs(self, value):
        self._breadcrumbs = value

    @property
    def color_axis(self) -> Optional[str | int | bool]:
        """When using dual or multiple color axes, this setting defines which
        :term:`color axis` the particular series is connected to. It refers to either the
        :meth:`ColorAxis.id` or the index of the axis in the :class:`ColorAxis` array,
        with ``0`` being the first. Set this option to ``False`` to prevent a series from
        connecting to the default color axis.

        Defaults to ``0``.

        :rtype: :obj:`None <python:None>` or :class:`str <python:str>` or
          :class:`int <python:int>` or :class:`bool <python:bool>`
        """
        return self._color_axis

    @color_axis.setter
    def color_axis(self, value):
        if value is None:
            self._color_axis = None
        elif value is False:
            self._color_axis = False
        else:
            try:
                self._color_axis = validators.string(value)
            except ValueError:
                self._color_axis = validators.integer(value,
                                                      minimum = 0)

    @property
    def color_by_point(self) -> bool:
        """When using automatic point colors pulled from the global colors or
        series-specific collections, this option determines whether the chart should
        receive one color per series (``False``) or one color per point (``True``).

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._color_by_point

    @color_by_point.setter
    def color_by_point(self, value):
        self._color_by_point = bool(value)

    @property
    def color_index(self) -> Optional[int]:
        """When operating in :term:`styled mode`, a specific color index to use for the
        series, so that its graphic representations are given the class name
        ``highcharts-color-{n}``.

        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._color_index

    @color_index.setter
    def color_index(self, value):
        self._color_index = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def color_key(self) -> Optional[str]:
        """Determines what data value should be used to calculate point color if
        :meth:`AreaOptions.color_axis` is used.

        .. note::

          Requires to set ``min`` and ``max`` if some custom point property is used or if
          approximation for data grouping is set to ``'sum'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color_key

    @color_key.setter
    def color_key(self, value):
        self._color_key = validators.string(value, allow_empty = True)

    @property
    def colors(self) -> Optional[List[str | Gradient | Pattern]]:
        """A series-specific or series type-specific color set to apply instead of the
        global colors when :meth:`ArcDiagramOptions.color_by_point` is ``True``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`,
          :class:`Gradient`, or :class:`Pattern` OR :obj:`None <python:None>`
        """
        return self._colors

    @colors.setter
    def colors(self, value):
        if not value:
            self._colors = None
        else:
            value = validators.iterable(value)
            checked_values = []
            for item in value:
                if isinstance(value, str):
                    checked_values.append(item)
                else:
                    processed_item = validate_types(item,
                                                    types = (Gradient, Pattern))
                    checked_values.append(processed_item)

            self._colors = checked_values

    @property
    def crisp(self) -> Optional[bool]:
        """If ``True``, each point or column edge is rounded to its nearest pixel in order
        to render sharp on screen. Defaults to ``True``.

        .. hint::

          In some cases, when there are a lot of densely packed columns, this leads to
          visible difference in column widths or distance between columns. In these cases,
          setting ``crisp`` to ``False`` may look better, even though each column is
          rendered blurry.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._crisp

    @crisp.setter
    def crisp(self, value):
        if value is None:
            self._crisp = None
        else:
            self._crisp = bool(value)

    @property
    def crop_threshold(self) -> Optional[int]:
        """When the series contains less points than the crop threshold, all points are
        drawn, even if the points fall outside the visible plot area at the current zoom.
        Defaults to ``300``.

        The advantage of drawing all points (including markers and columns), is that
        animation is performed on updates. On the other hand, when the series contains
        more points than the crop threshold, the series data is cropped to only contain
        points that fall within the plot area. The advantage of cropping away invisible
        points is to increase performance on large series.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._crop_threshold

    @crop_threshold.setter
    def crop_threshold(self, value):
        self._crop_threshold = validators.integer(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def find_nearest_point_by(self) -> Optional[str]:
        """Determines whether the series should look for the nearest point in both
        dimensions or just the x-dimension when hovering the series.

        If :obj:`None <python:None>`, defaults to ``'xy'`` for scatter series and ``'x'``
        for most other series. If the data has duplicate x-values, it is recommended to
        set this to ``'xy'`` to allow hovering over all points.

        Applies only to series types using nearest neighbor search (not direct hover) for
        tooltip.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._find_nearest_point_by

    @find_nearest_point_by.setter
    def find_nearest_point_by(self, value):
        self._find_nearest_point_by = validators.string(value, allow_empty = True)

    @property
    def get_extremes_for_all(self) -> Optional[bool]:
        """If ``True``, uses the Y extremes of the total chart width or only the zoomed
        area when zooming in on parts of the X axis. By default, the Y axis adjusts to the
        min and max of the visible data.

        .. warning::

          Applies to :term:`Cartesian series` only.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._get_extremes_for_all

    @get_extremes_for_all.setter
    def get_extremes_for_all(self, value):
        if value is None:
            self._get_extremes_for_all = None
        else:
            self._get_extremes_for_all = bool(value)

    @property
    def ignore_hidden_point(self) -> Optional[bool]:
        """If ``True``, the series shall be redrawn as if the hidden points were ``null``.
        If ``False``, hidden points will not be displayed but the slice will still be
        drawn as a gap in the pie.

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._ignore_hidden_point

    @ignore_hidden_point.setter
    def ignore_hidden_point(self, value):
        if value is None:
            self._ignore_hidden_point = None
        else:
            self._ignore_hidden_point = bool(value)

    @property
    def interact_by_leaf(self) -> Optional[bool]:
        """If ``True``, the user can only interact with leaf nodes. If ``False``, the user
        can interact with leaf and parent nodes. When :obj:`None <python:None>`, if
        :meth:`TreemapOptions.allow_traversing_tree` is ``True``, will default to
        ``False``. Otherwise will default to ``True``.

        Defaults to :obj:`None <python:None>`

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._interact_by_leaf

    @interact_by_leaf.setter
    def interact_by_leaf(self, value):
        if value is None:
            self._interact_by_leaf = None
        else:
            self._interact_by_leaf = bool(value)

    @property
    def layout_algorithm(self) -> Optional[str]:
        """This option decides which algorithm is used for setting position and dimensions
        of the points. Defaults to ``'sliceAndDice'``.

        Accepts the following (case-sensitive) values:

          * ``'sliceAndDice'``
          * ``'stripes'``
          * ``'squarified'``
          * ``'strip'``

        .. note::

          You also have the ability to extend Highcharts with your own layout algorithm.
          For more information, read the
          `original JavaScript documentation <https://www.highcharts.com/docs/chart-and-series-types/treemap#add-your-own-algorithm>`_.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._layout_algorithm

    @layout_algorithm.setter
    def layout_algorithm(self, value):
        self._layout_algorithm = validators.variable_name(value, allow_empty = True)

    @property
    def layout_starting_direction(self) -> Optional[str]:
        """Defines which direction the layout algorithm will start drawing. Defaults to
        ``'vertical'``.

        Accepts:

          * ``'vertical'``
          * ``'horizontal'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._layout_starting_direction

    @layout_starting_direction.setter
    def layout_starting_direction(self, value):
        if not value:
            self._layout_starting_direction = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['vertical', 'horizontal']:
                raise errors.HighchartsError(f'layout_starting_direction expects either '
                                             f'"vertical" or "horizontal". Received: '
                                             f'{value}')

            self._layout_starting_direction = value

    @property
    def level_is_constant(self) -> Optional[bool]:
        """If ``True``, the level will be the same as the tree structure. If ``False``,
        the first level visible when drilling is considered to be level one. Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._level_is_constant

    @level_is_constant.setter
    def level_is_constant(self, value):
        if value is None:
            self._level_is_constant = None
        else:
            self._level_is_constant = bool(value)

    @property
    def levels(self) -> Optional[List[TreemapLevelOptions]]:
        """Set options on specific levels. Takes precedence over series options, but not
        node and link options.

        :rtype: :obj:`None <python:None>`, or :class:`list <python:list>` of
          :class:`TreemapLevelOptions`
        """
        return self._levels

    @levels.setter
    @class_sensitive(TreemapLevelOptions, force_iterable = True)
    def levels(self, value):
        self._levels = value

    @property
    def linecap(self) -> Optional[str]:
        """The SVG value used for the ``stroke-linecap`` and ``stroke-linejoin`` of a line
        graph. Defaults to ``'round'``, which means that lines are rounded in the ends and
        bends.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._linecap

    @linecap.setter
    def linecap(self, value):
        self._linecap = validators.string(value, allow_empty = True)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the graph line. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def negative_color(self) -> Optional[str | Gradient | Pattern]:
        """The color for the parts of the graph or points that are below the
        :meth:`AreaOptions.threshold`.

        .. note::

          :meth:`Zones <AreaOptions.zones>` take precedence over the negative color.
          Using ``negative_color`` is equivalent to applying a zone with value of 0.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._negative_color

    @negative_color.setter
    def negative_color(self, value):
        if not value:
            self._negative_color = None
        elif isinstance(value, (Gradient, Pattern)):
            self._negative_color = value
        elif isinstance(value, (dict, str)) and 'linearGradient' in value:
            try:
                self._negative_color = Gradient.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._negative_color = Gradient.from_dict(value)
                else:
                    self._negative_color = validators.string(value)
        elif isinstance(value, dict) and 'linear_gradient' in value:
            self._negative_color = Gradient(**value)
        elif isinstance(value, (dict, str)) and 'patternOptions' in value:
            try:
                self._negative_color = Pattern.from_json(value)
            except ValueError:
                if isinstance(value, dict):
                    self._negative_color = Pattern.from_dict(value)
                else:
                    self._negative_color = validators.string(value)
        elif isinstance(value, dict) and 'pattern_options' in value:
            self._negative_color = Pattern(**value)
        else:
            raise errors.HighchartsValueError(f'Unable to resolve value to an '
                                              f'EnforcedNullType, string, '
                                              f'Gradient, or Pattern. Value received '
                                              f'was: {value}')

    @property
    def point_interval(self) -> Optional[int | float | Decimal]:
        """If no x values are given for the points in a series, ``point_interval`` defines
        the interval of the x values. Defaults to ``1``.

        For example, if a series contains one value every decade starting from year 0, set
        ``point_interval`` to ``10``. In true datetime axes, the ``point_interval`` is set
        in milliseconds.

        .. hint::

          ``point_interval`` can be also be combined with
          :meth:`point_interval_unit <AreaOptions.point_interval_unit>` to draw irregular
          time intervals.

        .. note::

          If combined with :meth:`relative_x_value <AreaOptions.relative_x_value>`, an x
          value can be set on each point, and the ``point_interval`` is added x times to
          the :meth:`point_start <AreaOptions.point_start>` setting.

        .. warning::

          This options applies to the series data, not the interval of the axis ticks,
          which is independent.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_interval

    @point_interval.setter
    def point_interval(self, value):
        self._point_interval = validators.numeric(value,
                                                  allow_empty = True,
                                                  minimum = 0)

    @property
    def point_interval_unit(self) -> Optional[str]:
        """On datetime series, this allows for setting the
        :meth:`point_interval <AreaOptions.point_interval>` to irregular time units, day,
        month, and year.

        A day is usually the same as 24 hours, but ``point_interval_unit`` also takes the
        DST crossover into consideration when dealing with local time.

        Combine this option with :meth:`point_interval <AreaOptions.point_interval>` to
        draw weeks, quarters, 6 month periods, 10 year periods, etc.

        .. warning::

          This options applies to the series data, not the interval of the axis ticks,
          which is independent.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_interval_unit

    @point_interval_unit.setter
    def point_interval_unit(self, value):
        self._point_interval_unit = validators.string(value, allow_empty = True)

    @property
    def point_start(self) -> Optional[int | float | Decimal]:
        """If no x values are given for the points in a series, ``point_start`` defines
        on what value to start. For example, if a series contains one yearly value
        starting from 1945, set ``point_start`` to ``1945``. Defaults to ``0``.

        .. note::

          If combined with :meth:`relative_x_value <AreaOptions.relative_x_value>`, an x
          value can be set on each point. The x value from the point options is multiplied
          by :meth:`point_interval <AreaOptions.point_interval>` and added to
          ``point_start`` to produce a modified x value.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_start

    @point_start.setter
    def point_start(self, value):
        self._point_start = validators.numeric(value, allow_empty = True)

    @property
    def relative_x_value(self) -> Optional[bool]:
        """When ``True``, X values in the data set are relative to the current
        :meth:`point_start <AreaOptions.point_start>`,
        :meth:`point_interval <AreaOptions.point_interval>`, and
        :meth:`point_interval_unit <AreaOptions.point_interval_unit>` settings. This
        allows compression of the data for datasets with irregular X values. Defaults to
        ``False``.

        The real X values are computed on the formula ``f(x) = ax + b``, where ``a`` is
        the :meth:`point_interval <AreaOptions.point_interval>` (optionally with a time
        unit given by :meth:`point_interval_unit <AreaOptions.point_interval_unit>`), and
        ``b`` is the :meth:`point_start <AreaOptions.point_start>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._relative_x_value

    @relative_x_value.setter
    def relative_x_value(self, value):
        if value is None:
            self._relative_x_value = None
        else:
            self._relative_x_value = bool(value)

    @property
    def soft_threshold(self) -> Optional[bool]:
        """When ``True``, the series will not cause the Y axis to cross the zero plane (or
        threshold option) unless the data actually crosses the plane. Defaults to
        ``True``.

        For example, if ``False``, a series of ``0, 1, 2, 3`` will make the Y axis show
        negative values according to the ``min_padidng`` option. If ``True``, the Y axis
        starts at 0.

        :rtype: :class:`bool <python:bool>`
        """
        return self._soft_threshold

    @soft_threshold.setter
    def soft_threshold(self, value):
        if value is None:
            self._soft_threshold = None
        else:
            self._soft_threshold = bool(value)

    @property
    def sort_index(self) -> Optional[int]:
        """The sort index of the point inside the treemap level. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._sort_index

    @sort_index.setter
    def sort_index(self, value):
        self._sort_index = validators.integer(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def stacking(self) -> Optional[str]:
        """Whether to stack the values of each series on top of each other. Defaults to
        :obj:`None <python:None>`.

        Acceptable values are:

          * :obj:`None <python:None>` to disable stacking,
          * ``"normal"`` to stack by value or
          * ``"percent"``
          * ``'stream'`` (for streamgraph series type only)
          * ``'overlap'`` (for waterfall series type only)

        .. note::

          When stacking is enabled, data must be sorted in ascending X order.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stacking

    @stacking.setter
    def stacking(self, value):
        if not value:
            self._stacking = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['normal', 'percent', 'stream', 'overlap']:
                raise errors.HighchartsValueError(f'stacking expects a valid stacking '
                                                  f'value. However, received: {value}')
            self._stacking = value

    @property
    def step(self) -> Optional[str]:
        """Whether to apply steps to the line. Defaults to :obj:`None <python:None>`.

        Possible values are:

          * :obj:`None <python:None>`
          * ``'left'``
          * ``'center'``
          * ``'right'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._step

    @step.setter
    def step(self, value):
        self._step = validators.string(value, allow_empty = True)

    @property
    def zone_axis(self) -> Optional[str]:
        """Defines the Axis on which the zones are applied. Defaults to ``'y'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zone_axis

    @zone_axis.setter
    def zone_axis(self, value):
        self._zone_axis = validators.string(value, allow_empty = True)

    @property
    def zones(self) -> Optional[List[Zone]]:
        """An array defining zones within a series. Defaults to :obj:`None <python:None>`.

        Zones can be applied to the X axis, Y axis or Z axis for bubbles, according to the
        :meth:`zone_axis <AreaOptions.zone_axis>` setting.

        .. warning::

          The zone definitions have to be in ascending order regarding to the value.

        :rtype: :obj:`None <python:None>` or :class:`list <python:list>` of
          :class:`Zone` instances
        """
        return self._zones

    @zones.setter
    @class_sensitive(Zone, force_iterable = True)
    def zones(self, value):
        self._zones = value

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
            'boost_threshold': as_dict.pop('boostThreshold', None),
            'color_axis': as_dict.pop('colorAxis', None),
            'color_key': as_dict.pop('colorKey', None),
            'colors': as_dict.pop('colors', None),
            'crop_threshold': as_dict.pop('cropThreshold', None),
            'find_nearest_point_by': as_dict.pop('findNearestPointBy', None),
            'get_extremes_for_all': as_dict.pop('getExtremesForAll', False),
            'ignore_hidden_point': as_dict.pop('ignoreHiddenPoint', True),
            'linecap': as_dict.pop('linecap', None),
            'line_width': as_dict.pop('lineWidth', None),
            'negative_color': as_dict.pop('negativeColor', None),
            'point_interval': as_dict.pop('pointInterval', None),
            'point_interval_unit': as_dict.pop('pointIntervalUnit', None),
            'point_start': as_dict.pop('pointStart', None),
            'relative_x_value': as_dict.pop('relativeXValue', None),
            'soft_threshold': as_dict.pop('softThreshold', None),
            'stacking': as_dict.pop('stacking', None),
            'step': as_dict.pop('step', None),
            'zone_axis': as_dict.pop('zoneAxis', None),
            'zones': as_dict.pop('zones', None),

            'color_index': as_dict.pop('colorIndex', None),
            'crisp': as_dict.pop('crisp', None),
            'allow_traversing_tree': as_dict.pop('allowTraversingTree', None),
            'breadcrumbs': as_dict.pop('breadcrumbs', None),
            'color_by_point': as_dict.pop('colorByPoint', None),
            'level_is_constant': as_dict.pop('levelIsConstant', None),
            'levels': as_dict.pop('levels', None),

            'alternate_starting_direction': as_dict.pop('alternateStartingDirection',
                                                        None),
            'interact_by_leaf': as_dict.pop('interactByLeaf', None),
            'layout_algorithm': as_dict.pop('layoutAlgorithm', None),
            'layout_starting_direction': as_dict.pop('layoutStartingDirection', None),
            'sort_index': as_dict.pop('sortIndex', None)
        }

        return kwargs

    def to_dict(self) -> dict:
        untrimmed = {
            'animationLimit': self.animation_limit,
            'boostBlending': self.boost_blending,
            'boostThreshold': self.boost_threshold,
            'colorAxis': self.color_axis,
            'colorKey': self.color_key,
            'colors': self.colors,
            'cropThreshold': self.crop_threshold,
            'findNearestPointBy': self.find_nearest_point_by,
            'getExtremesForAll': self.get_extremes_for_all,
            'ignoreHiddenPoint': self.ignore_hidden_point,
            'linecap': self.linecap,
            'lineWidth': self.line_width,
            'negativeColor': self.negative_color,
            'pointInterval': self.point_interval,
            'pointIntervalUnit': self.point_interval_unit,
            'pointStart': self.point_start,
            'relativeXValue': self.relative_x_value,
            'softThreshold': self.soft_threshold,
            'stacking': self.stacking,
            'step': self.step,
            'zoneAxis': self.zone_axis,
            'zones': self.zones,

            'colorIndex': self.color_index,
            'crisp': self.crisp,
            'allowTraversingTree': self.allow_traversing_tree,
            'breadcrumbs': self.breadcrumbs,
            'colorByPoint': self.color_by_point,
            'levelIsConstant': self.level_is_constant,
            'levels': self.levels,

            'alternateStartingDirection': self.alternate_starting_direction,
            'interactByLeaf': self.interact_by_leaf,
            'layoutAlgorithm': self.layout_algorithm,
            'layoutStartingDirection': self.layout_starting_direction,
            'sortIndex': self.sort_index
        }
        parent_as_dict = super(self).to_dict()

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return self.trim_dict(untrimmed)