from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        from babel.messages.frontend import compile_catalog

        cmd = compile_catalog()
        cmd.directory = "src/wtforms_formly/locale/"
        cmd.domain = "wtforms_formly"
        cmd.statistics = True
        cmd.finalize_options()
        cmd.run()
