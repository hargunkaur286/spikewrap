# Include all public functions here. The preferred way to use spikewrap is
#
# ```
# import spikewrap as sw
# sw.Session()
# sw.show_configs()
# ...
# ```

# __all__ is used for sphinx autodoc.
# DO NOT make a docstring-style comment here. It will show up at the top of the autogenerated API reference.
#
# TODO
# ----
#  write a test to check all public functions / classes are included here.
from .structure.session import Session
from .utils.getters import get_example_data_path
from .configs.config_utils import (
    show_configs,
    get_configs_path,
    show_supported_preprocessing_steps,
    show_available_configs,
    load_config_dict,
    save_config_dict,
)
from .configs.hpc import default_slurm_options

# TODO: there must be a better way!
# this is necessary for doc api linking? can I just remove!?!??
__all__ = [
    "Session",
    "get_example_data_path",
    "show_configs",
    "get_configs_path",
    "show_supported_preprocessing_steps",
    "show_available_configs",
    "load_config_dict",
    "save_config_dict",
    "default_slurm_options",
    "get_raw_run_names",
    "get_preprocessed_run_names",
    "parent_input_path",
    "get_output_path",
    "load_raw_data",
    "get_sync_channel",
    "plot_sync_channel",
    "silence_sync_channel",
    "get_sync_channel",
]
