from django.utils import timezone

from .label_template import LabelTemplate
from .job_result import JobResult


class PrintLabelError(Exception):
    pass


class Label:

    """A class that prepares and prints copies of labels.
    """
    label_name = 'label'
    label_template_cls = LabelTemplate
    job_result_cls = JobResult
    label_template_name = None

    def __init__(self, label_template_name=None, printer=None):
        if label_template_name:
            self.label_template_name = label_template_name
        self.messages = None
        self.printer = printer
        self.label_template = self.label_template_cls(
            template_name=self.label_template_name)

    def __str__(self):
        return f'{self.label_template_name} using {self.printer}.'

    def print_label(self, copies=None, context=None):
        """ Prints the label or raises.
        """
        job_ids = []
        copies = copies or 1
        timestamp = timezone.now().strftime('%Y-%m-%d %H:%M')
        zpl_data = []
        for i in range(copies, 0, -1):
            context.update({
                'label_count': i,
                'label_count_total': copies,
                'timestamp': timestamp})
            zpl_data.append(self.label_template.render(context).encode('utf8'))
        zpl_data = b''.join(zpl_data)
        job_id = self.printer.stream_print(zpl_data=zpl_data)
        if not job_id:
            raise PrintLabelError('Print job failed.')
        job_ids.append(job_id)
        return self.job_result_cls(
            name=self.label_template_name, copies=copies, job_ids=job_ids,
            printer=self.printer)
