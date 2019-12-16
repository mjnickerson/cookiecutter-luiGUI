import os
from luigi.contrib.external_program import ExternalProgramTask
from luigi import format, Parameter, WrapperTask, ExternalTask, Task, LocalTarget
from luigi.contrib.s3 import S3Target
from scripts.{{cookiecutter.node3_run_target}} import {{cookiecutter.node3_run_target}}


class Run_{{cookiecutter.graph_folder}}(WrapperTask):
    """
    Wrapper Task - to set Parameters for {{cookiecutter.graph_folder}}
    """
    def run(self):
        print("Running Lui_GUI graph {{cookiecutter.graph_folder}}!")

    def requires(self):
        {% if cookiecutter.active_nodes == "12345" %}
        return {{cookiecutter.node_4}}()
        {% endif %}
        {% if cookiecutter.active_nodes == "123" %}
        return {{cookiecutter.node_3}}()
        {% endif %}


class {{cookiecutter.node_2}}(ExternalTask):
    """
    {{cookiecutter.node_1}} for External File on S3
    """
    def output(self):
        return S3Target(r'{{cookiecutter.node1_target_entry}}', format=format.Nop) # <-- Node {{cookiecutter.node_1}}


class {{cookiecutter.node_3}}(Task):
    """
    Run task {{cookiecutter.node4_run_target}}
    """
    def requires(self):
        # Depends on the {{cookiecutter.node_2}}() being complete
        return {{cookiecutter.node_2}}()

    def run(self):
        {{cookiecutter.node3_run_target}}(self)

    def output(self):
        return LocalTarget(r"{{cookiecutter.node3_output_folder}}\{{cookiecutter.node1_target_filename}}", format=format.Nop)

{% if cookiecutter.active_nodes == "12345" %}
class {{cookiecutter.node_4}}(ExternalProgramTask):
    """
    Run the external program task {{cookiecutter.node4_run_target}}
    """
    source_image = r'{{cookiecutter.node4_input_params}}' #raw string to avoid escape characters
    output_folder = r'{{cookiecutter.node5_target_output}}'
    watermark_location = "topleft"

    def requires(self):
        """ Requires {{cookiecutter.node_2}} already downloaded
        """
        return {{cookiecutter.node_3}}()

    def program_args(self):
        """ Command line arguments to call external program Add_Watermark_Top_Left
        :return args: CLI args
        """
        # pattern: python <target_script.py> <source path> <input path> <output path> <args>
        return ['python','{{cookiecutter.node4_run_target}}', self.source_image, self.input().path, self.output().path, self.watermark_location]

    def output(self):
        self.file_name = os.path.basename(self.source_image)
        self.output_file_name = (os.path.splitext(self.file_name)[0]+"_watermarked"+os.path.splitext(self.file_name)[1])
        return LocalTarget(os.path.join(self.output_folder, self.output_file_name), format=format.Nop) # <-- {{cookiecutter.node_5}}
{% endif %}