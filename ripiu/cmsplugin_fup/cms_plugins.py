import math

from django.templatetags.static import static
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import FUPPluginModel, FUPContainerPluginModel, FUPItemPluginModel, FUPItemPosition
from .admin import FUPItemPositionInline
# from django.conf import settings

@plugin_pool.register_plugin
class FUPItemPluginPublisher(CMSPluginBase):
    model = FUPItemPluginModel
    name = _('FUP item')
    module = "Ri+"
    render_template = 'ripiu/cmsplugin_fup/fup-item.html'
    allow_children = True
    require_parent = True
    parent_classes = ["FUPContainerPluginPublisher"]
    fieldsets = (
        ('', {
            'fields': ('background_color',)
        }), (_("Size"), {
            'fields': (('width', 'width_unit'),('height', 'height_unit'),)
        }), (_("Animation"), {
            'fields': (('animation', 'animation_duration'),)
        })
    )
    inlines = [FUPItemPositionInline]
    AUTO = "auto"
    def position(self, top = AUTO, left = AUTO):
        return {
            "top":    top,
            "left":   left,
        }
    
    def render(self, context, instance, placeholder):
        context = super(FUPItemPluginPublisher, self).render(context, instance, placeholder)
        positions = []
        for position in instance.fupitemposition_set.all():
            x = "%f%s" % (position.x, position.x_unit)
            y = "%f%s" % (position.y, position.y_unit)
            p = self.position(y, x)
            positions.append(p)
        frames = []
        animation = None
        if instance.animation:
            db_frames = instance.animation.frames.all()
            total_frames = len(db_frames)
            for i in range(total_frames):
                frame = db_frames[i]
                frames.append({
                    'percent': math.floor(100 / (total_frames + 1)) * (i+1),
                    'x': frame.x,
                    'y': frame.y,
                    'z': frame.z,
                })
            frames.append({
                'percent': 100,
                'x': 0,
                'y': 0,
                'z': 0,
            })
            animation = {
                'slug':     instance.animation.slug,
                'duration': instance.animation_duration.to_eng_string(),
                'frames':   frames,
            }
        context.update({
            'fid':              "fup-item-%d" % instance.id,
            'children':         instance.child_plugin_instances,
            'background_color': instance.background_color,
            'width':            "%d%s" % (instance.width, instance.width_unit),
            'height':           "%d%s" % (instance.height, instance.height_unit),
            'positions':        positions,
            'animation':        animation,
        })
        return context

@plugin_pool.register_plugin
class FUPContainerPluginPublisher(CMSPluginBase):
    model = FUPContainerPluginModel
    name = _('FUP container')
    module = "Ri+"
    render_template = 'ripiu/cmsplugin_fup/fup-container.html'
    allow_children = True
    child_classes = ["FUPItemPluginPublisher"]

@plugin_pool.register_plugin
class FUPPluginPublisher(CMSPluginBase):
    model = FUPPluginModel
    name = _('FUP')
    module = "Ri+"
    render_template = 'ripiu/cmsplugin_fup/fup.html'
    text_enabled = True
    allow_children = False
    # fields = ('name')
    def icon_src(self, instance):
        return static("cms/img/icons/plugins/link.png")
        
    def render(self, context, instance, placeholder):
        context = super(FUPPluginPublisher, self).render(context, instance, placeholder)
        context.update({
            'container': instance.fup_container,
            'name': instance.name,
        })
        return context
    
    def save_model(self, request, obj, form, change):
        if not change:
            from cms.api import add_plugin
            # placeholder = request.current_page.placeholders.get(slot = settings.RIPIU_FUP_PLACEHOLDER)
            placeholder = obj.placeholder
            container = add_plugin(
                placeholder   = placeholder,
                plugin_type   = FUPContainerPluginPublisher,
                language      = obj.language,
                position      = 'last-sibling',
                target        = None,
            )
            container.name = "fup-container-%d" % container.id
            container.save()
            obj.fup_container = container
        response = super(FUPPluginPublisher, self).save_model(
            request, obj, form, change
        )
        return response
