from typing import Optional

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.options.plot_options.dependencywheel import DependencyWheelOptions


class SankeyOptions(DependencyWheelOptions):
    """General options to apply to all Sankey series types.

    A sankey diagram is a type of flow diagram, in which the width of the link between
    two nodes is shown proportionally to the flow quantity.

    .. tabs::

      .. tab:: Standard Sankey

        .. figure:: ../../../_static/sankey-example.png
          :alt: Sankey Example Chart
          :align: center

      .. tab:: Inverted Sankey

        .. figure:: ../../../_static/sankey-example-inverted.png
          :alt: Inverted Sankey Example Chart
          :align: center

      .. tab:: Sankey with Outgoing Links

        .. figure:: ../../../_static/sankey-example-outgoing.png
          :alt: Sankey Example Chart with Outgoing Links
          :align: center

    """
    def __init__(self, **kwargs):
        self._link_color_mode = None
      
        self.link_color_mode = kwargs.get('link_color_mode', None)
      
        super().__init__(**kwargs)

    @property
    def link_color_mode(self) -> Optional[str]:
        """Determines color mode for sankey links. 
        
        Available options:
        
          * ``'from'`` - color of the sankey link will be the same as the ``.from`` node
          * ``'gradient'`` - color of the sankey link will be set to gradient between
            colors of the ``.from`` node and the ``.to`` node
          * ``'to'`` - color of the sankey link will be same as the ``.to``
          
        Defaults to ``'from'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._link_color_mode
    
    @link_color_mode.setter
    def link_color_mode(self, value):
        if not value:
            self._link_color_mode = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['from', 'gradient', 'to']:
                raise errors.HighchartsValueError(
                    f'link_color_mode expects a value of either "from", '
                    f'"gradient", or "to". Received "{value}"')
            self._link_color_mode = value
            
    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'center': as_dict.get('center', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'color_index': as_dict.get('colorIndex', None),
            'colors': as_dict.get('colors', None),
            'curve_factor': as_dict.get('curveFactor', None),
            'levels': as_dict.get('levels', None),
            'link_opacity': as_dict.get('linkOpacity', None),
            'min_link_width': as_dict.get('minLinkWidth', None),
            'node_padding': as_dict.get('nodePadding', None),
            'node_width': as_dict.get('nodeWidth', None),
            'start_angle': as_dict.get('startAngle', None),
            
            'link_color_mode': as_dict.get('linkColorMode', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'linkColorMode': self.link_color_mode,
        }
        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed
