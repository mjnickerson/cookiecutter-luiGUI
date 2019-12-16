import os
from luigi.contrib.external_program import ExternalProgramTask
from luigi import format, Parameter, WrapperTask, ExternalTask, Task, LocalTarget
from luigi.contrib.s3 import S3Target
from lui_gui.src.target import SuffixPreservingLocalTarget
from scripts.{{cookiecutter.node3_run_target}} import {{cookiecutter.node3_run_target}}


class Run_{{cookiecutter.graph_folder}}(WrapperTask):
    """
    Wrapper Task - to set Parameters for file download
    """
    def run(self):
        print("Running Lui_GUI graph {{cookiecutter.graph_folder}}!")

    def requires(self):
        return {{cookiecutter.node_4}}


class {{cookiecutter.node_2}}(ExternalTask):
    # Fetch S3Target for External File on S3
    def output(self):
        return S3Target("{{cookiecutter.node1_target_entry}}",format=format.Nop) #this is node_1


class {{cookiecutter.node_3}}(Task):
    # Download to Local Target
    def requires(self):
        # Depends on the SavedModel ExternalTask being complete
        return {{cookiecutter.node_2}}

    def run(self):
        {{cookiecutter.node3_run_target}}(self)
        # Atomically copy the file locally
        # s3_atomic_download(self)

    def output(self):
        return LocalTarget("{{cookiecutter.node3_output_folder}}", format=format.Nop)


class {{cookiecutter.node_4}}(ExternalProgramTask):
    """
    Run the external program task {{cookiecutter.node4_run_target}}
    """

    output_folder = '{{cookiecutter.node5_target_output}}'

    def requires(self):
        """ Requires {{cookiecutter.node_2}} already downloaded
        :return model: Local Target of Model
        Note: passes Luigi Parameters for model
        """
        return {
            'file': {{cookiecutter.node_3}},
        }

    def program_args(self):
        """ Command line arguments to call external program {{cookiecutter.node_4}}
        :return args: CLI args
        """
        return ['{{cookiecutter.node4_run_target}} {{cookiecutter.node4_input_params}} {{cookiecutter.node3_output_folder}} {{cookiecutter.node5_target_output}} topleft']

    def run(self):
        # create missing directories
        if not os.path.exists(self.output_dir):  # if missing
            os.makedirs(self.output_dir) # create dir
        with self.output().temporary_path() as self.temp_output_path: # atomic write
            super().run()

    def output(self):
        self.file_name = os.path.basename(self.output_folder)
        self.output_file_name = (os.path.splitext(self.file_name)[0]+"_watermarked"+os.path.splitext(self.file_name)[1])
        return SuffixPreservingLocalTarget(os.path.join(self.output_folder, self.output_file_name),format=format.Nop) # <-- {{cookiecutter.node_5}}
