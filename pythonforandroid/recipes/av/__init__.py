from pythonforandroid.toolchain import Recipe
from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.toolchain import Recipe


class PyAV(CythonRecipe):
    version = 'v10.0.0'
    url = 'https://github.com/PyAV-Org/PyAV/archive/v10.0.0.zip'

    depends = ['python3', 'ffmpeg']
    opt_depends = ['openssl', 'av_codecs']

    def get_recipe_env(self, arch, with_flags_in_cc=True):
        env = super().get_recipe_env(arch)

        build_dir = Recipe.get_recipe('ffmpeg', self.ctx).get_build_dir(arch.arch)
        env["PYAV_TESTDATA_DIR"] = self.get_build_dir(arch.arch)
        self.setup_extra_args = ["--ffmpeg-dir={}".format(build_dir)]

        return env

recipe = PyAV()
