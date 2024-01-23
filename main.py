import classes.server
import util.getRoutes as gr

imported_modules = gr.import_files_from_folder("routes")

server = classes.server.server(imported_modules, "settings.conf")

server.run()