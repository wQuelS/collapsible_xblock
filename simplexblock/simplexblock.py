import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin


class SimpleXBlock(XBlock, StudioEditableXBlockMixin):
    title = String(
        default="Title",
        help="editable title block",
    )
    content = String(
        default="Content",
        scope=Scope.content,
        help="editable content block",
    )

    editable_fields = ("title", "content")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        loader = ResourceLoader("simplexblock")
        data = dict(title=self.title, content=self.content)
        template = loader.render_django_template(
            "static/html/simplexblock.html", context=data
        )
        frag = Fragment(template)
        frag.add_css(self.resource_string("static/css/simplexblock.css"))
        frag.add_javascript(
            self.resource_string("static/js/src/simplexblock.js")
        )
        frag.initialize_js("SimpleXBlock")
        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            (
                "SimpleXBlock",
                """<simplexblock/>
             """,
            ),
            (
                "Multiple SimpleXBlock",
                """<vertical_demo>
                <simplexblock/>
                <simplexblock/>
                <simplexblock/>
                </vertical_demo>
             """,
            ),
        ]
