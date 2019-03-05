from com.pnfsoftware.jeb.client.api import IScript, IGraphicalClientContext

class CollapseAll(IScript):
    def run(self, ctx):
        if not isinstance(ctx, IGraphicalClientContext):
            print('This script must be run within a graphical client')
            return
        
        views = ctx.getViews();
        for view in views:
            fragments = view.getFragments()
            for fragment in fragments:
                className = fragment.getClass().getSimpleName()
                if className == "CodeHierarchyView":
                    viewer = fragment.getViewer()
                    if viewer != None:
                        viewer.collapseAll()
                        break
